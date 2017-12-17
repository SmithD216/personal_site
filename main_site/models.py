from django.db import models

# Create your models here.

class Entry(models.Model):
    """An entry on the front page of the website."""
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=108)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

class CodeEntry(models.Model):
    """An entry on the programming pages of the website."""
    JAVASCRIPT = 'JS'
    PYTHON = 'PYTHON'

    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=108)
    LANGUAGE_CHOICES = (
        (JAVASCRIPT, 'Javascript'),
        (PYTHON, 'Python'),
    )
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default=JAVASCRIPT)
    explanation = models.TextField()
    notes = models.TextField(blank=True)
    attempt = models.TextField()
    goal = models.TextField()

    class Meta:
        verbose_name_plural = 'code_entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.title