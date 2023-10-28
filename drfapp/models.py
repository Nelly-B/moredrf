from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    email = models.EmailField(default='@nvit.tech')
    mobile_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title