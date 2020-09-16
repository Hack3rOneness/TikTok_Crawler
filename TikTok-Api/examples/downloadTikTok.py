from TikTokApi import TikTokApi
# Starts TikTokApi
api = TikTokApi()

# Below is if you have a DIRECT tiktok url
tiktokData = api.get_Video_By_Url("https://www.tiktok.com/@ceciliaannborne/video/6817602864228207878", return_bytes=1)

# Below is used if you have the download url from the tiktok object, but maybe not the full object
tiktokData = api.get_Video_By_DownloadURL(api.trending(count=1)[0]['video']['downloadAddr'])

# Below is if the method used if you have the full tiktok object
tiktokData = api.get_Video_By_TikTok(api.trending(count=1)[0])

with open("video.mp4", 'wb') as out:
    out.write(tiktokData)