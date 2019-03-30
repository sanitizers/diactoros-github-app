"""Diactoros robot runner."""

from octomachinery.app.routing import process_event_actions
from octomachinery.app.routing.decorators import process_webhook_payload
from octomachinery.app.runtime.context import RUNTIME_CONTEXT
from octomachinery.app.server.runner import run as run_app


if __name__ == "__main__":
    run_app(
        name='Diactoros-Bot-by-webknjaz',
        version='1.0.0',
        url='https://github.com/sanitizers/diactoros-github-app',
    )
