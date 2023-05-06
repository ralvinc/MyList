from django.db import models
from django.contrib.auth.models import User

class WatchOrRead(models.Model):
    action = models.CharField(max_length=200)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name_plural = 'Watch or Read'

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    watch_or_read = models.ForeignKey(WatchOrRead, on_delete=models.CASCADE, default='Watch')
    note = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['completed']