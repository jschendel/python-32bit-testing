python -c "import sys, struct; print('#' * 70); print('python:', sys.version); print('version_info:', sys.version_info); print('bits:', struct.calcsize('P') * 8); print('#' * 70);"
python py32.py
