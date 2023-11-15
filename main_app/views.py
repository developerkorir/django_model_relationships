from django.http import HttpResponse
from django.shortcuts import render

from main_app.models import Artist, Song


# Create your views here.
def show(request):
    # Fetching
    # artist = Artist.objects.order_by("?").first()
    # print(artist)
    # albums = artist.album_set.all()
    # # print(albums)
    # for alb in albums:
    #     print(alb.name, alb.release_year)
    #     songs = alb.songs.all()
    #     print(len(songs), "songs")
    song = Song.objects.order_by('?').first()
    print(song)
    album = song.album
    print(album)
    artists = album.artists.all().values('name')
    print(artists)
    return HttpResponse("Check the results on the console")
