from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = models.TextField()
    content_body = models.TextField(editable=False)
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', 'updated_at')

    def __unicode__(self):
        return unicode(self.title)
