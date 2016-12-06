#!/usr/bin/python3

from charmhelpers.core.services import helpers
from charmhelpers.core.services.base import ServiceManager

import actions


def manage():
    manager = ServiceManager([
        {
            'service': '<your service>',
            'ports': [],  # ports to after start
            'provided_data': [
                # context managers for provided relations
                # e.g.: helpers.HttpRelation()
            ],
            'required_data': [
                # data (contexts) required to start the service
                # e.g.: helpers.RequiredConfig('domain', 'auth_key'),
                #       helpers.MysqlRelation(),
            ],
            'data_ready': [
                helpers.render_template(
                    source='upstart.conf',
                    target='/etc/init/testing'),
                actions.log_start,
            ],
        },
    ])
    manager.manage()
