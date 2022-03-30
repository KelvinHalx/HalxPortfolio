from flask import render_template, url_for, flash, redirect, request, abort

# Entire Site
@app.route('/')
def index():
    return render_template('front_end/index.html')
