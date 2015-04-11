import flask
#create instance
app = flask.Flask(__name__)

#route, if asking for the route, return the function
messagez = ""

@app.route("/")
def index():
	html = """
	<a href='%s'>Home</a><br>
	<a href='%s'>About</a><br>
	<a href='%s'>Contact</a><br><br><br>Hello Everyone, Welcome to Python Code Camp!
	""" % (flask.url_for("index"), flask.url_for("about"), flask.url_for("contact"))
	return html


@app.route("/about")
def about():
	global messagez
	print messagez
	html= """<a href='%s'>Home</a><br>
	<a href='%s'>About</a><br>
	<a href='%s'>Contact</a><br><br><br>
	Just a simple project created for the sake of the prize!
	""" % (flask.url_for("index"), flask.url_for("about"), flask.url_for("contact"))
	return html
	
@app.route("/contact", methods=["GET", "POST"])
def contact():
	html = """
	<a href='%s'>Home</a><br>
	<a href='%s'>About</a><br>
	<a href='%s'>Contact</a><br><br><br>
	Name : Christian Edensor Arbon<br>
	Email: cearbon@netsuite.com<br>
	Message: Ping me if you need help with regards to NetSuite<br>
	""" % (flask.url_for("index"), flask.url_for("about"), flask.url_for("contact"))
	name = flask.request.form.get('name')
	message = flask.request.form.get('message')
	email = flask.request.form.get('email')
	if name is not None and message is not None and email is not None:
		global messagez
		print messagez
		messagex = messagez
		messagey = str(messagex) 
		namex = str(name)
		messagea = str(message)
		messagey = messagey + "<br>- " + namex + " : " + messagea
		messagez = messagey
	return flask.render_template('hello.html', name=name, email=email, message=message)

@app.route("/msg")
def msg():
	return messagez

	#return html

	
if __name__=="__main__":
	global messagez
	messagez = "<h1>Messages</h1>"
	print messagez
	app.debug = True
	app.run(port=8888)