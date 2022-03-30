from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from applications.profiles.utils import get_random_code


class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"

    def save(self, *args, **kwargs):
        ex = False
        if self.name and self.surname:
            to_slug = slugify(str(self.name) + " " + str(self.surname))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
            self.slug = to_slug
            super().save(*args, **kwargs)