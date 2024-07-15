
# uploadbeats

I made this script so that I could quickly upload hip hop beats to youtube and beatstars. In the process I added some cool features that may be useful to other producers who are looking to automate some of the beatmaking process. 

A lot of the variables, file paths, etc., need to be changed or adjusted to work on your local device; a lot of data was set assuming you were running the script on my mac lol.



The `beatstars.py` file is not fully done, some of the selenium doesn't work, but it's close. 


# How it works
Once you have a `.wav` for your beat (or `.mp3`) you can run the script with:
```
python main.py
```
This file executes these other functions in this order:
```
zip()

unsplash(wav)

thumbnail(img)

beatstars(wav, stems, sq)

make_video(wav, thumb)

add_audio(wav, video)

try:
    youtube(wav, beat, thumb) 
except Exception as e:
    print(e)
else:
    clean(files)
```
Note: initially the script was intended for people exporting all track stems for a beat, but if you are only exporting a `.wav` you can comment out the `zip.py` function. Also the files must be stored in a folder titled `content` in the main directory. This is where all necessary files will be dumped and moved.

Moving down the `main.py` file we have `unsplash(wav)` which accepts the audio path. Assuming the title of your beat has the name **(FREE FOR PROFIT) Drake X Lil Baby Type Beat "Sauce"** `unsplash.py` will make an API call to unsplash using the title of the beat as input in a search returning a thumbnail for your beat. If you are not satisfied with the returned image you can enter "x" in the terminal and the call will be made again.

Once you have your thumbnail; as of now it is just an image 1:1 which is fine for Beatstars which has square thumbnails, but for YouTube...

`thumbnail(img)` is responsible for making the thumbnail for YouTube. It works by finding dominant colors in the returned image and creating a backdrop that matches the returned image, while also adding a border and some filters to the image. 

Then we upload to Beatstars using a Selenium script in `beatstars(wav, stems, sq)`.

After that 


