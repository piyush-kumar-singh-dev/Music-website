from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100,help_text='albums title')
    artist = models.CharField(max_length=70, help_text='albums artist')
    genre = models.CharField(max_length=20, help_text='albums genre')
    ryear = models.DateField(help_text='release data')
    image = models.FileField(validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    def __str__(self):
        return self.name+' '+self.artist

class Song(models.Model):
    al_id = models.ForeignKey(Album,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='song title')
    artist = models.CharField(max_length=70, help_text='song artist')
    genre = models.CharField(max_length=20, help_text='song genre')
    file  = models.FileField(validators=[FileExtensionValidator(['mp3','mp4','aac'])])
    def __str__(self):
        return self.name+' '+self.artist