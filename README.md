# HackerNews
<h>Start with instalation</h>

<p>Update system: $ sudo apt update</p>
<p>Install necessary packages: $sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl</p>
<p>Log in to the Postgres interactive session: $ sudo -u postgres psql</p>
<p>Create PostgreSQL database: postgres=# CREATE DATABASE 'DATABASE_NAME';</p>
<p>Then create a database for project: postgres=# CREATE USER 'DATABASE_USER' WITH PASSWORD 'DATABASE_PASSWORD';</p>
<p>Now we will give the created user access to administer the new database:  postgres=# GRANT ALL PRIVILEGES ON DATABASE 'DATABASE_NAME' TO 'DATABASE_USER';</p>
<p>End PostgreSQL session: postgres=# \q</p>
<p>Install requirements: $pip install -r requirements.txt</p>
<p>Install virtual environment: $pip $python3 -m venv env</p>
<p>Activate virtual environment: $source env/bin/activated</p>
<p>Export environment variables:</p>
<ol>
<li>$export SECRET_KEY='DJANGO_SECRET_KEY'</li>
<li>export MAIN_HOST='DJANGO_HOST>
<li>export DATABASE_PORT='PORT'</li>
<li>export DATABASE_HOST='DATABASE_HOST'</li>
<li>export DATABASE_PASSWORD='DATABASE_PASSWORD'</li>
<li>export DATABASE_USER='DATABASE_USER'</li>
<li>export DATABASE_NAME='DATABASE_NAME'</li>
</ol>
<p>Run Django project: $gunicorn --bind 0.0.0.0:8000 hackernews.wsgi
</p>

<p>Postman collation:</p>

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4952de9105f2c22389e1#?env%5BHackerNews%5D=W3sia2V5IjoidXJsIiwidmFsdWUiOiJodHRwOi8vMTI3LjAuMC4xOjgwMDAvIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJ0b2tlbiIsInZhbHVlIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SnBaQ0k2TWl3aVpYaHdJam94TlRrM01EWTVNak15ZlEuVGEtbXk3YUxOeXFHdHdrS041S0ZKU1IxS1BRM1VDSVJ5eEp1bktDRExlMCIsImVuYWJsZWQiOnRydWV9XQ==)