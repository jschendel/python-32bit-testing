import platform
import struct
import sys

# display this prior to running python_script.py
print(
    "#" * 100,
    f"python: {'.'.join(map(str, sys.version_info))}",
    f"os: {platform.uname().system.lower()}",
    f"bits: {struct.calcsize('P') * 8}",
    "#" * 100,
    sep="\n"
)
