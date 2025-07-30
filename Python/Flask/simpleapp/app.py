from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/you")
def hello_you():
    return render_template("you.html")

@app.route("/myname/<name>")
def hello(name):
    return render_template("myname.html", name=name)

@app.route("/doit", methods=['POST'])
def doit():
    data = request.get_json()
    return f"Hello  {data['name']}"

# NOT TO BE DONE IN PRODUCTION
if __name__ == "__main__":
    # This would be replaced with something like gunicorn and NGINX
    # app.run()
    # app.run(host=0.0.0.0) # Run on any network interface, not just localhost
    # app.run(port=8080) # Change the port number
    app.run(debug=True) # Run in debug mode, see more output and allow save to update
    # We can combine options
    # app.run(host=0.0.0.0, port=8080, debug=True)