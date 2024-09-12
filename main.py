from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from config import app
from models import *


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    from forms import RegisterForm
    from werkzeug.security import generate_password_hash

    formulario = RegisterForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data
        sen = generate_password_hash(formulario.password.data)

        usu_ex = User.query.filter_by(username=usu).first()

        if usu_ex:
            print('Usuario já existe')
        else:
            novo_usuario = User(username=usu, password=sen)
            db.session.add(novo_usuario)
            db.session.commit()
            print('Usuairo criado')

    return render_template('register.html', form=formulario)


@app.route('/login', methods=['GET', 'POST'])
def login():
    from forms import LoginForm
    from werkzeug.security import check_password_hash

    formulario = LoginForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data
        usuBanco = User.query.filter_by(username=usu).first()

        if usuBanco:
            sen = formulario.password.data
            senhaHash = usuBanco.password

            if check_password_hash(senhaHash, sen):
                login_user(usuBanco)
                return redirect(url_for('dashboard'))

    return render_template('login.html', form=formulario)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.all()
    return render_template('dashboard.html', tasks=tasks)

@app.route('/user_tasks')
@login_required
def user_profile():
    return render_template('profile.html', user=current_user)


if __name__ == '__main__':
    app.run(debug=True)
