import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.run(debug=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:

        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import index, member, gym, roster, exam
    app.register_blueprint(member.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(gym.bp)
    app.register_blueprint(roster.bp)
    app.register_blueprint(exam.bp)

    return app
