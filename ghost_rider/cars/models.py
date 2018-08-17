from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    img_url = models.CharField(max_length=100)
    description = models.CharField(max_length=280)
    owner = models.ForeignKey('auth.User', related_name='cars', on_delete=models.CASCADE)
    # highlighted = models.TextField()
    # linenos = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.make

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        # lexer = get_lexer_by_name(self.make)
        # linenos = 'table' if self.linenos else False
        # options = {'make': self.make} if self.make else {}
        # formatter = HtmlFormatter(style=self.style, linenos=linenos,
        #                         full=True, **options)
        # self.highlighted = highlight(self.code, lexer, formatter)
        super(Car, self).save(*args, **kwargs)
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=280)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment


