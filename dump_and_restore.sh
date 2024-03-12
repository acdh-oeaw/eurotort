#!/bin/bash

pg_dump -d eurotort -h localhost -p 5433 -U  eurotort -c -f eurotort_dump.sql
# psql -U postgres -d eurotort < eurotort_dump.sql
