from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}_{self.pk}'

    def goto_post_detail(self):
        return f'/community/{self.pk}'

