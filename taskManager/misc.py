import os

def store_uploaded_file(title, f):
	d = '%s/static/taskManager/uploads' % (os.path.dirname(os.path.realpath(__file__)))
	if not os.path.exists(d):
		os.makedirs(d)

	# A1: Injection (shell)
	# Let's avoid the file corruption race condition!
	os.system ("mv " + f.temporary_file_path() + " " + "%s/static/taskManager/uploads/%s" % (os.path.dirname(os.path.realpath(__file__)), title))

	#with open('%s/static/taskManager/uploads/%s' % (os.path.dirname(os.path.realpath(__file__)), title), 'wb+') as destination:
	#	for chunk in f.chunks():
	#		destination.write(chunk)
	return '/static/taskManager/uploads/%s' % (title)