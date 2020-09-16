from django.shortcuts import render
from TikTokApi import TikTokApi
from django.http import HttpResponse
import requests
import asyncio
import os
import csv
import pandas
import urllib

workpath = os.path.dirname(os.path.abspath(__file__))


api = TikTokApi()      #Tiktok Api Initialisation

#Debug -------------------------------
#loop = asyncio.new_event_loop()
#asyncio.set_event_loop(loop)
#Debug -------------------------------


details = [
    {
        'author': '',
        'title': 'TikTok Live Dashboard',
        'content': 'TikTok Dumped Data',
        'date_posted': 'Jun 29, 2020'
    },
]

#Home page

def home(request):
    context = {
        'details': details
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'About': 'About'})

#TikTok Trending Data

def trend(request):
    c = open(os.path.join(workpath, 'Crawled_Data/Tiktok_craler_trending.csv'),'r', newline='\n')
    reader = csv.reader(c, delimiter='#', quotechar='|')
    Trend = []
    rownum = 0
    for row in reader:
        if rownum != 0:
            Trend.append(row)
        rownum += 1
        
    c.close()

#trending=requests.get("https://google.com")
#Create a script to open file to dump in a local file then open file
#to print to the html file here
#script of dumping data in write mode to txt file -----  
#  ------>   openfile in readd mode to print

    return render(request, 'blog/trend.html',{'Trend':Trend})

#Tiktok Username data

def user_name(request):

    '''
    api = TikTokApi() 
    count = 30

    tiktoks = api.byUsername('americanredcross', count=count)

    for UserName in tiktoks:
        print(UserName)
    '''
    a = open(os.path.join(workpath, 'Crawled_Data/user_id.csv'),'r')
    reader = csv.reader(a,delimiter='\n')
    user_id = []
    rownum = 0
    for row in reader:
        if rownum != 0:
            user_id.append(row)
        rownum += 1
        
    a.close()
    return render(request, 'blog/user_name.html', {'user_id': user_id})

#data using usernames

def hastags(request):
    api = TikTokApi()
    count = 10
    '''
    tiktoks = api.byHashtag('funny', count=count)
    for tiktok in tiktoks:
        print(tiktok)
    '''
    a = open(os.path.join(workpath, 'Crawled_Data/hashtags.csv'),'r')
    reader = csv.reader(a,delimiter='\n')
    Hashtag = []
    rownum = 0
    for row in reader:
        if rownum != 0:
            Hashtag.append(row)
        rownum += 1
        
    a.close()

    return render(request, 'blog/hastags.html', {'Hashtag': Hashtag})

#getting data from a mp4 file

def mp3_data(request):
    count = 10
    '''
    # You can find this from a tiktok getting method in another way or find songs from the discoverMusic method.
    soundId = '6601861313180207878'

    tiktoks = api.byUsername(soundId, count=count)

    for tiktok in tiktoks:
        print(tiktok)
    '''
    a = open(os.path.join(workpath, 'Crawled_Data/mp3_data.csv'),'r')
    reader = csv.reader(a,delimiter='\n', quotechar='|')
    Mp3_data = []
    rownum = 0
    for row in reader:
        if rownum != 0:
            Mp3_data.append(row)
        rownum += 1

    a.close()
    return render(request, 'blog/mp3_data.html', {'Mp3_data': Mp3_data})

#Getting data from user

def user_video(request):

    result = 10
    '''
    userPosts = api.userPosts("6745191554350760966", "MS4wLjABAAAAM3R2BtjzVT-uAtstkl2iugMzC6AtnpkojJbjiOdDDrdsTiTR75-8lyWJCY5VvDrZ", 30)

    for tiktok in userPosts:
        print(tiktok['desc'])

    print(len(userPosts))
    '''
    a = open(os.path.join(workpath, 'Crawled_Data/Discover_in_Tiktok.csv'),'r')
    reader = csv.reader(a,delimiter='\n', quotechar='\n')
    user_video = []
    rownum = 0
    for row in reader:
        if rownum != 0:
            user_video.append(row)
        rownum += 1
        
    a.close()
    return render(request, 'blog/user_video.html', {'user_video': user_video })    

#Fetching Complete datasets
def all_data(request):
    '''
    trendingMusic = api.discoverMusic()

    for tiktok in trendingMusic:
        print(tiktok)

# Gets array of trending challenges (hashtags)
    trendingChallenges = api.discoverHashtags()

    for tiktok in trendingChallenges:
        print(tiktok)
    '''
    a = open(os.path.join(workpath, 'Crawled_Data/complete_video_dataset.csv'),'r')
    reader = csv.reader(a,delimiter='\n', quotechar='\n')
    AllData = []
    rownum = 0
    for row in reader:
        if rownum != 0:
            AllData.append(row)
        rownum += 1
    a.close()
    return render(request, 'blog/all_data.html', {'AllData': AllData})

#Download video 
def download_video(request):
    file_name = []
    file_name = input("Enter an url:")
    
    return render(request, 'blog/download_video.html', {'file_name': file_name})
