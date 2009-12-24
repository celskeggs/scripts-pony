# -*- coding: utf-8 -*-
"""WSGI environment setup for ScriptsPony."""

import getpass

from scriptspony.config.app_cfg import base_config

__all__ = ['load_environment']

#Use base_config to setup the environment loader function
tg_load_environment = base_config.make_load_environment()

def load_environment(global_conf,app_conf):
    ## Hack to make our sqlalchemy config depend on scripts user
    url = ('mysql://sql.mit.edu/%s+scripts-pony?read_default_file=~/.my.cnf'
           % getpass.getuser())
    global_conf['sqlalchemy.url'] = app_conf['sqlalchemy.url'] = url
    print "Overriding sqlalchemy.url to: %s" % url
    tg_load_environment(global_conf,app_conf)


