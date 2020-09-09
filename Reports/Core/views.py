from flask import render_template, Blueprint, session, url_for, redirect, send_file, send_from_directory


core = Blueprint('core', __name__)

@core.route('/')
def base():

    return render_template('base.html')


@core.route('/download', methods = ['GET', 'POST'])
def download():

    return render_template('download.html')