from flask import Flask, render_template, request
# from flask import render_template

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1><i>Hello from Flask</i></h1>"

@app.route("/yourname/<name>")
def you(name):
    return f"<h1>Hello {name}</h1>"

@app.route("/yourname/istvan")
def you2():
    return f"<h1>I am here</h1>"

@app.route("/badpage")
def bp():
    return render_template("badpage.html")

@app.route("/myname/<name>/<greeting>")
def me(name, greeting):
    x = 2 + 2
    return f"<h1>{greeting} {name}</h1>"

@app.route("/mypage")
def mypage():
    return render_template("me.html")

@app.route("/ourpage/<myname>/<myaction>")
def ourpage(myname, myaction):
    return render_template("myargs.html", name=myname, something=myaction)

@app.route("/ohno")
def ohno():
    print("Wooops")
    
@app.route("/getname")
def getname():
    # return render_template("myform.html",myname="")
    return render_template("myform.html")

@app.route("/processform", methods=["POST"])
def processform():
    # username=request.args.get("username")
    username = request.form["username"]
    return render_template("myform.html",myname=username)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")