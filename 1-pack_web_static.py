# Import Fabric's API module
from fabric.api import *


env.hosts = [
    '35.175.135.222'
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
]
# Set the username
env.user   = "ubuntu"

# Set the password [NOT RECOMMENDED]
# env.password = "passwd"

def update():
    """
        Update the default OS installation's
        basic default tools.
                                            """
    sudo("apt    update")

def install_nginx():
    """ Download and install memcached. """
    sudo("apt install -y nginx")

def update_install():

    # Update
    update()

    # Install
    install_nginx()
