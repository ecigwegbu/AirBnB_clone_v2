#!/usr/bin/python3
""" Fabric file to archive a folser"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
       generates a web archive
    """
    dn = datetime.now()
    fname = "web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(
        dn.year, dn.month, dn.day, dn.hour, dn.minute, dn.second)
    local("if [ ! -d versions ]; then sudo mkdir versions; fi")
    result = local("sudo tar -cvzf versions/{} web_static".format(fname))
    if not result.failed:
        return fname
    else:
        return None
