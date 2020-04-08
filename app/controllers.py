from app import app, db, bcrypt
from flask import render_template, json, request, url_for, redirect, flash
from app.models import User, Ricetta


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html', title='Register')
    elif request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # validate the received values
        if username and email and password and confirm_password:
            if password != confirm_password:
                flash('Le password non coincidono', 'danger')
                return redirect(url_for('register'))
            else:
                hashed_password = bcrypt.generate_password_hash(password).decode(
                    'utf-8')  # questo comando trasforma la password inserita in hash string
                # qeusto comando trasmette la password hashed (criptata)
                user = User(username=username,
                            email=email, password_hash=hashed_password)
                # dopo aver creato l'utente facciamo il commit nel db
                db.session.add(user)
                db.session.commit()
                flash(
                    'Your account has been created! You are now able to log in', 'success')
                # dopo la registrazione dirige l'utente alla login page
                return redirect(url_for('showSignUp'))
        else:
            flash('Mancano campi obbligatori', 'danger')
            return redirect(url_for('register'))
