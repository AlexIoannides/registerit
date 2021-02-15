<div align="center">
<img src="https://dev-project-media.s3.eu-west-2.amazonaws.com/registerit-logo.png"/>
</div>

<div align="center">
<img src="https://img.shields.io/pypi/pyversions/registerit"/>
<img src="https://img.shields.io/pypi/v/registerit.svg?label=PyPI&logo=PyPI&logoColor=white&color=success"/>
</div>

---

## Register Package Names on PyPI

* Have an idea for a Python package?
* Thought of a great name?
* Register it on PyPI, before someone else does!

A tool that creates a minimal Python package with your chosen name and uploads it to PyPI, registering it for you.

## Install

```shell
$ pip install registerit
```

## Run

If you don't care about assigning your name and contact details to the package, then use

```shell
$ registerit MY_COOL_PKG --username PYPI_USERNAME --password PYPI_PASSWORD
```

If you do, then

```shell
$ registerit MY_COOL_PKG \
    --username PYPI_USERNAME \
    --password PYPI_PASSWORD \
    --author Me \
    --email me@me.com \
    --url www.me.com
```
