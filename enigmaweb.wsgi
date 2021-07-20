import sys
sys.path.insert(0, '/var/www/enigmaweb')

activate_this = '/var/www/enigmaweb/.venv/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file.read(), dict(__file__=activate_this))

from app import app as application
