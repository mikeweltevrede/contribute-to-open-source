# Contributing
Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.
- Speaking of credit: this guideline is based on the one in [deptry](https://github.com/fpgmaas/deptry/blob/main/docs/contributing.md) by [fpgmaas](https://github.com/fpgmaas).

You can contribute in many ways.

## Types of contributions

### Reporting bugs
Report bugs at https://github.com/mikeweltevrede/contribute-to-open-source. If you are reporting a bug, please fill out all sections in the issue template comprehensively.

### Fixing bugs
Look through the [GitHub issues](https://github.com/mikeweltevrede/contribute-to-open-source/issues) for bugs. Anything tagged with `bug` and `help wanted` is open to whoever wants to implement a fix for it.

### Implementing features
Look through the [GitHub issues](https://github.com/mikeweltevrede/contribute-to-open-source/issues) for feature requests. Anything tagged with `enhancement` and `help wanted` is open to whoever wants to implement it.

### Writing documentation
We could always use more documentation, whether as part of the official documentation, in docstrings, or even on the web in blog posts, articles, and such.

### Submitting feedback
The best way to send feedback is to file an issue at https://github.com/mikeweltevrede/contribute-to-open-source/issues.

If you are proposing a new feature:
* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project and that contributions are welcome :)

## Get started!
Ready to contribute? Here's how to set up for local development.
- NB: This section will be developed more as the repository is being set up.

1. [Fork](https://github.com/mikeweltevrede/contribute-to-open-source/fork) the repository on GitHub.

1. Clone your fork locally:
    ```bash
    cd <directory_in_which_repo_should_be_created>
    git clone git@github.com:YOUR_NAME/contribute-to-open-source.git
    ```

1. Now you need to set up your local environment.
   - Create a virtual environment
   - Install the dependencies
   - Install pre-commit

1. Create a branch `branch-name` (note that branch naming policies will be enforced at a certain point and will be outlined later) for local development:
    ```bash
    git checkout -b branch-name
    ```

1. Now you can make your changes locally. If you are adding a feature or fixing a bug, make sure to add tests in the `tests` directory.

1. Once you're done, validate that all tests are passing.

1. Commit your changes and push your branch to GitHub:
    ```bash
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin branch-name
    ```

1. [Submit a pull request](https://github.com/mikeweltevrede/contribute-to-open-source/pulls) through GitHub.

## Pull request guidelines
Before you submit a pull request, ensure that it meets the following guidelines:

1. If the pull request adds functionality or fixes a bug, the pull request should include tests.
2. If the pull request adds functionality, the documentation in `docs` directory should probably be updated.
