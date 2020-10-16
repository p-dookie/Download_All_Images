import requests
import shutil
def dp(url, path):
    filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        shutil.move(filename, path")
        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Could not be retreived')
