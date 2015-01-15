# for python 2.7
# requires eyed3: http://eyed3.nicfit.net/installation.html
# renames directories containing a media file with Artist - Album. So, "foo\song.mp3" will be renamed to "Artist - Album\song.mp3"

import os
import sys
import eyed3
import time
import string

directoryPath = sys.argv[1] if sys.argv[1].endswith('\\') else sys.argv[1] + '\\'
redundantIncrement = 0
valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

for dir in os.listdir(directoryPath):
	albumPath = os.path.join(directoryPath, dir)
	subdir = os.listdir(albumPath)
	if (len(subdir) > 0):
		firstMp3 = next(m for m in subdir if m.endswith(('.mp3','.flac','.m4a'), None))
		if (firstMp3 != None):
			tag = eyed3.load(os.path.join(albumPath, firstMp3))
			if (tag != None and tag.tag != None and tag.tag.artist != None and tag.tag.album != None):
				print "----------------------"
				friendlyAlbumName = tag.tag.artist.encode('UTF-8') + " - " + tag.tag.album.encode('UTF-8')
				friendlyAlbumName = ''.join(c for c in friendlyAlbumName if c in valid_chars)
				friendlyAlbumPath = os.path.join(directoryPath, friendlyAlbumName)
				friendlyAlbumPath = friendlyAlbumPath if friendlyAlbumName not in os.listdir(albumPath) else ''.join(friendlyAlbumPath,'_',str(++redundantIncrement))
				print friendlyAlbumPath
				os.rename(albumPath, friendlyAlbumPath)