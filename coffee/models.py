from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class WholebeanPost(models.Model):
    wholebean_id = models.SmallAutoField(primary_key=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='post_wholebean')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    wholebean_name = models.CharField(max_length=25)
    wholebean_origin = models.CharField(max_length=25)
    wholebean_brand = models.CharField(max_length=25)
    wholebean_content = models.TextField(max_length=400, null=True)
    wholebean_image = CloudinaryField('image', default='placeholder')
    slug = models.Slugfield(unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta: 
        ordering = ["-created_on"]
    
    def __str__(self):
        return self.wholebean_name


    def save(save, *args, **kwargs):
        """
        Function to auto generate slugfield
        """
        autoslug = self.wholebean_brand + wholebean_name
        self.slug = slugify(autoslug)
        super(WholebeanPost, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(WholebeanPost,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta: 
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)




   