FROM python:3.10.10-alpine3.17

ENV FLASK_JWT_SECRET_KEY="ShVmYq3t6w9z$C&F)J@NcQfTjWnZr4u7"
ENV POETRY_VERSION=1.4.0 \
    PIP_NO_CACHE_DIR=off

RUN pip install "poetry==${POETRY_VERSION}"

COPY . /code/
WORKDIR /code

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

CMD flask run --host=0.0.0.0