import configparser

import requests


class Configuration(object):
    def __init__(self, env):
        self.users = None
        config = configparser.ConfigParser(allow_no_value=True)
        if env == 'qa':
            config.read('resources/project-qa.cfg')
        elif env == 'staging':
            config.read('resources/project-lt.cfg')
        elif env == 'prod':
            config.read('resources/project-prd.cfg')
        else:
            config.read('project-qa.cfg')

        self.base_uri = config.get('GlobalSection', 'base_uri')
        self.auth_uri = config.get('GlobalSection', 'auth_uri')
        self.post_uri = config.get('GlobalSection', 'post_uri')
        self.create_post_uri = config.get('GlobalSection', 'create_post_uri')
        self.update_post_uri = config.get('GlobalSection', 'update_post_uri')
        self.db_host = config.get('GlobalSection', 'audience_uri')
        self.users['first_admin_user'] = {'username': config.get('FirstAdminSection', 'username'),
                                          'password': config.get('FirstAdminSection', 'password')}
        self.SESSION = requests.Session()
