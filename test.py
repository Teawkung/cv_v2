import requests
def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': 'test'}
    return _lineNotify(payload,file)

def sendline(msg,t):
	
	url='https://notify-api.line.me/api/notify'
	token='Y7ebrnmGTt9w7h2I45vp6OuhkHeCGwNKTfKy8SBmaLZ'
	headers={'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
	r = requests.post(url, headers=headers, data = {'message':msg})
	d = requests.post(url, headers=headers, data = {'message':t})
	print (r.text)
	print (d.text)
def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)
	