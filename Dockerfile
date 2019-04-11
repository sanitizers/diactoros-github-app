FROM python:3.7-slim

LABEL "maintainer"="Sviatoslav Sydorenko <wk+github-actions@sydorenko.org.ua>"
LABEL "repository"="https://github.com/sanitizers/diactoros-github-app"
LABEL "homepage"="https://github.com/sanitizers/diactoros-github-app"

LABEL "com.github.actions.name" "Diactoros"
LABEL "com.github.actions.description" "Add Deploy buttons to Checks pages for each commit"
LABEL "com.github.actions.icon" "play"
LABEL "com.github.actions.color" "green"

ADD . /usr/src/diactoros
RUN pip install -r /usr/src/diactoros/requirements.txt

ENV PYTHONPATH /usr/src/diactoros

ENTRYPOINT ["python", "-m", "diactoros.action"]
