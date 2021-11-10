from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Person(User):
    gender_choice = [('M', 'Male'),
                     ('F', 'Female'),
                     ]
    gender = models.CharField(verbose_name='Gender', max_length=6, choices=gender_choice, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password1', 'password2']

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """
        Message: Show person name as default
        Parameters:
            self:
        Returns:
            name (str): Return person name
                """
        return '{} {}'.format(self.first_name.title(), self.last_name.title())


class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_complete = models.BooleanField(default=False)
    category = [
        ('HT', 'Home Task'),
        ('OT', 'Office Task'),
        ('MISC', 'Misc'),
    ]
    task_category = models.CharField(max_length=11, choices=category, blank=False)
    start_date = models.DateTimeField(default=datetime.now())
    completed_date = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """
        Message: Show task title as default
        Parameters:
            self:
        Returns:
            task_title (str): Return task title
        """
        return self.task_title
