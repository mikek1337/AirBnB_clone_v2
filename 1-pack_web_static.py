#!/usr/bin/python3

"""create archive."""

from fabric.api import local, env
import datetime
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file_name))
    return file_name
