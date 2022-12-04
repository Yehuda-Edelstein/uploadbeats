import requests
import psutil
import time
from PIL import Image
import os

from pyunsplash import PyUnsplash

# unsplash info
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

def unsplash(wav):
    # get beat title
    q = ''

    # access api 
    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)

    # query photo
    photos = pu.photos(type_='random', count=1, featured=True, query=f"{q}")
    [photo] = photos.entries

    # check to see if photo is trash
    id = photo.id
    nope = open("nope.txt", "r")
    if id in nope.read():
        print('trash!')
        unsplash(wav)

    response = requests.get(photo.link_download, allow_redirects=True)

    open('../unsplash_temp.png', 'wb').write(response.content)
    img = Image.open('../unsplash_temp.png')
    img.show()

    # kill image
    time.sleep(4)
    close()
    
    # is photo good?
    i = input('yay or nay: ').lower()

    if i == 'y' or i == 'yes' or i == 'yay':
        # add this id to a file so no pic gets reused
        id = photo.id
        used = open("used.txt", "r")
        if id in used.read():
            print('already used that one')
            unsplash(wav)
        else:
            with open('used.txt', "a+") as f:
                f.seek(0)
                data = f.read(100)
                if len(data) > 0:
                    # figure out why there's a blank line
                    f.write(f"\n{id}")
                # f.write(id)
            unsplash_link = f"https://unsplash.com/photos/{id}"
            photographer = photo.body["user"]["name"]
            # save photo
            img.save('content/img.png')
            print('photo retrieved from unsplash and saved')

            # create new txt file to hold photo data
            with open('unsplash.txt', 'w') as f:
                f.write(unsplash_link)
                f.write('\n')
                f.write(photographer)
    elif i == 'n' or i == 'no' or i == 'nay':
        print('not for this beat')
        unsplash(wav)
    elif i == 'x':
        id = photo.id
        with open('nope.txt', "a+") as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                # figure out why there's a blank line
                f.write(f"\n{id}")
                print('trash')
                unsplash(wav)


def close():
    # close photo
    for proc in psutil.process_iter():
        if proc.name() == "Preview":
            proc.kill()

