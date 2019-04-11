"""Diactoros action processor."""

from octomachinery.app.action.runner import run as process_action

from . import __main__  # noqa: F401; pylint: disable=unused-import


# pylint: disable=expression-not-assigned
__name__ == '__main__' and process_action()
