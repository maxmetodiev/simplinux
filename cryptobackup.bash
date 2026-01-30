#!/bin/bash

# Backup Bisq
cd ~/.local/share
if [ -d "Bisq" ]; then
	zip -r bisqbackup.zip Bisq
	mv bisqbackup.zip ~
else
	echo "Dir '.local/share/Bisq' does not exist"
fi

cd ~
# Backup Bitcoin
if [ -d ".bitcoin" ]; then
	cd .bitcoin
	if [ -f "wallet.dat" ]; then
		zip -r btcbackup.zip wallet.dat
		mv btcbackup.zip ~
	elif [ -d "wallets" ]; then
		zip -r btcbackup.zip wallets
		mv btcbackup.zip ~
	fi
else
	echo "Dir '.bitcoin' not found"
fi
cd ~

#Backup Monero
if [ -d ".monero" ]; then
	cd .monero
	if [ -d "wallets" ]; then
		zip -r xmrbackup.zip wallets
		mv xmrbackup.zip ~
	else
		echo "Dir 'wallets' not found"
	fi
else
	echo "Dir '.monero' not found"
fi
cd ~
