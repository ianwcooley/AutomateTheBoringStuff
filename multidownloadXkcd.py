#! python3
# multidownloadXkcd.py - Downloads every single XKCD comic using 
# multiple threads

import requests, os, bs4, threading

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            try:
                res = requests.get(comicUrl)
                res.raise_for_status()
                # Save the image to ./xkcd.
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except Exception as error:
                print(f"An error occurred: {error}")

# Create and start the thread objects.
downloadThreads = []
for i in range(0, 2000, 100): # loops 20 times, creates 20 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
