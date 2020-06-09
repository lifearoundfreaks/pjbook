from django.core.management.utils import get_random_secret_key
import json
import os


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_STRUCTURE_PATH = os.path.join(SITE_ROOT, "structure.json")
PRIVATE_SETTINGS_PATH = os.path.join(SITE_ROOT, "private_settings.py")
TEMPLATE = (
    "INSTALLED_PROJECT_VERSION = {version}\n"
    "SECRET_KEY = '{secret_key}'\n"
    "DEBUG = {debug}\n"
    "SITE_ROOT = '{siteroot}'\n"
    "{allowed_hosts}"
)


def format_allowed_hosts(_input):
    return "ALLOWED_HOSTS = [\n    " + ",\n    ".join(
        map(lambda x: f"'{x}'", _input.split())) + "\n]\n"


def setup_project(force=False):
    if force or setup_required():
        print("Starting a project setup procedure...")

        user_input = None
        while user_input not in ['y', 'n']:
            user_input = input('Turn on debug? (y/n)').lower()
        debug = user_input == 'y'

        allowed_hosts = '' if debug else format_allowed_hosts(
            input('Enter allowed hosts separated by whitespaces:\n'))

        try:
            with open(PROJECT_STRUCTURE_PATH, 'r') as _file:
                version = json.load(_file)['version']
        except FileNotFoundError:
            version = 0

        data = {
            'version': version,
            'secret_key': get_random_secret_key(),
            'debug': debug,
            'siteroot': SITE_ROOT.replace("\\", "\\\\"),
            'allowed_hosts': allowed_hosts,
        }
        with open(PRIVATE_SETTINGS_PATH, 'w') as _file:
            _file.write(TEMPLATE.format(**data))


def setup_required():
    try:
        from .private_settings import INSTALLED_PROJECT_VERSION
        with open(PROJECT_STRUCTURE_PATH, 'r') as _file:
            version = json.load(_file)['version']
    except (FileNotFoundError, ModuleNotFoundError):
        return True

    return INSTALLED_PROJECT_VERSION != version
