from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort

# Entire Site
@app.route('/')
def index():
    return render_template('index.html')
