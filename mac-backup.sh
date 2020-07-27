#!/bin/sh
#error on desktop
rsync -avrzuR ~/./Documents/dev/ /Volumes/media-backup/mac-backup/ 2> "$(date +%Y-%m-%d_%H-%M-%S.txt)"
