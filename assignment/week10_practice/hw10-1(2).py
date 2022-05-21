# 2017110292 김지완

lyrics = "Half of my heart is in Havana"
lyrics_list = list(lyrics.split())

tups_list = [ (char, len(char)) for char in lyrics_list ]

print(tups_list)