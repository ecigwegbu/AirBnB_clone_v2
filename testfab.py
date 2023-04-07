#!/usr/bin/python3
"""fabric file for installing web server"""


from fabric.api import *

env.hosts = [
    '35.175.135.222',
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
]

# authentication
env.user = 'ubuntu'

run("ls")
