from django.db import models

# Create your models here.

class Entry(models.Model):
    """A post on the website."""
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=108)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."