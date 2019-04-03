from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
    session,
    g
)
from flask_login import current_user, login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from .models import User, Messages
from app.database import db
module = Blueprint('chat', __name__, url_prefix='/')

@module.before_request
def before_request():
    g.user = current_user


@module.route('/')
@module.route('/index.html', methods=['GET', 'POST'])
def index():
    if g.user is not None and g.user.is_authenticated:
        return '<h1>Welcome, {}<h1>'.format(g.user.username)
    return redirect('sign_in')


@module.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if g.user is not None and g.user.is_authenticated:
        return redirect('index.html')
    form = LoginForm(request.form)
    if form.validate_on_submit():
        sign_in_user(form)
    
    return render_template('chat/sign_in.html', form=form)



@module.route('/sign_up',  methods=['GET','POST'])
def sign_up():
    print(request.form)
    form=RegistrationForm(request.form)
    if form.validate_on_submit():
        print('test')
        registration_user(form)
        return redirect('/')
    return render_template('chat/sign_up.html', form=form)



@module.route('/logout')
def logout():
    logout_user()
    return redirect('/sign_in')


def registration_user(user_form):
    form = user_form
    try:            
        user = User.query.filter_by(email = form.email.data).first()

        if user:
            flash(u'Email занят, выбирите другой(пожалуйста)')          
        else:
            registration_user=User(
                email=form.email.data,
                username=form.username.data,
                password_hash=form.password.data,
                description=form.description.data
                )
            db.session.add(registration_user)
            db.session.commit()            
    except Exception as e:
        flash(u'Упс.')
        flash(str(e))
        print(e)
        
        
def sign_in_user(user_form):
    form = user_form
    try:            
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.valid_pass(form.password.data):            
            flash(u'Email не зарегестрирован, или пароль не верен', 'Ай')
        else:
            flash(u'Аутентификация успешна. Добро пожаловать {}, мы без вас скучали.'.format(user.username), 'Успех')
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        
    except Exception as e:
        flash(u'Произошло что то странное со стороны сервера.', 'Ooops')
        flash(str(e))

