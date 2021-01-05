import os
import eyed3
def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)

x = [i for i in mp3gen()]
for s in x:
    album = s[:-4]
    duration = eyed3.load(s).info.time_secs
    for i in range(1,int(duration//1200)+1):
        start = str(i*1200-1200)
        end = str(i*1200)
        print(f'ffmpeg -i "{s}" -acodec copy -ss {start} -to {end} "./out\\{album}{i}.mp3"')    
        os.system(f'ffmpeg -i "{s}" -acodec copy -ss {start} -to {end} "./out\\{album}{i}.mp3"')
        audiofile = eyed3.load(f"./out\\{album}{i}.mp3")
        audiofile.tag.album = album[2:]
        audiofile.tag.track_num = i

        audiofile.tag.save()
        last=i
   
    os.system(f'ffmpeg -i "{s}" -acodec copy -ss {end}  "./out\\{album}{last+1}.mp3"')
    audiofile = eyed3.load(f"./out\\{album}{last+1}.mp3")
    audiofile.tag.album = album
    audiofile.tag.track_num = last+1

    audiofile.tag.save()
            
