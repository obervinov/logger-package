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
| GitHub Actions Templates | [v1.0.13](https://github.com/obervinov/_templates/tree/v1.0.13) |


## <img src="https://github.com/obervinov/_templates/blob/main/icons/requirements.png" width="25" title="functions"> Supported functions
- Color selection depending on the logging level
- Structured and formatted message for more informative
- Loading the logger configuration and format from a environment variables

## <img src="https://github.com/obervinov/_templates/blob/main/icons/stack2.png" width="20" title="install"> Installing with Poetry
```bash
tee -a pyproject.toml <<EOF
[tool.poetry]
name = myproject"
version = "1.0.0"

[tool.poetry.dependencies]
python = "^3.10"
logger = { git = "https://github.com/obervinov/logger-package.git", tag = "v1.0.6" }

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

poetry install
```

## <img src="https://github.com/obervinov/_templates/blob/main/icons/config.png" width="25" title="usage"> Usage example
### Environment variables
| Name  | Description | Default value |
| ------------------------ | ------------------------------------------------ | --------------------------------------------------------------------- |
| `LOGGER_FORMAT` | A string with the event logging format | `[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s` |
| `LOGGER_LEVEL` | Event logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL or NOT SET | `INFO` |
| `LOGGER_DATE_FORMAT` | Date format in logging event output | `%d/%b/%Y %H:%M:%S` |

### Examples
#### Simple
```python
# Import module
from logger import log

# Examples
# error message
log.error(f"this error: {error}")

# warning message
log.warning(f"this warning: {warn}")

# info message
log.info(f"this info: {info}")
```

#### With using class
```python
from logger import log

class myproject:
  def __init__(self):
    self.log = create_logger(__name__, self.__class__.__name__)
    self.log.info("Init my class")

  def warning(self):
    self.log.warning("Warning")

  def error(self):
    self.log.error("Critical error")

  def debug(self):
    self.log.debug("Debug")

mp = myproject()
mp.warning()
mp.error()
mp.debug()
```
<img src="doc/example.png" width="200" title="example">