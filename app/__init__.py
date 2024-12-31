from flask import Flask
from flask_login import LoginManager
from config import Config, db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from app.controllers.auth_controller import dashboard, login, register, logout
    from app.controllers.training_controller import training
    from app.controllers.admin_controller import admin, add_word, edit_word, delete_word

    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    app.add_url_rule('/dashboard', 'dashboard', dashboard)
    app.add_url_rule('/register', 'register',
                     register, methods=['GET', 'POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/training', 'training', training)
    app.add_url_rule('/admin', 'admin', admin)
    app.add_url_rule('/admin/add_word', 'add_word',
                     add_word, methods=['GET', 'POST'])
    app.add_url_rule('/admin/edit_word/<word_id>', 'edit_word',
                     edit_word, methods=['GET', 'POST'])
    app.add_url_rule('/admin/delete_word/<word_id>',
                     'delete_word', delete_word, methods=['POST'])

    return app
