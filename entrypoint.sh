#!/bin/bash

if [[ "$1" == "pytest" ]]; then
  echo "🚨 Running tests..."
  exec pytest "${@:2}"
fi

echo "Collect static..."
python manage.py collectstatic --noinput

echo "📦 Migrations..."
python manage.py migrate --noinput

echo "🚀 Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
