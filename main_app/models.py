from django.db import models
from django.urls import reverse
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

PROGRESS = (
    ('P', 'Pending'),
    ('I', 'Interviewing'),
    ('O', 'Offer Extended'),
    ('R', 'Rejected'),
)

class Connection(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField('URL', max_length=50, blank=True)
    location = models.CharField('Place/Event Met', max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('connections_detail', kwargs={'connection_id': self.id})
    
    def days_since_update(self):
        last_update = self.interaction_set.all().last().date
        last_update_dt = datetime.combine(last_update, datetime.min.time())
        difference = datetime.now() - last_update_dt
        day_diff = difference.days
        return day_diff

class Job(models.Model):
    company = models.CharField(max_length=50)
    date = models.DateField('Applied Date')
    salary = models.IntegerField(default=0)
    position = models.CharField(max_length=50)
    notes = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    bookmarked = models.BooleanField('Add Bookmark', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connections = models.ManyToManyField(Connection, blank=True)

    progress = models.CharField(
        max_length=1,
        choices=PROGRESS,
        default=PROGRESS[0][0]
    )
    
    def __str__(self):
        return f'{self.company} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id': self.id})
    
    def days_since_update(self):
        day_diff = 0
        last_update = self.date
        if self.status_set.all().count():
            last_update = self.status_set.all().last().date
        last_update_dt = datetime.combine(last_update, datetime.min.time())
        difference = datetime.now() - last_update_dt
        day_diff = difference.days
        return day_diff
    
    def pending_todos(self):
        todos = self.todo_set.filter(done=False)
        return todos


class Todo(models.Model):
    description = models.TextField(max_length=200)
    done = models.BooleanField(default=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'
    

class Status(models.Model):
    description = models.TextField('Add New Status Update', max_length=200)
    date = models.DateField('')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'
    
    class Meta:
        ordering = ['date']



class Interaction(models.Model):
    description = models.TextField('Add Interaction',max_length=200)
    date = models.DateField('')
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'
    
    class Meta:
        ordering = ['date']
    


