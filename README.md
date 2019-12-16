# python-32bit-testing

Repo for testing out Python code on a 32-bit platform on Azure Pipelines

Workflow:

- Create a new branch
- Modify `python_script.py` to include whatever code you want to test on a 32-bit platform
- Commit the changes and push the branch to `origin`
- View the output of `python_script.py` under the "Run Python Scripts" step in CI
