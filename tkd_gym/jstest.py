from flask import Blueprint, jsonify


bp = Blueprint('jstest', __name__, url_prefix='/jstest')


@bp.route('/', methods=('GET', 'POST'))
def jstest():
    t = "hello"
    return jsonify(t)
