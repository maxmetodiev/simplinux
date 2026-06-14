#!/bin/bash

TMP="/Downloads/discord.deb"

wget -O "$TMP" "https://discord.com/api/download?platform=linux&format=deb"

sudo dpkg -i "$TMP"
sudo apt -f install -y

rm "$TMP"