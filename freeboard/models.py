from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     # user_id = models.IntegerField(primary_key=True)
#     name        = models.CharField(max_length=15, null=True)
#     profile_img = models.CharField(max_length=255, null=True)

class Post(models.Model):
    # post_id = models.IntegerField(default=0)
    subject  = models.CharField(max_length=200)
    content  = models.TextField()
    # author   = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    write_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.subject