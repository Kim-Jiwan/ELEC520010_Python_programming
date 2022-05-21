# 2017110292 김지완

lyrics = "Half of my heart is in Havana"
lyrics_list = list(lyrics.split())

tups_list = []

for char in lyrics_list:
    tups_list.append((char, len(char)))

print(tups_list)