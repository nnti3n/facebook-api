import requests

post_id = ""
access_token = ""
template = "https://graph.facebook.com/v2.4/%s?fields=likes&access_token=%s"
url = template % (post_id, access_token,)
likes = []
first = True
while 1:
    r = requests.get(url)
    result = r.json()
    print (result)
    if first:
        page_likes = result['likes']
        first = False
    else:
        page_likes = result
    print (page_likes['data'])
    likes += page_likes['data']
    if page_likes and 'next' not in page_likes['paging']:
        break
    url = page_likes['paging']['next']

fp = open("%s_likes.csv" % post_id, "w")

fp.write("Name,Profile Link\n")
for liker in likes:
    fp.write("https://facebook.com/" + liker['id'] + "\n")
fp.close()
