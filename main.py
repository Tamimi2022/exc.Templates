from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/")
def index(title='index'):
    return render_template('index.html')

@app.route("/home")
def home():
    return redirect(url_for('index'))

@app.route("/about")
def about(title='about'):
    return render_template('about.html')

@app.route("/form")
def form(title='form'):
    return render_template('form.html')

if __name__ == '__main__':
    app.run()