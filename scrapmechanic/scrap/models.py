from django.db import models
from django.urls import reverse


class mods(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    creator = models.CharField(max_length=50,verbose_name='создатель')
    content = models.TextField()
    steam = models.URLField()
    img = models.ImageField(upload_to="photos/%m")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True, db_index=True)

    class Meta:
        verbose_name_plural  = 'моды'
        verbose_name = 'моды'
        ordering = ['time_create']


    def get_absolute_url(self):
        return reverse('about', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('mods', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name