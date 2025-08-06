from flask import Flask,render_template
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = '29_ece'
mysql = MySQL(app)

@app.route("/",methods=["GET"])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM people")
    results = cur.fetchall()
    cur.close()
    return render_template("index.html",results=results)

@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/blog",methods=["GET"])
def blog():
    return render_template("blog.html")

@app.route("/contact",methods=["GET"])
def contact():
    return render_template("contact.html")

if __name__ == 'main':
    app.run()



