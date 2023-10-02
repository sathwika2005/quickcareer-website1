from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
  return "Home Page"

@app.route("/about")
def about_page():
  return "About Page"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)