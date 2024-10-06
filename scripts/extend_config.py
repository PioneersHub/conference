""" Alter config on run
 https://www.mkdocs.org/user-guide/configuration/#hooks
 """
from datetime import datetime
from pathlib import Path

import yaml


def on_config(config, **kwargs):
    """ Alter the config on run:

    1. Alter configuration with attributes 'config.yml'
       To simplify configuration for users, configuration parameters (event name, emails) are stored in ‘config.yml’

    2. Add current year to copyright (Footer)

    """
    content = Path(__file__).parents[1] / 'config.yml'
    with content.open('r') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)

    for key, value in content.items():
        if key.startswith('site_') or key.startswith('repo_'):
            config[key] = value
        elif key == 'copyright':
            config.copyright = (
                f'Copyright © {content[key]["start_year"]}{"-" + str(datetime.now().year) if datetime.now().year > int(content[key]["start_year"]) else ""} {content[key]["owner"]} – '
                f'<a href="#__consent">Change cookie settings</a>')
        else:
            config['extra'][key] = value
