from __future__ import unicode_literals
from ytdl import youtube_dl
import pprint

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(d)
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'nocheckcertificate': False,
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=Ihb7odWK5uQ'])

