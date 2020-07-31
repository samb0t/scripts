#!/bin/sh

# Run this in crontab

# errors on desktop
# fix hidden files on target ntfs with --inplace
# no -z (compression) to speed it up

src_paths=(
    "$HOME/./Calibre Library/"
    "$HOME/./Documents/"
    "$HOME/./Movies/"
    "$HOME/./Music/"
    "$HOME/./Pictures/"
    "$HOME/./Splice/"

    "$HOME/./Library/Pioneer/"
    "$HOME/./Library/Audio/"
    "$HOME/./Library/Application Support/Ableton/"
    "$HOME/./Library/Application Support/Cycling '74/"
    "$HOME/./Library/Application Support/Pioneer"

    "/Library/Audio/"
    "/Library/Application Support/Native Instruments/"
)

root_dest="/Volumes/media-backup/mac-backup/"
error_file="$HOME/Desktop/$(date +%Y-%m-%d.txt)"

for i in "${src_paths[@]}"
do
    dest=$root_dest

    if  [[ $i == /Users* ]] ;
    then
        dest+="User/"
    fi

    rsync -avruR --inplace "$i" "$dest" 2> "$error_file"
done

if [ -f "$error_file" ] && [ ! -s "$error_file" ]
then
    echo "No errors; removing error file"
    rm "$error_file"
fi
