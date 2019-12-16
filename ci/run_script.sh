#!/bin/bash -e

if [ "$(uname)" == "Windows" ]; then
    echo "setting windows path"
    pydir="$PWD/pyinstall/${PYTHON_PKG}"
    export PATH="${pydir}/tools:${pydir}/tools/scripts:$PATH"
fi

python python_info.py
python python_script.py
