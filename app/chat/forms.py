from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, validators, SubmitField 



class LoginForm(FlaskForm):
    email = StringField(u'Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField(u'Пароль', [validators.DataRequired()])
    remember_me = BooleanField(u'Запомнить меня')
    submit = SubmitField(u'Войти')


class RegistrationForm(FlaskForm):
    username = StringField(u'Username', [validators.Length(min=3, max=40)])
    email = StringField(u'Email', [validators.DataRequired(), validators.Email()])
    password= PasswordField(u'Пароль', [
        validators.DataRequired(),
        validators.EqualTo('repeat_password', message=u'Пароли должны совпадать')
    ])
    password_repeat = PasswordField(u'Повторите пароль', [validators.DataRequired()])
    description = TextAreaField(u'Расскажите о себе(Или не рассказывайте)')
    submit = SubmitField(u'Зарегистрироваться')

class UserCard(FlaskForm):
    pass