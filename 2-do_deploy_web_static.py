#!/usr/bin/python3
"""deploy archives to servers"""

# Import Fabric's API module
from fabric.api import *
from pathlib import Path


# set env parameters
env.hosts = [
 '35.175.135.222',
 '52.3.240.190'
]
env.user = "ubuntu"
env.key_filename = "/root/.ssh/id_rsa"


def do_deploy(archive_path):
    """
       deploy an archive to web server
    """

    local("echo Executing task 'do_deploy'")
    fpath = Path(archive_path)
    fname = Path(archive_path).name
    fstem = Path(archive_path).stem
    if not fpath.exists():
        return False
    r1 = put(archive_path, "/tmp/{}".format(fname))
    r2 = sudo("mkdir -p /data/web_static/releases/{}".format(fstem))
    r3 = sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
        fname, fstem))
    r4 = sudo("rm /tmp/{}".format(fname))
    r5 = sudo("rm -rf /data/web_static/releases/{}/web_static".format(fstem))
    r6 = sudo("rm -rf /data/web_static/current")
    r7 = sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(fstem))

    if r1.failed or r2.failed or r3.failed or r4.failed or\
            r5.failed or r6.failed or r7.failed:
        return None
    else:
        return True
