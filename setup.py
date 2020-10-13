from glob import glob
import setuptools, re, os

with open("README.md", "r") as f:
    LONG_DESCRIPTION = re.sub(r'\!\[gladiator gif\]\(docs\/cropped.gif\)', '', f.read()) # substitute out the gif image

# based on https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
with open(os.path.join('src', 'coliseum', '_version.py')) as f:
    versionstr = f.read()
    regex = r"^__version__ = ['\"]([\d\.]*)['\"]"
    mo = re.search(regex, versionstr, re.M)
    VERSION = mo.group(1)

with open(os.path.join('src', 'coliseum', '_metadata.py')) as f:
    authorstr = f.read()
    regex = r"__author__ = [\'\"]([\w\- ]*)[\'\"]"
    mo = re.search(regex, authorstr, re.M)
    AUTHOR = mo.group(1)

with open(os.path.join('src', 'coliseum', '_metadata.py')) as f:
    licensestr = f.read()
    regex = r"__license__ = [\'\"]([\w]*)[\'\"]"
    mo = re.search(regex, licensestr, re.M)
    LICENSE = mo.group(1)

with open(os.path.join('src', 'coliseum', '_metadata.py')) as f:
    emailstr = f.read()
    regex = r"__email__ = [\'\"]([\w\-\@\. ]*)[\'\"]"
    mo = re.search(regex, emailstr, re.M)
    EMAIL = mo.group(1)

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

setuptools.setup(
    name="coliseum",
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    description="a simple, turn-based command line game in python",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/signebedi/coliseum",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    python_requires='>=3.6',
)