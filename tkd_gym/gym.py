from flask import Blueprint, flash, g, redirect, render_template, request, url_for # noqa

from . import database

bp = Blueprint('gym', __name__, url_prefix='/gym')


@bp.route('/', methods=['GET'])
def index():
    return render_template('gym/gym_index.html')


@bp.route('/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        name = request.form['name']

        error = None

        if not name:
            error = '请正确填入道馆名称'
        if error is None:
            session = database.DBSession()
            new_gym = database.Gym(name=name)
            session.add(new_gym)
            session.commit()
            session.close()
            return render_template('gym/add_success.html')
        flash(error)
        # gyms = session.query(database.Gym).all()

    return render_template('gym/new.html')


@bp.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        edit_id = request.form['edit_id']
        session = database.DBSession()
        global show_info
        show_info = session.query(database.Gym).filter(database.Gym.id == edit_id).one() # noqa
        session.close()
        return redirect(url_for('gym.edit_by_id'))
    return render_template('gym/edit.html')


@bp.route('/edit_by_id', methods=('GET', 'POST'))
def edit_by_id():
    if request.method == 'POST':
        name = request.form['name']
        session = database.DBSession()
        edit_member = session.query(database.Gym).filter(database.Gym.id == show_info.id).one() # noqa
        edit_member.name = name
        session.commit()
        session.close()
        return render_template('add_success.html')
    return render_template('gym/edit_by_id.html', show_info=show_info)


@bp.route('/archive', methods=('GET', 'POST'))
def archive():
    if request.method == 'POST':
        session = database.DBSession()
        get_gyms = session.query(database.Gym).all()
        session.close()
        return render_template('gym/archive_results.html', get_gyms=get_gyms)
    return render_template('gym/archive.html')


@bp.route('/recover', methods=('GET', 'POST'))
def recover():
    return render_template('gym/recover.html')
