#!/bin/bash

MAX_RETRIES=60
I=0

while [[ $I < $MAX_RETRIES ]] ; do
    echo "Trying to connect to the database...attempt $I of $MAX_RETRIES"
    if python manage.py migrate --noinput ; then
        echo "Applying fixtures..."
        python manage.py loaddata equipments
        python manage.py loaddata stopping_reasons

        echo "Running server..."
        python manage.py runserver 0.0.0.0:8000
        break
    fi

    I=$((I + 1))
    sleep 1
done
