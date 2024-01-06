#!/usr/bin/env bash

ruff check --select I --fix .
ruff format .