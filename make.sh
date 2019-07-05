#!/bin/bash -x
cp -f apilinux/apilinux.py apilinux/apilinux
python ./setup.py bdist_wheel
python3 ./setup.py bdist_wheel
