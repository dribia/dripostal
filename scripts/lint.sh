#!/usr/bin/env bash

set -e
set -x

poetry run mypy dripostal
poetry run flake8 dripostal tests
poetry run black dripostal tests --check
poetry run isort dripostal tests --check-only
poetry run pydocstyle dripostal
