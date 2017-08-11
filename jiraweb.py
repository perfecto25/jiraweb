#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, url_for, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from app.config import PORT 

app = Flask(__name__)
app.config.from_object('app.config')

Bootstrap(app)

from app.views import *

app.run(host='0.0.0.0', port=PORT, debug=True)