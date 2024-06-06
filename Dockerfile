ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --deploy --system
COPY . /code

ENV SECRET_KEY "yUmJW4nXzm3ecLpS4S7Dc7jPaje16aWMrOo1UxMJGcLsbkC00o"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "eventex.wsgi"]
