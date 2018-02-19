from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'shove'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'f5fe0995ccf9fa'
app.config['MAIL_PASSWORD'] = 'f65ea7fa2dae12'
mail = Mail(app)
from app import views