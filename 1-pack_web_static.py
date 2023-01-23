from fabric.api import local, env
import datetime

env.hosts = "127.0.0.1"


def do_pack():

    local("mkdir versions > /dev/null 2>&1")

    test = local("sudo tar -cvf versions/web_static_{year}{month}{day}{hour}{minute}{second}.tgz ./web_static".format(year=datetime.datetime.today().year, month=datetime.datetime.today(
    ).month, day=datetime.datetime.today().day, hour=datetime.datetime.today().hour, minute=datetime.datetime.today().minute, second=datetime.datetime.today().second))
    print(test)
