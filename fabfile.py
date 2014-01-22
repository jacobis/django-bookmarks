from fabric.api import local

def runserver():
	"""
	run server
	"""
	local("python manage.py runserver_plus")


def shell():
	"""
	run shell
	"""
	local("python manage.py shell_plus")