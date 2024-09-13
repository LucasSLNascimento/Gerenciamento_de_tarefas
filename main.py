from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from config import app
from forms import TaskForm
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
    users = User.query.all()
    tasks = Task.query.all()
    return render_template('dashboard.html', tasks=tasks, users=users, user=current_user)

@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def user_tasks():
    from models import User, Task
    from forms import TaskForm

    users = User.query.all()
    form = TaskForm()

    form.assigned_user.choices = [(user.id, user.username) for user in users]

    # Filtrar tarefas pelo status (caso o usuário selecione um filtro)
    status_filter = request.args.get('status_filter')

    # Query base para filtrar as tarefas do usuário logado
    query = Task.query.filter_by(user_id=current_user.id)

    if status_filter:  # Se houver um filtro de status, aplique-o à query
        query = query.filter_by(status=status_filter)

    tasks = query.all()

    if form.validate_on_submit():  # Tratamento de criação de nova tarefa
        task = Task(
            task_name=form.task_name.data,
            description=form.description.data,
            status=form.status.data,
            assigned_user_id=form.assigned_user.data,
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('user_tasks'))

    return render_template('tasks.html', tasks=tasks, form=form, users=users)


@app.route('/create_task', methods=['POST'])
@login_required
def create_task():
    task_name = request.form.get('task_name')
    description = request.form.get('description')
    status = request.form.get('status')
    assigned_user_id = request.form.get('assigned_user')

    if task_name and description and assigned_user_id:
        new_task = Task(
            task_name=task_name,
            description=description,
            status=status,
            user_id=assigned_user_id  # O responsável pela tarefa é o usuário selecionado
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('user_tasks'))

    users = User.query.all()
    return render_template('create_task.html', users=users)

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    form = TaskForm(obj=task)
    form.assigned_user.choices = [(user.id, user.username) for user in User.query.all()]

    if form.validate_on_submit():
        task.task_name = form.task_name.data
        task.description = form.description.data
        task.status = form.status.data
        task.user_id = form.assigned_user.data

        db.session.commit()
        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('edit_task.html', form=form, task=task)


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()
    flash('Tarefa excluída com sucesso!', 'success')
    return redirect(url_for('dashboard'))



if __name__ == '__main__':
    app.run(debug=True)
