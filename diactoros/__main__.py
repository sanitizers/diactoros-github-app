"""Diactoros robot runner."""

from octomachinery.app.routing import process_event_actions
from octomachinery.app.routing.decorators import process_webhook_payload
from octomachinery.app.runtime.context import RUNTIME_CONTEXT
from octomachinery.app.server.runner import run as run_app


@process_event_actions('push')
@process_webhook_payload
async def on_commit_pushed(
        *,
        ref, before,
        head_commit, base_ref,
        commits, repository,
        head=None, sender=None,
        size=None, distinct_size=None,
        installation=None,
        **kwargs,
):
    """Whenever git push happened."""
    github_api = RUNTIME_CONTEXT.app_installation_client

    check_run_name = 'Deployment UI'
    check_runs_base_uri = f'{repository["url"]}/check-runs'

    for commit in commits:
        await github_api.post(
            check_runs_base_uri,
            preview_api_version='antiope',
            data={
                'name': check_run_name,
                'head_branch': ref,
                'head_sha': commit['sha'],
                'status': 'completed',
                'conclusion': 'neutral',
                'started_at': f'{datetime.utcnow().isoformat()}Z',
                'completed_at': f'{datetime.utcnow().isoformat()}Z',
                'output': {
                    'title':
                        f'🔘 Commit Deployment UI for {commit["sha"]}',
                    'summary':
                        'This change can be deployed. Just push a button (above).'
                        '\n\n'
                        '![Deploy it!]('
                        'https://leaks.wanari.com/wp-content/uploads/2016'
                        '/05/deploy-play-framework-app-button.jpg)',
                },
                'actions': [
                    {
                        'label': 'Deploy it!',
                        'description': 'Deploy this commit',
                        'identifier': 'deploy',
                    },
                ],
            },
        )

              
@process_event_actions('check_run', {'requested_action'})
@process_webhook_payload
async def on_deploy_action_button_click(
        *,
        action, check_run, requested_action,
        repository, sender,
        installation,
):
    """Broadcast a deploy event for the commit."""
    requested_action_id = requested_action['identifier']
    if requested_action_id not in {'deploy'}:
        return

    github_api = RUNTIME_CONTEXT.app_installation_client
    deployments_url = repository['deployments_url']
    ref = check_run['head_sha']

    await github_api.post(deployments_url, data={'ref': ref})


if __name__ == "__main__":
    run_app(
        name='Diactoros-Bot-by-webknjaz',
        version='1.0.0',
        url='https://github.com/sanitizers/diactoros-github-app',
    )
