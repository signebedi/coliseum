#!/bin/bash

# this script should help add an alias to bashrc and ensure that there is a coliseum virtual env containing all its dependencies
# there are a few areas for this script to be improved:
# 1. check if there is an alias already existing in .bashrc and, if so, replace it https://unix.stackexchange.com/a/32507

if [ $VIRTUAL_ENV ]

then
        pip install coliseum
        CMD=$(printf 'source %s/bin/activate && python -m coliseum && deactivate' $VIRTUAL_ENV)
        echo $CMD
        echo alias coliseum=\""$CMD"\" >> /home/$USER/.bashrc
else
        echo You are not running a virtualenv, we are creating one here...
        python3 -m venv venv || python36 -m venv venv || python -m venv venv || exit
        source $PWD/venv/bin/activate
        pip install coliseum
        CMD=$(printf 'source %s/bin/activate && python -m coliseum && deactivate' $VIRTUAL_ENV)
        echo $CMD
        echo alias coliseum=\""$CMD"\" >> /home/$USER/.bashrc
        deactivate
fi
