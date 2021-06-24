import cgi

form = cgi.FieldStorage()

image = form.getvalue('filename')


