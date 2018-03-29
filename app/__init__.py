from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'shove66'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '3e7cb90fe86c4a'
app.config['MAIL_PASSWORD'] = 'fad1200db3d863'
mail = Mail(app)
from app import views