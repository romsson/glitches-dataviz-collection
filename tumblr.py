# -*- coding: utf-8 -*-
import pytumblr # https://github.com/tumblr/pytumblr/issues/77
import time
from requests import get
import json
import os

OUTPUT_IMAGES_DIR = "images/"

def credentials():
    with open("credentials.json") as file:
        credentials = json.load(file)    
    return credentials
    
def download(url, filename, directory):
        
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)     
    
    with open(directory + filename, "wb") as file:
        response = get(url);
        file.write(response.content);
        print(directory + filename, "downloaded")
        
def save(data, filename):
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=2)
        print(filename, "saved")

def fetch_tumblr():
    
    # From pytumblr API https://github.com/tumblr/pytumblr
    # Create a credentials.json file as follows
    # {
    #  "consumer_key": "XXXXXXXXXXXX7YSB5dYM3F3IpcSPPO4MkLg",
    #  "consumer_secret": "XXXXXXXXXXXXOSpC648SoZ3u0IUUwTARFc",
    #  "oauth_token": "XXXXXXXXXXXXXXXXXdOo2iBRbY",
    #  "oauth_secret": "XXXXXXXXXXXXXX60Xkbh5BcFrmP85zDsWCFSdM4YF"
    # }
    client = pytumblr.TumblrRestClient(credentials['consumer_key'], credentials['consumer_secret'], credentials['oauth_token'], credentials['oauth_secret']);

    result = []
    r = range(9)
    for off in r:
        posts = client.posts('accidental-art.tumblr.com', limit=20, offset=off, notes_info=True, filter='text')
        for p in posts['posts']:
            d = {};
            d['url'] = p['photos'][0]['alt_sizes'][0]['url'];
            d['filename'] = d['url'].strip().split('/')[-1].strip()
            d['text'] = p['summary'];
            d['source'] = 'tumblr';
            d['post_url'] = p['post_url'];
            download(d['url'], d['filename'], os.path.join(os.getcwd(), OUTPUT_IMAGES_DIR))
            time.sleep(2)
            result.append(d);
    return result

if __name__ == "__main__":
    credentials = credentials()
    collection = fetch_tumblr()
    save(collection, 'glitches.json')