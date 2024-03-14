import datetime

from data import db_session
from flask import Flask

from data.models.models import User, Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()
    # user_1 = User()
    #
    # user_1.surname = 'Scott'
    # user_1.name = 'Ridley'
    # user_1.age = 21
    # user_1.position = 'captain'
    # user_1.speciality = 'research engineer'
    # user_1.address = 'module_1'
    # user_1.email = 'scott_chief@mars.org'
    #
    # user_2 = User()
    #
    # user_2.surname = 'Dmit'
    # user_2.name = 'Trop'
    # user_2.age = 19
    # user_2.position = 'senior'
    # user_2.speciality = 'python developer'
    # user_2.address = 'module_4'
    # user_2.email = 'dmit_trop@mars.org'
    #
    # user_3 = User()
    #
    # user_3.surname = 'Lilu'
    # user_3.name = 'Poller'
    # user_3.age = 23
    # user_3.position = 'middle'
    # user_3.speciality = 'c developer'
    # user_3.address = 'module_2'
    # user_3.email = 'lilu_poller@mars.org'
    #
    # user_4 = User()
    #
    # user_4.surname = 'Eva'
    # user_4.name = 'Krop'
    # user_4.age = 32
    # user_4.position = 'teamlead'
    # user_4.speciality = 'project manager'
    # user_4.address = 'module_0'
    # user_4.email = 'eva_krop@mars.org'
    #
    # session.add_all([user_2, user_3, user_4])

    job_1 = Jobs()
    job_1.team_leader = 1
    job_1.job = 'deployment of residential modules 1 and 2'
    job_1.work_size = 15
    job_1.collaborators = '2, 3'
    job_1.start_date = datetime.datetime.now(datetime.UTC)
    job_1.is_finished = False

    session.add(job_1)

    session.commit()

    app.run()


if __name__ == '__main__':
    main()
