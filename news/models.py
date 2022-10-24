from django.db import models
from django.contrib.auth.models import User
# from sorl.thumbnail import get_thumbnail

# Create your models here.

CATEGORIES = (
    ('lifestyle', 'Lifestyle'),
    ('sport', 'Sport'),
    ('travels', 'Travels'),
    ('skeping', 'Skeping'),
    ('fashion', 'Fashion'),
    ('night party', 'Night Party'),
    ('see beach', 'See Beach'),
    ('technology', 'Technology'),
    ('corporate', 'Corporate'),
    ('event time', 'Event Time'),
    ('politics', 'Politics'),
)


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    body = models.TextField()
    feature_image = models.FileField(upload_to='news-gallery/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']
        verbose_name_plural = 'News'

    def __str__(self):
        return '{} by {} on {}'.format(self.title, self.author, self.pub_date)

    # def save(self, *args, **kwargs):
    #     if self.feature_image:
    #         self.feature_image = get_thumbnail(self.feature_image, '500x600', quality=99)
    #     super(News, self).save(*args, **kwargs)

