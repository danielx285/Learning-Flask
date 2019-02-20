#coding: utf-8
import bd
from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	html = ['<ul>']
	for username, user in bd.users.items():
		html.append(
			"<li><a href='/user/%s'>%s</a></li>" \
			% (username, user["name"])
		)
	html.append("</ul>")
	return "\n".join(html)

def profile(username):
	user = bd.users.get(username)

	if user:
		html_code = "<h1>%s</h1>" % user["name"]  \
			+ "\n<img src='%s' /><br/>" % user["imagen"]  \
			+ "\ntelefone: %s <br/>" % user["tel"] \
			+ "\n<a href='/'>Voltar<a/>"
		return html_code
	else :
		return abort(404, "User not found")

app.add_url_rule('/user/<username>/', view_func=profile, endpoint='user')

@app.route("/about")
def about():
	return "<h1>Esta é uma simples página criada para que eu possa aprender sobre programação Web</h1>"

if __name__ == "__main__":
	app.run(debug=True)
