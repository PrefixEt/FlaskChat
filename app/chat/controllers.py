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
from app.database import db
module = Blueprint('chat', __name__, url_prefix='/')


@module.route('/')
@module.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    return redirect('sign_in')


@module.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect('index')
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
            return redirect('sign_in')
    except Exception as e:
        flash(u'Упс.')
        flash(str(e))
        
        
    def sign_in_user(user_form):
        form = user_form
        try:            
            user = User.query.filter_by(email=form.email.data).first()
            if not user and not user.check_password(form.password.data):            
                flash(u'Email не зарегестрирован, или пароль не верен', 'Ай')
            else:
                flash(u'Аутентификация успешна. Добро пожаловать {}, мы без вас скучали.'.format(user.username), 'Успех')
                login_user(user, remember=form.remember_me.data)
                return redirect('/')    

            
        except Exception as e:
            flash(u'Произошло что то странное со стороны сервера.', 'Ooops')
            flash(str(e))

