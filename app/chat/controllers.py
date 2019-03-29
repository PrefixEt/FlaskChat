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
    if request.method == 'POST' and form.validate():
        print(request.form.get('password'))
    return render_template('chat/sign_in.html', form=form)



@module.route('/sign_up',  methods=['GET','POST'])
def sign_up():
    form=RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
                
        print(dict(request.form))
    return render_template('chat/sign_up.html')





