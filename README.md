
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

## `beatstars(wav, stems, sq)`
Then we upload to Beatstars using a Selenium script in the `beatstars(wav, stems, sq)` function. The function isn't totally done, some of the uploading process still needs to be done manually, but if you're only interested in uploading to YouTube...?

## `thumbnail(img)`
Alright, you have your thumbnail, but it's 1:1 aspect ratio, which is is fine for Beatstars who require square thumbnails, but for YouTube we need aspect ratio of 16:9. This function works by finding the most dominant color in the returned image and creating a backdrop (with the correct aspect ratio) that matches the returned image, while also adding a border and some filters to the square image itself that is superimposed over the backdrop. Sounds complicated, but is actually very simple.

Now we have:

![thumb](https://github.com/user-attachments/assets/1a53b7e6-6381-4ae8-9a20-ce7daa807fb6)

## `make_video(wav, thumb)`
This function creates an `.mp4` with the thumbnail as a background for as long as the beat is.

## `add_audio(wav, video)`
Then we add the audio.

## `youtube(wav, beat, thumb)`
Then we access YouTube's API to upload the entire video to whatever YouTube channel you want (remember you will need an API key).

And lastly...

## `clean(files)`
We clean all the files so that we can do it all over again.

**You can find the official video here: https://www.youtube.com/watch?v=3CdIAIDSi5U**
