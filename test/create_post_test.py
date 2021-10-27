import os
import pytest
from .blog_helper import BlogHelper
from E2EAF_blog_automation.blog.blogsvc import Blog
from E2EAF_auth_automation.auth.auth import Auth
import logging

env = os.environ.get('env')
if os.environ.get('env') is not None:
    env = os.environ.get('env')
else:
    env = 'qa'

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

auth = Auth(env)
blog = Blog(env)
blog_helper = BlogHelper(env, auth, blog)


@pytest.mark.parametrize(
    "test_case, username, password, title, content, slug", [
        ('valid_create_post', 'test', 'test', 'title_', 'content_', 'slug_'),
    ])
def test_create_post(test_context, test_case, username, password, title, content, slug):
    logger.info("************** Start Test: " + test_case + " ***********")
    result = True
    response, login = blog_helper.create_post(username=username, password=password, title=title, content=content,
                                              slug=slug)

    if not login:
        logging.info("Unable to authorize the user")
        result &= False

    if response.status_code == 200:
        logging.info("successfully created the new post")
    else:
        logger.info("Unable to create post " + str(response.status_code))
        result &= False
    assert result
    logger.info("************** End Test ***********")
