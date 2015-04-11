import flask
#create instance
app = flask.Flask(__name__)

#route, if asking for the route, return the function
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
	return flask.render_template('hello.html', name=name, email=email, message=message)
	#return html

	
if __name__=="__main__":
	app.debug = True
	app.run(port=8888)