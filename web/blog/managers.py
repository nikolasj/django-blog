from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        """
        Return a new QuerySet object. Subclasses can override this method to
        customize the behavior of the Manager.
        """
        return super(PublishedManager, self).get_queryset().filter(draft=False)
