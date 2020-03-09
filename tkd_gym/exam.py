from flask import Blueprint, flash, g, redirect, render_template, request, url_for # noqa

from . import database


bp = Blueprint('exam', __name__, url_prefix='/exam')


@bp.route('/', methods=['GET'])
def index():
    return render_template('exam/exam_index.html')


@bp.route('/new', methods=['GET'])
def new():
    return render_template('exam/new.html')


@bp.route('/history', methods=['GET'])
def history():
    return render_template('exam/history.html')


@bp.route('/rules', methods=['GET'])
def rules():
    return render_template('exam/rules.html')
