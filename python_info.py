import struct
import sys

print('#' * 100)
print('python:', sys.version)
print('version_info:', sys.version_info)
print('bits:', struct.calcsize('P') * 8)
print('#' * 100)
