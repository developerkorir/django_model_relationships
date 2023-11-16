from django.db import models


# Create your models here.
# Artist
class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = "musicians"


# many to many
class Album(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    artists = models.ManyToManyField(Artist, related_name="albums")

    def __str__(self):
        return f"Album {self.name} - {self.release_year}"


# One to many
class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title

# TODO add one to one relationship
