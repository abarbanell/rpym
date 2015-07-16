#!/bin/sh

# set up rpym

echo checking /etc/hosts for a valid statsd entry
grep statsd /etc/hosts
if [ $? -eq 0 ] 
then
	echo looks good.
else
	echo looks bad.
	exit 1
fi


sudo apt-get install python-pip
sudo pip install statsd




