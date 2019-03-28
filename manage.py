import os
from flask_script import Manager
from flask import render_template
from app import create_app


app = create_app()
app.config.from_object(os.environ['APP_SETTINGS'])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

manager = Manager(app)

if __name__ == "__main__":
    manager.run()