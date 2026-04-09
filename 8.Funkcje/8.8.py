#8.8
print("\n8.8")

def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist name': artist_name, 'album_title': album_title}
    
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album

while True:
    singer = input("Who is your favorite singer? ").lower()
    if singer == 'q':
        break
    song = input("What is your favorite album of that singer? ").lower()
    if song == 'q':
        break
    musician = make_album(singer, song)
    print(musician)
    print("Press 'q' to leave the program.")