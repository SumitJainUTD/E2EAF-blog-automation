from E2EAF_auth_automation.auth.auth import Auth
from E2EAF_blog_automation.blog.blogsvc import Blog


class FeatureContext():
    def __init__(self, env, HIGH_TIME=None, MEDIUM_TIME=None, LOW_TIME=None):
        self.auth_client = Auth(env)
        self.blog_client = Blog(env)
        self.HIGH_TIME = HIGH_TIME
        self.MEDIUM_TIME = MEDIUM_TIME
        self.LOW_TIME = LOW_TIME