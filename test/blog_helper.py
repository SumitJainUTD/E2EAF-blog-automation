from E2EAF_common.common_utils import get_random_string
from E2EAF_blog_automation.blog.blog_objects import Post
import logging


class BlogHelper():
    def __init__(self, env=None, test_context=None):
        self.env = env
        self.test_context = test_context

    def create_post(self, username=None, password=None, title=None, content=None, slug=None):
        rnd = get_random_string()
        if title is not None:
            title = "title_" + rnd
        if content is not None:
            content = "content_" + rnd
        if slug is not None:
            slug = rnd
        post = Post(title, content, slug)

        response = self.test_context.auth_client.get_token(username=username, password=password)

        access_token = None
        if response.status_code == 200:
            access_token = response.json()['access']
            refresh = response.json()['refresh']
        else:
            logging.error("Unable to login with give credentials")
            return None, False

        headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
        return  self.test_context.blog_client.create_post_api(post, headers=headers), True
