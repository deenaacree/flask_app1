from flask import Flask, render_template
app = Flask(__name__)

from worst_songs import WORST_SONGS

source = WORST_SONGS

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


# to do song=song in the page function, it says I need to define the variable song globally
for row in source:
    song = row["Song Title"]


# find the row that matches the song name, retrieve artist, year, info, and links for that title
def get_songinfo(source, page):
    for row in source:
        if song == row["Song Title"]:
            artist = row["Artist"]
            year = row["Year"]
            info = row["Information"]
            wiki = row["Wikipedia Link"]
            youtube = row["YouTube Link"]
    return song, artist, year, info, wiki, youtube


@app.route('/')
def index():
    return render_template('list.html')
get_songs(WORST_SONGS)


@app.route('/songs/<song>')
def page():
    return render_template('song.html', songs=songs)
get_songinfo(WORST_SONGS, song)


# the code below works
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
