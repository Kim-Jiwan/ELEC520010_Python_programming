lyrics = "Half of my heart is in Havana"
lyric_list = (lyrics.split())

tup_list = [ (lyric, len(lyric)) for lyric in lyric_list ]
print(tup_list)