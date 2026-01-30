#!/bin/bash

cd ~/.local/share
if [ -d "Bisq" ]; then
	zip -r bisqbackup.zip Bisq
	mv bisqbackup.zip ~
else
	echo "Dir '.local/share/Bisq' does not exist"
fi

cd ~
if [ -d ".bitcoin" ]; then
	zip -r dotbitcoin.zip .bitcoin
	mv dotbitcoin.zip ~
else
	echo "Dir '.bitcoin' does not exist"
fi
