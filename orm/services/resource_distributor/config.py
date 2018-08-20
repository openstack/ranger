import orm.base_config as config
# Pecan Application configurations
app = {
    'root': 'orm.services.resource_distributor.rds.controllers.root.RootController',
    'modules': ['orm.services.resource_distributor.rds'],
    'service_name': 'RDS'
}

server = {
    'port': config.rds['port'],
    'host': config.orm_host
}

# DB configurations
database = {
    'url': config.db_url + 'orm_rds?charset=utf8'
}

sot = {
    'type': 'git',
}

git = {
    # possible values : 'native', 'gittle'
    'type': 'native',
    'local_repository_path': config.rds['repo_local_location'],
    'file_name_format': 's_{}.yml',
    'relative_path_format': '/{}/hot/{}/{}',
    'commit_message_format': 'File was added to repository: {}',
    'commit_user': config.rds['repo_user'],
    'commit_email': config.rds['repo_email'],
    'git_server_url': config.rds['repo_remote_location'],
    'git_cmd_timeout': 45
}

audit = {
    'audit_server_url': config.audit_server['base_url'] + 'v1/audit/transaction',
    'num_of_send_retries': 3,
    'time_wait_between_retries': 1
}

cms = {
    'base_url': config.cms['base_url'],
    'delete_region': 'v1/orm/customers/{0}/regions/{1}'
}

fms = {
    'base_url': config.fms['base_url'],
    'delete_region': 'v1/orm/flavors/{0}/regions/{1}'
}

ims = {
    'base_url': config.ims['base_url'],
    'metadata_path': 'v1/orm/images/{0}/regions/{1}/metadata',
    'delete_region': 'v1/orm/images/{0}/regions/{1}'
}

rms = {
    'base_url': config.rms['base_url'],
    'all_regions_path': 'v2/orm/regions'
}

ordupdate = {
    'discovery_url': 'http://' + config.orm_host,
    'discovery_port': config.rms['port'],
    'template_type': 'hot',
    # This flag should be false only in case the ord does not support https.
    'https_enabled': False,
    # ORD supports HTTPS and you don't need a certificate? set 'cert_path': ''
    'cert_path': ''
}

UUID_URL = config.uuid['base_url'] + 'v1/uuids'

# yaml configurations
yaml_configs = {
    'customer_yaml': {
        'yaml_version': '2014-10-16',
        'yaml_options': {
            'quotas': True,
            'type': 'ldap'
        },
        'yaml_keys': {
            'quotas_keys': {
                'keypairs': 'key_pairs',
                'network': 'networks',
                'port': 'ports',
                'router': 'routers',
                'subnet': 'subnets',
                'floatingip': 'floating_ips'
            }
        },
        'cms_template_version': {
            'resource_v1': {
                'ranger_agent_version': 3.0,
                'quota_unsupported_params': ['vips', 'members', 'pools',
                                             'nat_instance', 'route_table',
                                             'health_monitors', 'loadbalancer',
                                             'listener']
            },
            'resource_v2': {
                'ranger_agent_version': 3.6,
                'quota_unsupported_params': []
            }
        }
    },
    'flavor_yaml': {
        'yaml_version': '2013-05-23',
        'yaml_args': {
            'rxtx_factor': 1
        }
    },
    'image_yaml': {
        'yaml_version': '2014-10-16'
    }
}

# value of status to be blocked before creating any resource
block_by_status = "Submitted"

# this tells which values to allow resource submit the region
allow_region_statuses = ['functional']

region_resource_id_status = {
    # interval_time_validation in minutes
    'max_interval_time': {
        'images': 2,
        'tenants': 2,
        'flavors': 2,
        'users': 2,
        'default': 2
    },
    'allowed_status_values': {
        'Success',
        'Error',
        'Submitted'
    },
    'allowed_operation_type':
    {
        'create',
        'modify',
        'delete'
    },
    'allowed_resource_type':
    {
        'customer',
        'image',
        'flavor'
    },
    'allowed_ranger_agent_resource_version':
    {
        'customer': '3.0',
        'image': '3.0',
        'flavor': '3.0'
    }
}

logging = {
    'root': {'level': 'INFO', 'handlers': ['console']},
    'loggers': {
        'orm.services.resource_distributor.rds': {
            'level': config.debug_level,
            'handlers': ['console', 'Logfile'],
            'propagate': False
        },
        'orm.common.orm_common': {'level': config.debug_level,
                                  'handlers': ['console', 'Logfile'],
                                  'propagate': False},
        'orm.common.client.audit.audit_client': {
            'level': config.debug_level,
            'handlers': ['console', 'Logfile'],
            'propagate': False
        },
        'pecan': {'level': config.debug_level,
                  'handlers': ['console'], 'propagate': False},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': config.debug_level,
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        },
        'Logfile': {
            'level': config.debug_level,
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 50000000,
            'backupCount': 10,
            'filename': config.rds['log'],
            'formatter': 'simple'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': '%(asctime)s [%(padded_color_levelname)s] [%(name)s] [%(threadName)s] %(message)s',
            '__force_dict__': True
        }
    }
}


verify = config.ssl_verify

authentication = {
    "enabled": config.token_auth_enabled,
    "mech_id": config.token_auth_user,
    "mech_pass": config.token_auth_pass,
    "tenant_name": config.token_auth_tenant,
    "token_role": config.token_auth_user_role,
    # The Keystone version currently in use. Can be either "2.0" or "3"
    "keystone_version": "3"
}
