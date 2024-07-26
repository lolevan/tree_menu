from django.db import models


class MenuManager(models.Manager):
    def with_items(self):
        return self.prefetch_related(
            models.Prefetch(
                'items',
                queryset=MenuItem.objects.select_related('parent').order_by('parent', 'order')
            )
        )


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    objects = MenuManager()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('menu', 'name')
        ordering = ['order']
        indexes = [
            models.Index(fields=['menu', 'parent', 'order']),
        ]

    def __str__(self):
        return self.name
