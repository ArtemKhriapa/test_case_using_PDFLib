from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', blank=True, null=True)
    question_name = models.CharField(max_length=255)
    value = models.TextField()
    index = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "User: %s, %s" % (self.user.username, self.value)

