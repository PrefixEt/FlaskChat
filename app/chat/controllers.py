from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
)


module = Blueprint('chat', __name__, url_prefix='/')


@module.route('/')
@module.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    return "index.html"


@module.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if request.method == 'POST':
        pass
    return render_template('chat/sign_in.html')



@module.route('/sign_up',  methods=['GET','POST'])
def sign_up():
    return "<h1>sign_up</h1>"


