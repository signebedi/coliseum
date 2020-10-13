# get version number
REGEX="[0-9]*\.[0-9]*\.[0-9]*"
VERSION=`grep -o "$REGEX" src/coliseum/_version.py`

# pull relevant commit messages from the git log and write to a temporary file
COMMITS=`git log $(git describe --tags --abbrev=0)..HEAD --pretty=%B | grep -E '^Added|^Removed|^Changed|^Fixed|^Docs|^Tests'`

# set a standard, simple message -- in the future, summarize from CHANGELOG
M=$(printf $'Release of version %s\n%s' $VERSION "$COMMITS")
# sed command brought to you by https://stackoverflow.com/a/1252191
MESSAGE=`echo "$M" | sed ':a;N;$!ba;s/\n/\<br\/\>/g'`

DRAFT="false"
PRE="false"
BRANCH="master"
GITHUB_ACCESS_TOKEN=`cat .github_token`

# get repo name and owner
REPO_REMOTE=$(git config --get remote.origin.url)

if [ -z $REPO_REMOTE ]; then
	echo "Not a git repository"
	exit 1
fi

REPO_NAME=$(basename -s .git $REPO_REMOTE)
REPO_OWNER=$(git config --get user.name)
API_JSON=$(printf '{"tag_name": "%s","target_commitish": "%s","name": "coliseum %s","body": "%s","draft": %s,"prerelease": %s}' "$VERSION" "$BRANCH" "$VERSION" "$MESSAGE" "$DRAFT" "$PRE" )
API_RESPONSE_STATUS=$(curl --data "$API_JSON" -s -i -H "Authorization: token $GITHUB_ACCESS_TOKEN" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases)
echo "$API_RESPONSE_STATUS"

git pull origin # then we pull the remote origin to ensure our internal versioning is correct

# finally deploy to pypi and clean up
python setup.py sdist bdist_wheel
twine upload dist/* --repository pypi --config-file .pypirc || echo failed to upload to PyPi # uses project-scoped API token for coliseum
rm -rf dist/