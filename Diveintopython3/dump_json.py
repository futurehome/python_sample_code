import httplib2

import time

entry = {
    'comments_link': None,
    'internal_id': b'\xDE\xD5\xB4\xF8',
    'title': 'Dive into history, 2009 edition',
    'tags': ('diveintopython', 'docbook', 'html'),
    'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
    'published_date': time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1),
    'published': True
}

import json
def to_json(python_object):
    if isinstance(python_object, time.struct_time):
        return {
            '__class__': 'time.asctime',
            '__value__': time.asctime(python_object)
        }
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes', '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')

with open('entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f, default=to_json, indent=4)