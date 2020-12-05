from django.db import models


class PublishedManager(models.Manager):

    @property
    def published(self):
        return self.filter(draft=False)
