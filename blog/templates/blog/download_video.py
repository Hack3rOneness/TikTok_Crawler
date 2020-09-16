import requests, urllib

    
def download(requests):
    file_name=requests.get("http://wnget.com/uapi/tiktok/post?user_id=6691366574592396038")
    with open("video.mp4", 'wb') as out:
        out.write(file_name)
    
    return file_name



