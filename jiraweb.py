#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.config import PORT


from app import app

app.run(host='0.0.0.0', port=PORT, debug=True)