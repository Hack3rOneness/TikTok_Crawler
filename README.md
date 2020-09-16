# TikTok_Crawler
A Python Based Crawler written in Django(UI). 

## Project Description : 
- Project was developed under ```Cyber Peace Foundation``` [![Twitter](https://img.shields.io/badge/Twitter-Cyber%20Peace%20Foundation-blue?style=social&logo=appveyor)](https://twitter.com/cyberpeacengo) the abstract of this project was do analysis on live streamed "TikTok" data for we called an Api (TikTok-Api).
- The project is fully written in Djang-Framework (UI).
- ### Why we choose Django??
  - As we all know lot's of good things about the Django-Framework as it works on Python, we can create a complete project envirnoment with django.

- ### What did I used for web scraping??
  - I nothing used like ```Scapy```, ```BeautifulSoap``` or other, as we know this was an prototype of our ideology so We wanted to implements our idea behind this project. 

- ### Features available!!!
  - I added some interesting features like : 
    - Fetch Raw data from Tiktok Server.
    - Trending Feeds
    - Comments
    - Public profiles
    - Trending Videos url
    - Descriptions etc.

- ### Screenshots :
- [![HomePage][img-1]][img-1]
- [![About][about]][about]
- [![trend][trend]][trend]
- [![user-name][user-name]][user-name]
- [![hashtag][hashtag]][hashtag]
- [![mp3-data][mp3-data]][mp3-data]
- [![video][video]][video]
- [![download][download]][download]
- [![login][login]][login]

- ### Setting up environment : Follow the complete tutorial for Django [here](https://docs.djangoproject.com/en/1.8/howto/windows/#:~:text=Django%20can%20be%20installed%20easily,version%20in%20the%20command%20prompt.)
    - #### Install Django by running this command : 
        - On Windows Download Binary Executable file from it's official website [Docs.Djangoproject.com](https://python.org/download/).
        - Add this ```C:\Python34\;C:\Python34\Scripts;``` PATH In system environment.
    - #### Install with Setuptool : 
        - Install latest version of setuptool from [SetupTool](https://pypi.python.org/pypi/setuptools)
    - #### Install PIP : 
        - Open a command prompt and execute easy_install pip. This will install pip on your system. This command will work if you have successfully installed Setuptools.
    - #### Install Django :
        - ```pip install django```
        - Run this command in cmd ```django-admin --version```
    - #### In linux running commands are same as above but need to add proxy path in such way :
        - set http_proxy=http://username:password@proxyserver:proxyport
        - set https_proxy=https://username:password@proxyserver:proxyport
- ### Install this project :
  - git clone https://github.com/Hack3rOneness/TikTok_Crawler.git
  - cd TikTok_Crawler
  - cd TikTok-Api
  - build setup.py
  - cd ../
  - python manage.py runserver
  - Open browser enter this address [localhost](http://127.0.0.1:8000) you must see the complete project.

[![Custom badge][Insta-shield]][Insta-me]
[![LinkedIn][linkedIn-shield]][linkedin-url]
[![contributor][contributor]][contributor] [![GitHub issues](https://img.shields.io/github/issues/Hack3rOneness/TikTok_Crawler?style=plastic)](https://github.com/Hack3rOneness/TikTok_Crawler/issues) [![GitHub forks](https://img.shields.io/github/forks/Hack3rOneness/TikTok_Crawler?style=plastic)](https://github.com/Hack3rOneness/TikTok_Crawler/network) [![GitHub stars](https://img.shields.io/github/stars/Hack3rOneness/TikTok_Crawler?style=plastic)](https://github.com/Hack3rOneness/TikTok_Crawler/stargazers)

[linkedin-url]: https://www.linkedin.com/in/sumit-o-a30926158
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[NHC-JOIN-shield]: https://img.shields.io/badge/NHC-Join%20Us-cyan?style=plastic&logo=appveyor
[Insta-shield]: https://img.shields.io/badge/~Hack3r__Oneness-Instagram-02f5ff?style=plastic&logo=appveyor
[Insta-me]: https://instagram.com/hack3r_oneness 
[contributor]: https://img.shields.io/badge/Contributor-Lalit-brightgreen?style=plastic&logo=appveyor
[img-1]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(265).png
[about]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(266).png
[trend]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(267).png
[user-name]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(268).png
[hashtag]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(269).png
[mp3-data]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(270).png
[video]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(271).png
[download]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(272).png
[login]:https://github.com/Hack3rOneness/TikTok_Crawler/blob/master/Screenshots/Screenshot%20(273).png
