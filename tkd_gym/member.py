# coding=UTF-8
from flask import Blueprint, flash, render_template, request, redirect, url_for


from . import database

bp = Blueprint('member', __name__, url_prefix='/member')


@bp.route('/', methods=['GET'])
def index():
    return render_template('member/member_index.html')


@bp.route('/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        registration_date = request.form['registration_date']
        birthday = request.form['birthday']
        belt = request.form['belt']
        gym = request.form['gym']
        unlimited_count = int(request.form['unlimited_count'])

        if unlimited_count == 1:
            validity_count = 9999
            validity_date = str(int(registration_date[:4])+1) + registration_date[4:] # noqa

        if unlimited_count == 0:
            validity_count = 20
            validity_date = '9999-01-01'
        error = None

        if not name or not gender or not phone_number or not registration_date:
            error = '姓名、性别、电话号码、注册日期为必填项'
        if error is None:
            session = database.DBSession()
            new_member = database.Member(name=name, gender=gender,
                                         phone_number=phone_number,
                                         registration_date=registration_date,
                                         birthday=birthday, belt=belt, gym=gym,
                                         validity_count=validity_count,
                                         validity_date=validity_date,
                                         unlimited_count=unlimited_count)
            session.add(new_member)
            session.commit()
            session.close()
            return render_template('add_success.html')
        flash(error)
    return render_template('member/new.html')


@bp.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == 'POST':
        edit_id = request.form['edit_id']
        session = database.DBSession()
        global show_info
        show_info = session.query(database.Member).filter(database.Member.id == edit_id).one() # noqa
        session.close()
        return redirect(url_for('member.edit_by_id'))
    return render_template('member/edit.html')


@bp.route('/edit_by_id', methods=('GET', 'POST'))
def edit_by_id():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        birthday = request.form['birthday']
        belt = request.form['belt']
        gym = request.form['gym']

        session = database.DBSession()
        edit_member = session.query(database.Member).filter(database.Member.id == show_info.id).one() # noqa
        edit_member.name = name
        edit_member.gender = gender
        edit_member.phone_number = phone_number
        edit_member.birthday = birthday
        edit_member.belt = belt
        edit_member.gym = gym
        session.commit()
        session.close()
        return render_template('add_success.html')
    return render_template('member/edit_by_id.html',
                           show_info=show_info)


@bp.route('/archive', methods=('GET', 'POST'))
def archive():
    if request.method == 'POST':
        session = database.DBSession()
        get_members = session.query(database.Member).all()
        session.close()
        return render_template('member/archive_results.html', get_members=get_members) # noqa
    return render_template('member/archive.html')


@bp.route('/recover', methods=('GET', 'POST'))
def recover():
    return render_template('member/recover.html')
