import json

from E2EAF_blog_automation.resources.configuration import Configuration
from E2EAF_common import ApiClient
from ..resources import blog_constants


class Blog:

    def __init__(self, env=None):
        self.env = env
        self.config = Configuration(env)
        self.api_client = ApiClient()

    def create_post_api(self, post, headers=None):

        url = self.config.base_uri + blog_constants.blog_base_uri + blog_constants.create_post_uri

        body_dict = {"title": post.title, "content": post.content, "slug": post.slug}
        body = json.dumps(body_dict)

        response = self.api_client.call_api(method="POST", url=url, data=body, headers=headers)
        return response


