from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
app2= Flask(__name__)
# app = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/login'
db = SQLAlchemy(app2)

class signing(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20), unique=False,  nullable=False)
    Email = db.Column(db.String(8), unique=False, nullable=False)
    Password = db.Column(db.String(8), unique=False, nullable=False)
    ConPassword = db.Column(db.String(8), unique=False, nullable=False)
    AADHARNUM = db.Column(db.String(8), unique=False, nullable=False)
    
    
    
@app2.route("/sign", methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        fullname = request.form.get('Fullname')
        Email = request.form.get('Email')
        Password = request.form.get('Password')
        ConPassword = request.form.get('ConPassword')
        AADHARNUM = request.form.get('AADHARNUM')
        
        
        entry = signing(fullname=fullname,Email=Email, Password=Password,ConPassword= ConPassword,AADHARNUM=AADHARNUM)
        db.session.add(entry)
        db.session.commit()

    return render_template('signup.html')

app2.run(debug=True)
