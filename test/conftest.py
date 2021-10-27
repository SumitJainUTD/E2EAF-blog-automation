import pytest
import os
from .feature_context import FeatureContext


@pytest.fixture(scope='session')
def test_context(request) -> FeatureContext:
    if os.environ.get('env') is not None:
        env = os.environ.get('env')
    else:
        env = 'qa'

    return FeatureContext(env)
