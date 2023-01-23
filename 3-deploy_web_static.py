#!/usr/bin/python3

"""create archive."""

from fabric.api import local, env, run, put
from datetime import datetime
from os.path import isdir, exists
env.hosts = ['34.204.60.99', '54.164.127.171']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """extract and deploy"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        new_dir = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {path}{new_dir}".format(path=path, new_dir=new_dir))
        run("tar -xzf /tmp/{filename} -C {path}{new_dir}/".format(
            filename=filename, path=path, new_dir=new_dir))
        run('rm /tmp/{filename}'.format(filename=filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, new_dir))
        run('rm -rf {}{}/web_static'.format(path, new_dir))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, new_dir))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
