# Logger Package
[![Release](https://github.com/obervinov/logger-package/actions/workflows/release.yaml/badge.svg)](https://github.com/obervinov/logger-package/actions/workflows/release.yaml)
[![CodeQL](https://github.com/obervinov/logger-package/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/obervinov/logger-package/actions/workflows/github-code-scanning/codeql)
[![PR](https://github.com/obervinov/logger-package/actions/workflows/pr.yaml/badge.svg?branch=main&event=pull_request)](https://github.com/obervinov/logger-package/actions/workflows/pr.yaml)

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/obervinov/logger-package?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/obervinov/logger-package?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/obervinov/logger-package?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/obervinov/logger-package?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/obervinov/logger-package?style=for-the-badge)

## <img src="https://github.com/obervinov/_templates/blob/main/icons/book.png" width="25" title="about"> About this project
This is an additional implementation over the **logging** module.

This module is designed for fast initialization and configuration of readable and structured logging.

## <img src="https://github.com/obervinov/_templates/blob/main/icons/github-actions.png" width="25" title="github-actions"> GitHub Actions
| Name  | Version |
| ------------------------ | ----------- |
| GitHub Actions Templates | [v1.0.1](https://github.com/obervinov/_templates/tree/v1.0.1) |


## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Supported functions
- Color selection depending on the logging level
- Structured and formatted message for more informative
- Loading the logger configuration and format from a environment varibales

## <img src="https://github.com/obervinov/_templates/blob/main/icons/stack2.png" width="20" title="install"> Installing
```bash
# Install current version
pip3 install git+https://github.com/obervinov/logger-package.git#egg=vault
# Install version by branch
pip3 install git+https://github.com/obervinov/logger-package.git@main#egg=vault
# Install version by tag
pip3 install git+https://github.com/obervinov/logger-package.git@v1.0.0#egg=vault
```

## <img src="https://github.com/obervinov/_templates/blob/main/icons/config.png" width="25" title="usage"> Usage example
### Environment variables
| Name  | Description | Default value |
| ------------------------ | ------------------------------------------------ | --------------------------------------------------------------------- |
| `LOGGER_FORMAT` | A string with the event logging format | `[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s` |
| `LOGGER_LEVEL` | Event logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL or NOT SET | `INFO` |
| `LOGGER_DATE_FORMAT` | Date format in logging event output | `%d/%b/%Y %H:%M:%S` |

### Examples
```python
"""Import module"""
from logger import log

"""Examples"""
"""error"""
log.error(f"[class.{__class__.__name__}] this error: {error}")

"""warning"""
log.warning(f"[class.{__class__.__name__}] this warning: {warn}")

"""info"""
log.info(f"[class.{__class__.__name__}] this info: {info}")
```
