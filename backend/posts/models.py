from django.db import models

class Post(models.Model):
    caption = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption[:20]
