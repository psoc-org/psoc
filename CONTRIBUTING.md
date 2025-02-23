# Development

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```shell
cd $PATH_TO_YOUR_BENCH # Assuming you've created a Frappe Bench
bench get-app https://github,com/psoc-org/psoc --branch dev
bench --site [YOUR SITE NAME] install-app psoc
```

### Contributing

This app uses pre-commit for code formatting and linting. Please install `pre-commit` and enable it for this repository:

```shell
cd apps/batwara
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- `ruff`
- `eslint`
- `prettier`
- `pyupgrade`

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

**CI:** Installs this app and runs unit tests on every push to develop branch.

**Linters:** Runs Frappe Semgrep Rules and pip-audit on every pull request.