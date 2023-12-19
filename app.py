from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/login'
db = SQLAlchemy(app)

class detail(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False,  nullable=False)
    password = db.Column(db.String(8), unique=False, nullable=False)
    

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
       
        entry = detail(username=username, password=password)
        db.session.add(entry)
        db.session.commit()

    return render_template('login.html')

app.run(debug=True)
