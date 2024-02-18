FROM python:3.12-slim
ENV APP_HOME /home/django/app
WORKDIR $APP_HOME
COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY ./ ./
CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py makemigrations; python manage.py migrate; gunicorn config.wsgi -b 0.0.0.0:8000"]