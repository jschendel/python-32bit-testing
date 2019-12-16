# By default temp and cache directories are on C:\. Fix that.
# export TEMP="${AGENT_TEMPDIRECTORY}"
# export TMP="${AGENT_TEMPDIRECTORY}"
# export TMPDIR="${AGENT_TEMPDIRECTORY}"
# export PIP_CACHE_DIR="${AGENT_TEMPDIRECTORY}\\pip-cache"

# Download and install Python from scratch onto D:\, instead of using the
# pre-installed versions that azure pipelines provides on C:\.
# Also use -DirectDownload to stop nuget from caching things on C:\.
nuget install "${PYTHON_PKG}" -Version "${PYTHON_VERSION}" \
-OutputDirectory "$PWD/pyinstall" -ExcludeVersion \
-Source "https://api.nuget.org/v3/index.json" \
-Verbosity detailed -NonInteractive
# -Verbosity detailed -DirectDownload -NonInteractive

pydir="$PWD/pyinstall/${PYTHON_PKG}"
export PATH="${pydir}/tools:${pydir}/tools/scripts:$PATH"
echo which python
python --version
sh ./test.sh
