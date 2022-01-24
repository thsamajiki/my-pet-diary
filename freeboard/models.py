from django.db import models

class Post(models.Model):
    # post_id = models.IntegerField(default=0)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    pub_date = models.DateTimeField()