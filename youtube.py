import os
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
from simple_youtube_api.YouTube import YouTube
from info import Beat

def youtube(wav, beat, img):
    # turn wav into youtube title
    a = wav.split('/')
    b = a[1].split('.wav')
    c = b[0].split('"')
    title = f'(FREE FOR PROFIT) {c[0]}"{c[1]}"'

    # photo credz 
    if os.path.isfile('unsplash.txt'):
        f = open('unsplash.txt')
        lines = f.readlines()
        unsplash_link = lines[0]
        photographer = lines[1]

    # taglist
    hashtags = taglist(wav)

    # fix this info to get rid of unneccesary info.py
    bpm = Beat.bpm
    key = Beat.key
    link = Beat.link
    account = Beat.account
    # find out of there's an 'x' in name and make two seperate artist tags
    tags = Beat.yt_tags
    if os.path.isfile('unsplash.txt'):
        description = f"Checkout more beats here: {account}\n💰 buy 1 get 2 free, buy 2 get 5 free\n\n⚪ key {key}\n⚪ bpm {bpm}\n\nYou can use this beat on Youtube and Soundcloud for profit but a license is needed if you are uploading to Spotify, Apple Music, or other major streaming platforms. if you want to be sure that your song doesn't get taken down, or if your distributor requires a license for the beat, I recommend buying a lease: {link}\n\nPhoto by {photographer} here: {unsplash_link}\n\n{hashtags}"
    else:
        description = f"Checkout more beats here: {account}\n💰 buy 1 get 2 free, buy 2 get 5 free\n\n⚪ key {key}\n⚪ bpm {bpm}\n\nYou can use this beat on Youtube and Soundcloud for profit but a license is needed if you are uploading to Spotify, Apple Music, or other major streaming platforms. if you want to be sure that your song doesn't get taken down, or if your distributor requires a license for the beat, I recommend buying a lease: "

    # auth
    channel = Channel()
    channel.login("client_secret.json", "credentials.storage")

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=beat)

    # setting snippet
    video.set_title(title)
    video.set_description(description)
    video.set_tags(tags)
    video.set_category("music")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)

    # not safe for kids
    video.set_made_for_kids(False)

    # setting thumbnail
    video.set_thumbnail_path(img)

    # uploading video and printing the results
    try:
        video = channel.upload_video(video)
    except Exception as e:
        print(e)
    else: 
        if os.path.isfile('unsplash.txt'):
            # remove uneeded txt file
            os.remove('unsplash.txt') 
                
def taglist(wav):
    a = wav.split('/')
    b = a[1].split('.wav')
    c = b[0].split('"')

    # fix this, doesn't need the 'Type Beat' can add that later
    i = f'{c[0]} "{c[1]}"'
    j = i.split('Type')
    k = j[0].split(')')

    # if song has one artist
    t = k[0].lower()
   
    if 'x' in j:
        try:
            if 'x' in k[1]:
                t = k[1].split('x')
                tag1 = t[0].replace(" ", "").lower()
                tag2 = t[1].replace(" ", "").lower()
                return f"#{tag1} #{tag2} #trap #beats #freeforprofit #freeforprofitbeats #freebeats #rap"
            else:
                tag = k[1].replace(" ", "").lower()
                return f"#{tag} #trap #beats #freeforprofit #freeforprofitbeats #freebeats #rap"
        except:
            if 'x' in k[0]:
                t = k[0].split('x')
                tag1 = t[0].replace(" ", "").lower()
                tag2 = t[1].replace(" ", "").lower()
                return f"#{tag1} #{tag2} #beats #trap #freeforprofit #freeforprofitbeats #freebeats #rap"
    else:
        # add more adjectives to check
        if t.lower().startswith('sad'):
            adj = t.split(" ")
            tag1 = adj[0].replace(" ", "").lower()
            tag2 = adj[1].replace(" ", "").lower()
            return f"#{tag1} #{tag2} #beats #freeforprofit #freeforprofitbeats #freebeats #rap" 

        # # check if beat is lofi
        # elif t.lower().startswith('lofi'):
        #     return f"#{tag} #lofi #beats #freeforprofit #freeforprofitbeats #freebeats #rap" 
    tag = t.replace(" ", "")
    return f"#{tag} #beats #trap #freeforprofit #freeforprofitbeats #freebeats #rap" 
