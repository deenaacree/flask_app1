from flask import Flask, render_template
from worst_songs import WORST_SONGS

app = Flask(__name__)



# retrieve all the songs from the dataset and put them into a list
def get_songs(source):
    # new empty list
    songs = []
    # loop through the source list
    for row in source:
        song = row["Song Title"]
        # add the title to the list
        songs.append(song)
    return (songs)


# find the row that matches the song name, retrieve artist, year, info, and links for that title
def get_songinfo(source, song):
    for row in source:
        if song == row["Song Title"]:
            artist = row["Artist"]
            year = row["Year"]
            info = row["Information"]
            wiki = row["Wikipedia Link"]
            youtube = row["YouTube Link"]
    return song, artist, year, info, wiki, youtube


@app.route('/list')
def index():
    songs = get_songs(WORST_SONGS)
    return render_template('list.html', songs=songs)


@app.route('/list/<song>')
def page(song):
    song, artist, year, info, wiki, youtube = get_songinfo(WORST_SONGS, song)
    return render_template('song.html', song=song, artist=artist, year=year, info=info, wiki=wiki, youtube=youtube)



# the code below works in the terminal to show that the information is being gathered
'''
# run the functions and use variables to hold what they return
songs = get_songs(WORST_SONGS)
song = songs[8]
song, artist, year, info, wiki, youtube = get_songinfo(WORST_SONGS, song)

print("\nThese are all the titles in the Python list:")
print songs
print("\nThis is one selected title from that list:")
print song
print("\nThese values came from one row in the data file:")
print song, artist, year, info, wiki, youtube
'''



if __name__ == '__main__':
    app.run(debug=True)
