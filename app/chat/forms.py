from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, validators



class LoginForm(Form):
    email = StringField(u'Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField(u'Пароль', [validators.DataRequired()])
    remember_me = BooleanField(u'Запомнить меня')


class RegistrationForm(Form):
    username = StringField(u'Username', [validators.Length(min=3, max=40)])
    email = StringField(u'Email', [validators.DataRequired(), validators.Email()])
    password= PasswordField(u'Пароль', [
        validators.DataRequired(),
        validators.EqualTo('repeat_password', message=u'Пароли должны совпадать')
    ])
    repeat_password= PasswordField(u'Повторите пароль', [validators.DataRequired()])
    description = TextAreaField(u'Информация')


class UserCard(Form):
    pass