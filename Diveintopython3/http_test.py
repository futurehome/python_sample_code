import httplib2
import chardet

httplib2.debuglevel = 1
h = httplib2.Http('.cache')
response, content = h.request('http://www.diveintopython3.net/examples/feed.xml')