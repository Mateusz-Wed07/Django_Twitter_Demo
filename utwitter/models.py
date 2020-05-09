from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Tweet(models.Model):
    content = models.TextField(max_length=140)
    creation_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        content = self.content
        if len(content) > 15:
            words = content.split()
            short = ' '.join(words[:4])
            content = short+'...'
        return "{}: {}".format(self.user.username, content)
