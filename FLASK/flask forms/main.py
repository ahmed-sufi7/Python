from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        with open ("file.txt","w") as f:
            f.write(f"The name is {request.form['Name']} and email is {request.form['Email']}")
            return render_template("contact.html")
        
    else:
        return render_template("contact.html")
        


app.run(debug=True)