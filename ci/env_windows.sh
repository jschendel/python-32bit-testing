# By default temp and cache directories are on C:\. Fix that.
export TEMP="${AGENT_TEMPDIRECTORY}"
export TMP="${AGENT_TEMPDIRECTORY}"
export TMPDIR="${AGENT_TEMPDIRECTORY}"
export PIP_CACHE_DIR="${AGENT_TEMPDIRECTORY}\\pip-cache"

# Download and install Python from scratch onto D:\, instead of using the
# pre-installed versions that azure pipelines provides on C:\.
# Also use -DirectDownload to stop nuget from caching things on C:\.
nuget install "${PYTHON_PKG}" -Version "${PYTHON_VERSION}" \
-OutputDirectory "$PWD/pyinstall" -ExcludeVersion \
-Source "https://api.nuget.org/v3/index.json" \
-Verbosity detailed -DirectDownload -NonInteractive

pydir="$PWD/pyinstall/${PYTHON_PKG}"
export PATH="${pydir}/tools:${pydir}/tools/scripts:$PATH"
python -c "import sys, struct; print('#' * 70); print('python:', sys.version); print('version_info:', sys.version_info); print('bits:', struct.calcsize('P') * 8);"
