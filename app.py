from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignupForm, LoginForm
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TSTACK'

cnx = mysql.connector.connect(user='root',
                            password = '1234554321',
                            host = 'localhost',
                            database = 'link')

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    return render_template('contact.html')

@app.route("/search", methods=['POST', 'GET'])
def search():
    return render_template('search.html')

@app.route('/loginbutton', methods=['POST', 'GET'])
def loginbutton():
    return render_template('log-in.html')

@app.route('/signinbutton', methods=['POST', 'GET'])
def signinbutton():
    return render_template('sign-up-form.html')

@app.route("/profile", methods=['POST', 'GET'])
def profile(): 
    return render_template('profile-view.html')

@app.route("/profile1", methods=['POST', 'GET'])
def profile1(): 
    return render_template('profile-view1.html')

@app.route("/profile2", methods=['POST', 'GET'])
def profile2(): 
    return render_template('profile-view2.html')

@app.route("/profile3", methods=['POST', 'GET'])
def profile3(): 
    return render_template('profile-view3.html')

@app.route("/profile4", methods=['POST', 'GET'])
def profile4(): 
    return render_template('profile-view4.html')

@app.route("/profile5", methods=['POST', 'GET'])
def profile5(): 
    return render_template('profile-view5.html')

@app.route("/profile6", methods=['POST', 'GET'])
def profile6(): 
    return render_template('profile-view6.html')

@app.route("/profile7", methods=['POST', 'GET'])
def profile7(): 
    return render_template('profile-view7.html')

@app.route("/profile8", methods=['POST','GET'])
def profile8():
    return render_template('profile-view8.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    msg = ''
    form = LoginForm()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM link.tstack WHERE email=%s AND password=%s',(email,password))
        record = cursor.fetchall()
        if record:
            session['email'] = email
            session['password'] = password
            return redirect('/edit')
        else:
            msg = 'No account found, please try again...'
    return render_template('log-in.html', msg = msg, form=form)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        phonenum = request.form['phonenum']
        cursor = cnx.cursor()
        cursor.execute('INSERT INTO link.tstack (firstname, lastname, email, password, phonenum) VALUES (%s,%s,%s,%s,%s)',(firstname,lastname,email,password,phonenum))
        cnx.commit()
        cursor.close()
        return redirect('login')
    return render_template('/sign-up-form.html', form=form)

@app.route("/edit", methods=['POST','GET'])
def edit():
    if 'email' in session:
        email = session['email']
        firstname = session.get('firstname')
        lastname = session.get('lastname')
        phonenum = session.get('phonenum')
        cursor = cnx.cursor()
        query = 'SELECT * FROM tstack WHERE email = %s'
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            firstname = user[0]
            lastname = user[1]
            phonenum = user[4]
            return render_template('index.html',firstname=firstname, lastname=lastname, phonenum=phonenum, email=email)
        else:
            return redirect('/')
    else:
        return redirect('/')

app.run(host='localhost', port=5000, debug=True)