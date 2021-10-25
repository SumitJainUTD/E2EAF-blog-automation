import pytest
import os

from main.utils.configuration import Configuration

env = None
logged_in_user = {}


def pytest_addoption(parser):
    parser.addoption("--env")


@pytest.fixture(scope="session", autouse=True)
def before_suite(request):
    print('Beginning of the suite')
    global env
    env = request.config.getoption("--env")
    env = os.environ.get('env')
    if os.environ.get('env') is not None:
        env = os.environ.get('env')
    else:
        env = 'qa'
    properties = Configuration(env)

    def after_suite():
        print('End of the suite')

    request.addfinalizer(after_suite)


def get_env():
    return env


def get_token_for_user(user, refresh=False):
    tokens = logged_in_user.get(user)
    auth = Auth()
    if refresh:
        tokens = auth.login(refresh_token=tokens.get('refresh'))
        logged_in_user[user] = tokens
    else:
        username = user.get('username')
        password = user.get('password')
        # login the user
        if tokens is None:
            tokens = auth.login(username=username, password=password)
            logged_in_user[user] = tokens
        else:
            if not auth.verify_token(tokens.get('access')):
                return get_token_for_user(user=user, refresh=True)

    return tokens
