from mutagen.mp3 import EasyMP3
from pip._vendor import requests
import spotipy
import spotipy.util as util



def get_artists(data, total):
    list = []
    for i in range(total):
        list.append(data["tracks"][i]["artists"][0]["name"])
    return list

def get_albums(data, total):
    list = []
    for i in range(total):
        list.append(data["tracks"][i]["album"]["name"])
    return list

def get_tracks(data, total):
    list = []
    for i in range(total):
        list.append(data["tracks"][i]["name"])
    return list

def get_id(data):
    id = data["tracks"]["items"][0]["id"]
    return id

def get_data(track_name, artist_name, album_name):
    url = "https://api.spotify.com/v1/search"
    track_name.replace(" ", "%20")
    params = {"q": track_name + " " + artist_name + " " + album_name, "type": "track", "limit" : "5"}
    r = requests.get(url, params = params)
    data = r.json()
    return data

def get_data_list(data):
    track_data_list = []
    for i in range(len(data["tracks"]["items"])) :
        track_data_list.append(data["tracks"]["items"][i]["external_urls"]["spotify"])
    return track_data_list

def add_recs(token, song_id_list = []):
    limit = 5
    sp = spotipy.Spotify(auth=token)
    seed_tracks = []
    seed_tracks.append(song_id_list[0])
    song_recs = sp.recommendations(seed_tracks=seed_tracks, limit=limit)
    name_list = get_tracks(song_recs, limit)
    artist_list = get_artists(song_recs, limit)
    album_list = get_albums(song_recs, limit)
    print "The following songs were found, please select your preference: "
    for i in range(limit) :
        print str(i + 1) + " " + name_list[i] + " by " + artist_list[i] + " in the album " + album_list[i]
    selection_list = []
    selection = input("Please enter the selection number you would like to add to your library or 0 to exit: ")
    while(1):
        if(selection == 0):
            break
        selection_list.append(song_recs["tracks"][selection - 1]["id"])
        selection = input("Please enter the selection number you would like to add to your library or 0 to exit: ")
    return selection_list


def spotify_functionality(track, artist, album):
    scope = "user-library-modify"
    client_id = "24e38cbb98ba478eb09448f8a2c976db"
    client_secret = "6f708e45a9f545b3b391e7b2f9909eba"
    redirect_uri = "http://arulajmani.github.io"
    username = raw_input("Please enter your Spotify username")
    token = util.prompt_for_user_token(username, scope=scope, client_id=client_id,
                                       client_secret=client_secret, redirect_uri=redirect_uri)
    data = get_data(track,artist,album)
    song_id = get_id(data)
    add_list = []
    add_tracks = raw_input("Would you like to add the song to Your Music in Spotify? yes/no : ")
    while(1):
        if(add_tracks == "yes"):
            rec_input = raw_input("Would you like to get some additional recommendations? yes/no : ")
            while(1):
                if(rec_input == "yes"):
                    temp_list = []
                    temp_list.append(song_id)
                    add_list = add_recs(token,temp_list)
                    add_list.append(song_id)
                    add_to_lib(token, add_list)
                elif(rec_input == "no"):
                    add_list.append(song_id)
                    add_to_lib(token, add_list)
                else:
                    rec_input = raw_input("Please enter valid input yes/no ")
        elif(add_tracks == "no"):
            print "You decided not to add the track to Your Music in Spotify"
            quit()
        else:
            add_tracks = raw_input("Please enter valid input yes/no ")


def get_name(file):
    audio = EasyMP3(file)
    if("title" in audio):
        actual_name = audio["title"][0]
    else:
        actual_name = ""
    if("artist" in audio):
        actual_artist = audio["artist"][0]
    else:
        actual_artist = ""
    if("album" in audio):
        actual_album = audio["album"][0]
    else:
        actual_album = ""
    print "The song details are:"
    if(actual_name != ""):
        print "Track : " + actual_name
    if(actual_artist != ""):
        print "Artist : " + actual_artist
    if(actual_album != ""):
        print "Album : " + actual_album
    sp_functionality = raw_input("Would you like to try out some Spotify functionality? yes/no ")
    while(1):
        if (sp_functionality == "yes"):
            spotify_functionality(actual_name, actual_artist, actual_album)
        elif (sp_functionality == "no"):
            exit()
        else:
            sp_functionality = raw_input("Would you like to try out our Spotify functionality? yes/no ")


def add_to_lib(token, track_list = []):

    add_song = raw_input("Would you like to add the track to Spotify? yes/no :")
    while(1):
        if (add_song == "yes"):
            sp = spotipy.Spotify(auth=token)
            sp.current_user_saved_tracks_add(track_list)
            print "Done! Thanks for using MusicMatch"
            exit()
        elif(add_song == "no"):
            sure = raw_input("Are you sure? All your progress will be lost")
            if(sure == "yes"):
                exit()
        else:
            add_song = raw_input("Please enter valid input!")


def main():
    print "Welcome to MusicMatch, a simple program that lets you manage your local library, export songs to Spotify and \
get recommendations based on your existing library"
    file_name = raw_input("To start, simply enter the name of any unkown or known file you would like to manage using MusicMatch: ")
    get_name(file_name)

main()



