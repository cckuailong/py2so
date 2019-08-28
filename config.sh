#!/bin/bash

uname -a | grep 'ubuntu' > /dev/null
echo $?
if [ $? -eq 0 ]; then
    apt-get install python-dev cython python3-dev cython3
else
    yum install python-dev cython python3-dev cython3
fi
