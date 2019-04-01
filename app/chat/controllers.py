from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
)
from flask_login import current_user, login_user
from .forms import LoginForm, RegistrationForm
from .models import User, Messages
module = Blueprint('chat', __name__, url_prefix='/')


@module.route('/')
@module.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    return redirect('sign_in')


@module.route('/sign_in', methods=['GET','POST'])
def sign_in():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        sign_in_user(form)
    
    return render_template('chat/sign_in.html', form=form)



@module.route('/sign_up',  methods=['GET','POST'])
def sign_up():
    form=RegistrationForm(request.form)
    if form.validate_on_submit():                
        print(dict(request.form))
    return render_template('chat/sign_up.html', form=form)





def registration_user(user_form):
    form = user_form
    try:            
        user = User.query.filter_by(email = form.email).first()
        if user:
            flash(u'Email занят, выбирите другой(пожалуйста)')          
        else:
            registration_user=User(
                email=form.email,
                username=form.username,
                password_hash=form.password,
                description=form.description
                )
            registration_user.commit()
    except:
        pass

def sign_in_user(user_form):
    form = user_form
    try:            
        user = User.query.filter_by(email = form.email).first()
        if user:            
            if user.valid_pass(form.password):
                flash(u'Аутентификация успешна. Добро пожаловать {}, мы без вас скучали.'.format(user.username), 'Успеъх')
                return redirect('/')
            else:
                flash(u'Пароль неверен', u'ОЙ')
        else:
            flash(u'Email не зарегестрирован', u'Ай')
    except Exception as e:
        flash(u'Произошло что то странное со стороны сервера.', 'Ooops')
        flash(str(e))

