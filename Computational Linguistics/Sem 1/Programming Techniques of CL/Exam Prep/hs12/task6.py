song = ["I", "scream", "you", "scream", "we", "all", "scream", "for", "ice", "Cream"]

#task a
print(len(set(song)))

#task b
song[-1] = song[-1].lower()
print(song)

#task c
song_three = song*3
print(song_three)

#task d
for word in song:
    if word == "I":
        song[song.index(word)] = "you"
print(song)

#task e
for i in range(len(song)):
    if i % 2 == 0:
        print(song[i])  
        
#task f
song2 = [word.upper() for word in song]
print(song2)

#task g
enum = [(word, len(word)) for word in song]
print(enum)
