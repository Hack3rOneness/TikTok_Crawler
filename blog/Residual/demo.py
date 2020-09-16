from TikTokApi import TikTokApi
from TikTokApi import *
api = TikTokApi()

result = 10

trending = api.trending(result)

for tiktok in trending:
	print(tiktok['desc'])
print(len(trending))

