from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
)
from .forms import LoginForm, RegistrationForm
from .models import User, Messages
module = Blueprint('chat', __name__, url_prefix='/')


@module.route('/')
@module.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    return "index.html"


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
    




def sign_in_user(user_form):
    form = user_form
    try:            
        user = User.query.filter_by(email = form.email).first()
        if user:
            hashpass = User.password_to_hash(form.password)
            if hashpass == user.password_hash:
                flash('Аутентификация успешна. Добро пожаловать {}, мы без вас скучали.'.format(user.username))
                return redirect('/')
            else:
                flash('Пароль неверен')
        else:
            flash('Email не зарегестрирован')
    except:
        flash('Произошло что то странное со стороны сервера.')

