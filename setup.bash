#!/bin/bash

mkdir -p ~/.local/bin
# Ensure Flathub is enabled
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.discordapp.Discord com.valvesoftware.Steam com.visualstudio.code -y

