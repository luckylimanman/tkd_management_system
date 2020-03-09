from flask import Blueprint, flash, g, redirect, render_template, request, url_for # noqa

from . import database

bp = Blueprint('roster', __name__, url_prefix='/roster')


@bp.route('/', methods=['GET'])
def index():
    return render_template('roster/roster_index.html')


@bp.route('/check_in', methods=('GET', 'POST'))
def check_in():
    if request.method == 'POST':
        member_id = request.form['member_id']
        error = None
        if not member_id:
            error = '请填入会员ID'
        if error is None:
            session = database.DBSession()
            global get_member
            get_member = session.query(database.Member).filter(database.Member.id == member_id).one() # noqa
            session.close()
            return redirect(url_for('roster.check_in_confirm'))
        flash(error)
    return render_template('roster/check_in.html')


@bp.route('check_in_confirm', methods=('GET', 'POST'))
def check_in_confirm():
    if request.method == 'POST':
        training_gym = request.form['training_gym']
        session = database.DBSession()
        new_roster = database.Roster(member_id=get_member.id,
                                     member_name=get_member.name,
                                     training_gym=training_gym)
        session.add(new_roster)
        session.commit()
        session.close()

        session = database.DBSession()
        reduce_one = session.query(database.Member).filter(database.Member.id == get_member.id).one() # noqa
        reduce_one.validity_count -= 1
        session.commit()
        session.close()

        return render_template('add_success.html')
    return render_template('roster/check_in_confirm.html',
                           get_member_name=get_member.name,
                           get_member_phone=get_member.phone_number,
                           get_member_gender=get_member.gender)


@bp.route('/view_records', methods=('GET', 'POST'))
def view_records():
    if request.method == 'POST':
        session = database.DBSession()
        get_rosters = session.query(database.Roster).all()
        session.close()
        return render_template('roster/view_records_results.html', get_rosters=get_rosters) # noqa
    return render_template('roster/view_records.html')
