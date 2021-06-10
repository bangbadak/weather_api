from django.db import models
from account.models import ID
from community.models import Post
# Create your models here.
class My_info(models.Model):
    password = ID.password
    title = Post.title

    def goto_post_detail(self):
        return f'/community/{self.pk}'