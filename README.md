# contribute-to-open-source

[![Release](https://img.shields.io/github/v/release/mikeweltevrede/contribute-to-open-source)](https://img.shields.io/github/v/release/mikeweltevrede/contribute-to-open-source)
[![Build status](https://img.shields.io/github/actions/workflow/status/mikeweltevrede/contribute-to-open-source/main.yml?branch=main)](https://github.com/mikeweltevrede/contribute-to-open-source/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/mikeweltevrede/contribute-to-open-source/branch/main/graph/badge.svg)](https://codecov.io/gh/mikeweltevrede/contribute-to-open-source)
[![Commit activity](https://img.shields.io/github/commit-activity/m/mikeweltevrede/contribute-to-open-source)](https://img.shields.io/github/commit-activity/m/mikeweltevrede/contribute-to-open-source)
[![License](https://img.shields.io/github/license/mikeweltevrede/contribute-to-open-source)](https://img.shields.io/github/license/mikeweltevrede/contribute-to-open-source)

Tool to help one to contribute to Open Source projects. Goal is to search Github for open issues that might be interesting.

- **Github repository**: <https://github.com/mikeweltevrede/contribute-to-open-source/>
- **Documentation** <https://github.com/mikeweltevrede/contribute-to-open-source/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:mikeweltevrede/contribute-to-open-source.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-pdm/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-pdm/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-pdm/features/codecov/).

## Releasing a new version



---

Repository initiated with [fpgmaas/cookiecutter-pdm](https://github.com/fpgmaas/cookiecutter-pdm).
