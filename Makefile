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

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@pdm run pytest --cov --cov-config=pyproject.toml --cov-report=xml

.PHONY: build
build: clean-build ## Build wheel file
	@echo "🚀 Creating wheel file"
	@pdm build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@pdm run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@pdm run mkdocs serve

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
