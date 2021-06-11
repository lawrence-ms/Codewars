# https://www.codewars.com/kata/551dc350bf4e526099000ae5

def song_decoder(song):
    wub_check = False
    new_song = ""
    pos = 0
    while pos < len(song):
        if song[pos:pos+3] == "WUB":
            pos = pos + 2
            wub_check = True
        else:
            if wub_check:
                new_song += " " + song[pos]
                wub_check = False
            else:
                new_song += song[pos]
        pos += 1
    return new_song.lstrip()
    
