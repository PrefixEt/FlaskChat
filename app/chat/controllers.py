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
    try:            
        user = User.query.filter_by(email = form.email).first()
        if user:
            flash(u'Email занят, выбирите другой(пожалуйста)')          
        else:






def sign_in_user(user_form):
    form = user_form
    try:            
        user = User.query.filter_by(email = form.email).first()
        if user:            
            if user.valid_pass(form.password):
                flash(u'Аутентификация успешна. Добро пожаловать {}, мы без вас скучали.'.format(user.username))
                return redirect('/')
            else:
                flash(u'Пароль неверен')
        else:
            flash(u'Email не зарегестрирован')
    except:
        flash(u'Произошло что то странное со стороны сервера.')

