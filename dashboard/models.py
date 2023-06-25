from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

#contact form


class HomePage(models.Model):
    background_photo = models.ImageField(upload_to='static/homepage_img')
    title = models.CharField(max_length=100,default='My Homepage')
    description = models.TextField()

    def __str__(self):
        return self.title
    

class ContactForm(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name

class Office(models.Model):
    title = models.CharField(max_length=255,default='Office')
    address = models.TextField()
    fax = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    cellphone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    



class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='static/aboutpage_img')

    def __str__(self):
        return self.title
    

class TeamMemberKBG(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='static/Team_image')

    def __str__(self):
        return self.name
    
class TeamMemberKBGRA(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='static/Team_image')

    def __str__(self):
        return self.name