# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).


## v2.0.6 - 2026-09-18
### What's Changed
#### 📚 Documentation
* `README.md`: correct the documented `LOGGER_FORMAT` default (`%(logger_name)s`, not `%(name)s.`), fix the class example — it called `create_logger()`, which is not exported from the package and takes one argument, not two — and point the install snippet at this release. Also fixes the unbalanced quote that made the pasted `pyproject.toml` invalid.
* `README.md`: replace the hand-maintained GitHub Actions Templates table with a badge that reads the pinned version out of `.github/workflows/pr.yaml` — the table went stale on every template bump because nothing kept it in sync.


## v2.0.5 - 2026-09-17
### What's Changed
#### 🐛 Bug Fixes
* `.github/workflows`: move the reusable workflows to `obervinov/_templates@v4.0.0`. Node 20 is removed from the Actions runner on 2026-09-23, and the pinned templates still called `actions/create-release` (`runs.using: node12`, archived) along with a set of `node20` actions — releases and checks in this repository would stop running.


## v2.0.4 - 2025-12-23
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v2.0.3...v2.0.4 by @obervinov https://github.com/obervinov/logger-package/pull/40
#### 🚀 Features
* upgrade dev dependencies to latest versions


## v2.0.3 - 2025-12-23
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v2.0.2...v2.0.3 by @obervinov https://github.com/obervinov/logger-package/pull/39
#### 🚀 Features
* upgrade dependencies to latest versions
* fix codeql recommendations


## v2.0.2 - 2025-07-10
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v2.0.1...v2.0.2 by @obervinov https://github.com/obervinov/logger-package/pull/28
#### 🚀 Features
* bump dependencies to latest versions
* bump workflows to `v2.1.1`


## v2.0.1 - 2024-12-17
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v2.0.0...v2.0.1 by @obervinov https://github.com/obervinov/logger-package/pull/22
#### 🚀 Features
* bump dependencies
* bump workflow to `v2.0.2`


## v2.0.0 - 2024-10-11
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v1.0.6...v2.0.0 by @obervinov https://github.com/obervinov/logger-package/pull/19
#### 🚀 Features
* bump python version to `3.12`
* bump workflow to `v2.0.0`


## v1.0.6 - 2024-02-07
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v1.0.5...v1.0.6 by @obervinov https://github.com/obervinov/logger-package/pull/18
#### 🐛 Bug Fixes
* [Duplicate entries in messages](https://github.com/obervinov/logger-package/issues/16)
#### 📚 Documentation
* [Corrections to README.md](https://github.com/obervinov/logger-package/issues/15)
 

## v1.0.5 - 2024-02-02
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v1.0.4...v1.0.5 by @obervinov https://github.com/obervinov/logger-package/pull/14
#### 🐛 Bug Fixes
* fix the supported versions of python `"^3.9 || ^3.10 || ^3.11"`


## v1.0.4 - 2024-01-24
### What's Changed
**full changelog**: https://github.com/obervinov/logger-package/compare/v1.0.3...v1.0.4 by @obervinov https://github.com/obervinov/logger-package/pull/13
#### 🐛 Bug Fixes
* removed `logging = "^0.4.9.6"` for fix `ImportError: cannot import name 'log' from 'logger'`
* added imports in `__init__.py` for fix `ImportError: cannot import name 'log' from 'logger'`


## v1.0.3 - 2024-01-22
### What's Changed
**Full Changelog**: https://github.com/obervinov/logger-package/compare/v1.0.2...v1.0.3 by @obervinov in https://github.com/obervinov/logger-package/pull/12
#### 🐛 Bug Fixes
* rename workflow file extensions


## v1.0.2 - 2024-01-22
### What's Changed
**Full Changelog**: https://github.com/obervinov/logger-package/compare/v1.0.1...v1.0.2 by @obervinov in https://github.com/obervinov/logger-package/pull/11
#### 🐛 Bug Fixes
* [Rename the directory with the src module to the package name](https://github.com/obervinov/logger-package/issues/7)
* [Dependency graph does not work correctly, sort it out and fix it network/dependencies](https://github.com/obervinov/logger-package/issues/4)
#### 📚 Documentation
* [Fix badge with tests in README.md](https://github.com/obervinov/logger-package/issues/10)
* [Fix typos in README.md](https://github.com/obervinov/logger-package/issues/3)
* [Update PR template](https://github.com/obervinov/logger-package/issues/8)
* [Format function headers in comments](https://github.com/obervinov/logger-package/issues/6)
* [Dependency graph does not work correctly, sort it out and fix it network/dependencies](https://github.com/obervinov/logger-package/issues/4)
#### 💥 Breaking Changes
* [Migration from pip to poetry](https://github.com/obervinov/logger-package/issues/2)
#### 🚀 Features
* [Migration from pip to poetry](https://github.com/obervinov/logger-package/issues/2)
* [Define a constant instead of duplicating this literal '[class.%s]](https://github.com/obervinov/logger-package/issues/9)


## v1.0.1 - 2023-03-03
### What's Changed
**Full Changelog**: https://github.com/obervinov/logger-package/compare/v1.0.0...v1.0.1 by @obervinov in https://github.com/obervinov/logger-package/pull/1
#### 🐛 Bug Fixes
* updated the code in accordance with the recommendations of **flake8** and **pylint**
* adjusted [pyproject.toml](https://github.com/obervinov/logger-package/blob/main/pyproject.toml) and [setup.py](https://github.com/obervinov/logger-package/blob/main/setup.py) for package delivery
#### 📚 Documentation
* updated and expanded the documentation in the file [README.md](https://github.com/obervinov/logger-package/blob/main/README.md)
#### 💥 Breaking Changes
* global **code recycling**: _removed old artifacts_ and _more comments added to the code_
#### 🚀 Features
* added support for loading the **logger settings from a environment variable**
* added github actions: **flake8**, **pylint** and **create release**
* added [SECURITY](https://github.com/obervinov/logger-package/blob/main/SECURITY.md)
* added [ISSUE_TEMPLATE](https://github.com/obervinov/logger-package/tree/main/.github/ISSUE_TEMPLATE)
* added [PULL_REQUEST_TEMPLATE](https://github.com/obervinov/logger-package/tree/main/.github/PULL_REQUEST_TEMPLATE)
* added [CODEOWNERS](https://github.com/obervinov/logger-package/tree/main/.github/CODEOWNERS)
* added [dependabot.yml](https://github.com/obervinov/logger-package/tree/main/.github/dependabot.yml)


## v1.0.0 - 2022-11-05
### What's Changed
**Full Changelog**: https://github.com/obervinov/logger-package/commits/v1.0.0
#### 💥 Breaking Changes
* Module release
