import os, shutil
from info import Beat
    
# moves files to new folder
def clean(files):
    wav = files[0]
    a = wav.split('/')
    b = a[1].split('.wav')
    c = b[0].split('"')
    title = f'{c[0]} Type Beat "{c[1]}"'
    os.mkdir(f'/Users/almoni/Desktop/Music/my_beats/{title}')
    for f in files:
        # save fl studio project
        if f.endswith('.flp'):
            shutil.copy(f, f'/Users/almoni/Desktop/Music/projects/{title}')    
            print('fl project saved')
        shutil.copy(f, f'/Users/almoni/Desktop/Music/my_beats/{title}')
    print('files saved to new dir')

    # delete unneeded duplicates
    folder = 'content'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    os.mkdir('content/stems')