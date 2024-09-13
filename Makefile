.PHONY: install
install: ## Install the environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using PDM"
	@pdm install
	@pdm run pre-commit install

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Linting code: Running pre-commit"
	@pdm run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@pdm run mypy

.PHONY: check-main
check-main: ## Run code quality tools, excluding "no-commit-to-branch" pre-commit hook
	@echo "🚀 Linting code: Running pre-commit"
	@SKIP=no-commit-to-branch pdm run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@pdm run mypy

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@pdm run pytest --cov --cov-config=pyproject.toml --cov-report=xml --cov-report=term-missing

.PHONY: build
build: clean-build ## Build wheel file
	@echo "🚀 Creating wheel file"
	@pdm build

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@rm -rf dist

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
