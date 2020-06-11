# HackerNews
<h>Start with instalation</h>

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
<p>Run Django project: $gunicorn hackernews.wsgi</p>