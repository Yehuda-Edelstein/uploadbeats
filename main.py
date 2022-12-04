import os
import tempfile
from video import make_video, add_audio
from youtube import youtube
from clean import clean
from zip import zip
from thumbnail import thumbnail
from unsplash import unsplash
# from beatstars import beatstars

video = 'content/video.mp4'
beat = 'content/beat.mp4'
stems = 'content/stems.zip'
thumb = 'content/thumb.png'
sq = 'content/sq.png'
img = 'content/img.png'
# gif = 'content/img.gif'

for f in os.listdir('content'):
    if f.endswith('.wav'):
        wav = f'content/{f}'
    elif f.endswith('.flp'):
        project = f'content/{f}'
        
files = [wav, stems, thumb, sq]

# get bpm and key from stems possibly

# zip()

# unsplash(wav)

thumbnail(img)

beatstars(wav, stems, sq)

# create txt file (then wipe it) with beat info for youtube either here or within beatstars()
  
make_video(wav, thumb)

add_audio(wav, video)

try:
    youtube(wav, beat, thumb) 
except Exception as e:
    print(e)
else:
    clean(files)

