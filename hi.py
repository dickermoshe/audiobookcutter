import os
import eyed3
os.mkdir('out')

x = [i  for i in os.listdir() if i[-3:].lower() == 'mp3']

for s in x:
    album = s[:-4]
    try:
        duration = eyed3.load(s).info.time_secs
    except:
        continue
    
    for i in range(1,int(duration//1200)+1):
        start = str(i*1200-1200)
        end = str(i*1200)
        print(f'ffmpeg -i "{s}" -vn -acodec copy -ss {start} -to {end} "./out\\{album}{i}.mp3"')    
        os.system(f'ffmpeg -i "{s}" -vn -acodec copy -ss {start} -to {end} "./out\\{i}{album}.mp3"')
        audiofile = eyed3.load(f"./out\\{i}{album}.mp3")
        audiofile.tag.album = album
        audiofile.tag.track_num = i

        audiofile.tag.save()
        last=i
   
    os.system(f'ffmpeg -i "{s}" -vn -acodec copy -ss {end}  "./out\\{last+1}{album}.mp3"')
    audiofile = eyed3.load(f"./out\\{last+1}{album}.mp3")
    audiofile.tag.album = album
    audiofile.tag.track_num = last+1

    audiofile.tag.save()
            
