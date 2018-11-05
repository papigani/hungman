# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 00:43:26 2018

@author: matsu
"""

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

app.run(port=8000)