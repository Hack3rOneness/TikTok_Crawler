
# Unofficial TikTok API in Python

This is an unofficial api wrapper for TikTok.com in python. With this api you are able to call most trending and fetch specific user information.

 [![GitHub release (latest by date)](https://img.shields.io/github/v/release/davidteather/TikTok-Api)](https://github.com/davidteather/TikTok-Api/releases) [![Build Status](https://travis-ci.com/davidteather/TikTok-Api.svg?branch=master)](https://travis-ci.com/davidteather/TikTok-Api) [![GitHub](https://img.shields.io/github/license/davidteather/TikTok-Api)](https://github.com/davidteather/TikTok-Api/blob/master/LICENSE) [![PyPI - Downloads](https://img.shields.io/pypi/dm/TikTokApi)](https://pypi.org/project/TikTokApi/) [![Downloads](https://pepy.tech/badge/tiktokapi)](https://pypi.org/project/TikTokApi/)

If you want to use this API as a service visit the [RapidAPI](https://rapidapi.com/rapidapideveloper/api/tiktok2)


 Consider sponsoring me [here](https://github.com/sponsors/davidteather)

## Important Information
* If this API stops working for any reason open an issue.

## Getting Started

To get started using this api follow the instructions below.

### Installing

If you need help installing or run into some error, please open an issue. I will try to help out as much as I can.

```
pip install TikTokApi
pyppeteer-install
```

If you're running a virtual machine you need to install chromedriver for your machine globally. Download it [here](https://sites.google.com/a/chromium.org/chromedriver/) and add it to your path.


## Quick Start Guide

Here's a quick bit of code to get the most recent trending on TikTok. There's more example in the examples directory.


```
from TikTokApi import TikTokApi
api = TikTokApi()

results = 10

trending = api.trending(results)

for tiktok in trending:
    # Prints the text of the tiktok
    print(tiktok['desc'])

print(len(trending))
```
[Here's](https://gist.github.com/davidteather/7c30780bbc30772ba11ec9e0b909e99d) an example of what a tiktok dictionary looks like.

## Detailed Documentation

##### The TikTok class

```
TikTokApi(self, debug=False)
```

debug - Enable this if you need some more output.


##### The trending Method

```
# Where count is how many result you want
# Verbose is optional, default=0. Set it to 1 to get more information
api.trending(self, count=30, referrer="https://www.tiktok.com/@ondymikula/video/6756762109670477061")
```

count - this is how many trending Tiktoks you want to be returned.

Trending returns an array of dictionaries. Example structure [here](https://www.tiktok.com/@ondymikula/video/6756762109670477061)

##### The get_Video_By_TikTok Method

```
api.get_Video_By_TikTok(data)
```

data - The tiktok dictionary returned from the API. Will return bytes.


##### The bySound Method

This method returns an array of tiktoks based on a sound id.
```
def bySound(self, id, count=30)
```

id - the sound's id (you can get this from other methods)


##### The getUserObject Method

This method returns a user object, primarily used for other methods within the package.
```
def getUserObject(self, username)
```

username - the unique username of the person you want to get an object for.

##### The getMusicObject Method

This method returns a music object, primarily used for other methods within the package.

```
def getMusicObject(self, id)
```

id - the ID of the music.

##### The getHashtagObject Method

This method returns a hashtag (challenge) object, primarily used for other methods within the package.

```
def getHashtagObject(self, hashtag)
```

hashtag - the hashtag or challenge name

##### The byUsername Method

This method returns an array of tiktoks by a username

```
def byUsername(self, username, count=30)
```

##### The byHashtag Method

This method returns an array of TikToks by a given hashtag or challenge (without the #)

```
def byHashtag(self, hashtag, count=30)
```

hashtag - a given hashtag or challenge without the #

##### The discoverMusic Method

Returns trending music shown on the side at tiktok's trending page on desktop

```
def discoverMusic(self)
```

##### The discoverHashtags Method

Returns trending hashtags (challenges) shown on the side at tiktok's trending page on desktop

```
def discoverHashtags(self)
```

##### The get_Video_By_DownloadURL Method

```
api.get_Video_By_DownloadURL(url)
```

url - The download url that's found in the TikTok dictionary. TikTok['video']['downloadAddr']


##### The get_Video_By_Url Method

```
api.get_Video_By_Url(video_url, return_bytes=0)
```

video_url - The video you want to get url.

return_bytes - The default value is 0, when it is set to 1 the function instead returns the bytes from the video rather than just the direct url.

## Built With

* [Python 3.7](https://www.python.org/) - The web framework used

## Authors

* **David Teather** - *Initial work* - [davidteather](https://github.com/davidteather)

See also the list of [contributors](https://github.com/davidteather/TikTok-Api/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
