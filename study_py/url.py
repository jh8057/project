from urllib.request import urlopen

url = 'http://www.python.org'
with urlopen(url) as f:
	doc = f.read().decode()
	print(doc)