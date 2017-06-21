from django.db import models
from django.conf import settings

'''
Post모델
author(User 모델로 연결)
photo
comment
created_date
modify_date
'''


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(blank=True)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)
