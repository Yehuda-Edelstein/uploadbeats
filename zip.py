import os, shutil

def zip():
    folder = 'content/stems'
    for f in os.listdir(folder):
        old = f
        stems = f.split('_', 1)
        if len(stems) > 0:
            f = stems[1]
        os.rename(f'{folder}/{old}', f'{folder}/{f}')
    print('rename stems')
    if os.path.exists(f'{folder}/Current.wav'):
        os.remove(f'{folder}/Current.wav')
    print('current stem deleted')
    shutil.make_archive('content/stems', 'zip', 'content/stems')
    print('zipfile made')
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print('extra stem wavs deleted')

