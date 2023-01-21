FROM acidrain/python-poetry:3.9-alpine-1.3.2

# copy the requirements file into the image
COPY ./poetry.lock /app/poetry.lock
COPY ./pyproject.toml /app/pyproject.toml

WORKDIR /app

RUN poetry config virtualenvs.create false && \
    poetry install

COPY ./src /app/src

CMD ["python", "src/main.py"]
