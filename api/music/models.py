from django.db import models

# Create your models here.
class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    #song title
    title = models.CharField(max_length=255, null=False)
    #name artist
    artist = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return "{} - {}".format(self.id, self.title, self.artist)