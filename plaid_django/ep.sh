service nginx restart
python manage.py migrate
supervisord -n -c supervisor.conf
