import string
import random
from django.db import models


# Create your models here.
def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Website(models.Model):
    full_url = models.CharField(max_length=512, null=False, editable=False, unique=True)
    short_url = models.CharField(max_length=10, editable=False, unique=True, null=True)

    def save(self):
        if not self.short_url:
            self.short_url = id_generator()
            while Website.objects.filter(short_url=self.short_url).exists():
                self.short_url = id_generator()
        super(Website, self).save()
