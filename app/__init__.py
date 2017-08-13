from flask import Flask, request, url_for, render_template, flash, redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)

from views import main, email_prod_change



