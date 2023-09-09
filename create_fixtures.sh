#!/usr/bin/env bash
# create_fixtures.sh

# make sure you ran `pip install django-fixture-magic` and added `'fixture_magic'` to INSTALLED_APPS
source env/bin/activate
source set_env_variables.sh
mkdir ./archiv/fixtures
touch ./archiv/fixtures/dump.json
echo "create fixtures_courtdecission"
python manage.py dump_object archiv.courtdecission 4  100 > ./archiv/fixtures/dump.json

echo "done"