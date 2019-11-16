from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import math
from datetime import datetime

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)




# -----------------------------HOME PAGE--------------------------------------
@app.route("/")
def home():
    return render_template('index.html', params=params)




# -----------------------------DONOR PAGE--------------------------------------
class Donor(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    bloodgroup = db.Column(db.String(10), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/donor", methods = ['GET', 'POST'])
def donor():
    if (request.method == 'POST'):
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        bloodgroup = request.form.get('bloodgroup')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        entry = Donor(name=name, gender=gender, age=age, bloodgroup=bloodgroup, phone_num=phone, email=email, address=address, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        flash("Submit Successfully. Thank You for participating in this Donor Lists. Hope, Your contribution will definitely contribute to the wellbeing of patients.", "success")
        return redirect(request.url)

    donors = Donor.query.filter_by().all()
    last = math.ceil(len(donors) / int(params['no_of_posts']))
    return render_template('donor.html', params=params, donors=donors)


@app.route("/donoredit/<string:sno>", methods = ['GET', 'POST'])
def donoredit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_name = request.form.get('name')
            gender = request.form.get('gender')
            age = request.form.get('age')
            bloodgroup = request.form.get('bloodgroup')
            phone = request.form.get('phone')
            email = request.form.get('email')
            address = request.form.get('address')
            date = datetime.now()

            if sno=='0':
                donor = Donor(name=box_name, gender=gender, age=age, bloodgroup=bloodgroup, phone_num=phone, email=email, address=address, date=datetime.now())
                db.session.add(donor)
                db.session.commit()
            else:
                donor = Donor.query.filter_by(sno=sno).first()
                donor.name = box_name
                donor.gender = gender
                donor.age = age
                donor.bloodgroup = bloodgroup
                donor.phone_num = phone
                donor.email = email
                donor.address = address
                donor.date = date
                db.session.commit()
                # return redirect('/donoredit/'+sno)
                flash("Donor's Detail Edited Successfully.", "success")
                return redirect('/dashboard')

        donor = Donor.query.filter_by(sno=sno).first()
        return render_template('donoredit.html', params=params, donor=donor)


@app.route("/donordelete/<string:sno>", methods = ['GET', 'POST'])
def donordelete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        donors = Donor.query.filter_by(sno=sno).first()
        db.session.delete(donors)
        db.session.commit()
        flash("Donor's Details Deleted Successfully", "success")
        return redirect('/dashboard')




# -----------------------------RECIPIENT PAGE--------------------------------------
class Recipient(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    bloodgroup = db.Column(db.String(10), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/recipient", methods=['GET', 'POST'])
def recipient():
    if (request.method == 'POST'):
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        bloodgroup = request.form.get('bloodgroup')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        entry = Recipient(name=name, gender=gender, age=age, bloodgroup=bloodgroup, phone_num=phone, email=email,
                          address=address, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        flash(
            "Submit Successfully. Thank You for participating in this Recipient Lists. Hope, You will get your blood very soon.",
            "success")
        return redirect(request.url)

    recipients = Recipient.query.filter_by().all()
    last = math.ceil(len(recipients) / int(params['no_of_posts']))
    return render_template('recipient.html', params=params, recipients=recipients)


@app.route("/recipientedit/<string:sno>", methods=['GET', 'POST'])
def recipientedit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_name = request.form.get('name')
            gender = request.form.get('gender')
            age = request.form.get('age')
            bloodgroup = request.form.get('bloodgroup')
            phone = request.form.get('phone')
            email = request.form.get('email')
            address = request.form.get('address')
            date = datetime.now()

            if sno == '0':
                recipient = Recipient(name=box_name, gender=gender, age=age, bloodgroup=bloodgroup, phone_num=phone,
                                      email=email, address=address, date=datetime.now())
                db.session.add(recipient)
                db.session.commit()
            else:
                recipient = Recipient.query.filter_by(sno=sno).first()
                recipient.name = box_name
                recipient.gender = gender
                recipient.age = age
                recipient.bloodgroup = bloodgroup
                recipient.phone_num = phone
                recipient.email = email
                recipient.address = address
                recipient.date = date
                db.session.commit()
                # return redirect('/recipientedit/'+sno)
                flash("Recipient's Detail Edited Successfully.", "success")
                return redirect('/dashboard')

        recipient = Recipient.query.filter_by(sno=sno).first()
        return render_template('recipientedit.html', params=params, recipient=recipient)


@app.route("/recipientdelete/<string:sno>", methods=['GET', 'POST'])
def recipientdelete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        recipients = Recipient.query.filter_by(sno=sno).first()
        db.session.delete(recipients)
        db.session.commit()
        flash("Recipient's Detail Deleted Successfully", "success")
        return redirect('/dashboard')




# -----------------------------ABOUT PAGE--------------------------------------
@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html', params=params)




# -----------------------------CONTACT PAGE--------------------------------------
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [params['gmail-user']],
                          body = message + "\n" + phone
                          )
        flash("Submited Successfully, Thank You for the Feedback.", "success")
        return redirect(request.url)

    return render_template('contact.html', params=params)




# -----------------------------ADMIN CONTROL PAGE--------------------------------------
@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        contacts = Contacts.query.filter_by().all()
        donors = Donor.query.filter_by().all()
        recipients = Recipient.query.filter_by().all()
        return render_template('dashboard.html',params=params, donors=donors, recipients=recipients, contacts=contacts)

    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            # set the session variable
            contacts = Contacts.query.filter_by().all()
            session['user'] = username
            donors = Donor.query.filter_by().all()
            recipients = Recipient.query.filter_by().all()
            return render_template('dashboard.html', params=params, donors=donors, recipients=recipients, contacts=contacts)
        else:
            flash("** Incorrect UserID or Password.", "danger")
            return redirect(request.url)

    return render_template('/login.html', params=params)


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/')




app.run(host='0.0.0.0', port=5000, debug=True)