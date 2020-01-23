from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField
    post_name = models.CharField(max_length=50)
    post_publish_date = models.DateTimeField(auto_now=False)
    post_short_description = models.TextField
    post_heading = models.CharField(default="", max_length=50)
    post_sub_heading = models.CharField(default="", max_length=100)
    post_body = models.TextField(default="")
    post_link_of_destination_heading = models.CharField(default="", max_length=50)
    post_link_of_destination =models.URLField(default="")
    post_img = models.ImageField(default="", upload_to='blog/images',blank=True)

    def __str__(self):
        return self.post_name

