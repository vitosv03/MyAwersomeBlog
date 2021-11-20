from django.db import models

# 1. Create Post model. It should have the following attributes:
# 	title
# 	date
# 	text
# 	image
#
# 2. Make all needed operations to add Blog app with Post model to admin


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
