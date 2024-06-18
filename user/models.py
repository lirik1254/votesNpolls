from django.db import models
from django.conf import settings
from django.db import models
from registration.models import User
from django.db.models import Sum


class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_polls')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    @property
    def votes_percentage(self):
        total_votes = self.poll.choices.aggregate(total_votes=Sum('votes'))['total_votes'] or 0
        if total_votes > 0:
            return (self.votes / total_votes) * 100
        else:
            return 0