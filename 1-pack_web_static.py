from fabric.api import run, env
from datetime import datetime

env.hosts = "127.0.0.1"


def do_pack():
    run("git clone https://github.com/mikek1337/AirBnb_clone_v2.git")
    run("cd ./AirBnb_clone_v2")
    run("mkdir versions > /dev/null 2>&1")
    test = run("tar -c -f -z -v versions/web_static_{year}{month}{day}{hour}{minute}{second}.tgz".format(year=datetime.year(
    ), month=datetime.month(), day=datetime.day(), hour=datetime.hour(), minute=datetime.minute(), second=datetime.second()))
    print(test)
