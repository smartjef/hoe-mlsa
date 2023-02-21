from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title

EDUCATION_LEVELS = (
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('Tertiary', 'Tertiary'),
    ('Masters', 'Masters'),
    ('PhD', 'PhD'),
)
class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    education_level = models.CharField(max_length=100, choices=EDUCATION_LEVELS)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-level']
    
class Hobby(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Hobbies'

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Contacts'
        