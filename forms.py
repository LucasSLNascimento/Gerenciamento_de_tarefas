from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    task_name = StringField('Nome da tarefa', validators=[DataRequired()])
    description = TextAreaField('Descrição', validators=[DataRequired()])
    status = SelectField('status', choices=[
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluída', 'Concluída')
    ], validators=[DataRequired()])
    assigned_user = SelectField('Responsável pela tarefa', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Criar tarefa')

