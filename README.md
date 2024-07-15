
# uploadbeats

I made this script so that I could quickly upload hip-hop beats to YouTube and Beatstars. In the process I added some cool features that may be useful to other producers who are looking to automate some of the beatmaking process. 

Note: a lot of the variables, file paths, etc., need to be changed or adjusted to work on your local device; a lot of data was set assuming you were running the script on my mac lol. Furthermore, the `beatstars.py` file is not fully done, some of the selenium doesn't work, but it's close. 

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

youtube(wav, beat, thumb) 

clean(files)
```
Note: all relevant files must be stored in a folder titled `content` in the main directory. This is where all necessary files will be dumped and/or moved.

![Screenshot 2024-07-15 at 2 23 51 PM](https://github.com/user-attachments/assets/c17f9353-e517-4056-8355-c9f60a582c36)


## `zip()`
This function compresses your exported track stems into a `.zip` then deletes the stems, as they are no longer needed. If however, you are only uploading a `.wav` or `.mp3` you can skip this step by commenting out this function. 

## `unsplash(wav)`
Moving down the `main.py` file we have a function which accepts the audio path as a paremeter and makes an API call to unsplash, an image hosting website. Assuming the title of your beat has the title **(FREE FOR PROFIT) Youtube Survey Type Beat "Survey"** our `unsplash.py` script will make the API call using the title as a query and return an image for your beat:

![sq](https://github.com/user-attachments/assets/f7fc7ed9-4078-47d9-9cc4-fed8c4e8f2cb)

If you are not satisfied with the returned image you can enter "x" in the terminal and the call will be made again.

Also, this image was not the one actually returned from the query, but documentation can get a bit boring so I spiced it up. The actual query would return one of the following images (most likely):

![Screenshot 2024-07-15 at 2 30 23 PM](https://github.com/user-attachments/assets/bc2cb1f3-6c42-4dac-8ca2-f9184b44692f)

Note: the image returned can have an aspect ratio but the function cuts it into a 1:1 square. This is the image that you are displayed with so there isn't any fear that after cropping, you won't like the image. 

## thumbnail(img`
Alright, you have your thumbnail, but it's 1:1 which is is fine for Beatstars which has square thumbnails, but for YouTube we need 16:9 aspect ratio.

`thumbnail(img)` is responsible for making the thumbnail for YouTube. It works by finding dominant colors in the returned image and creating a backdrop that matches the returned image, while also adding a border and some filters to the image. 

Then we upload to Beatstars using a Selenium script in `beatstars(wav, stems, sq)`.

After that 


