#!/bin/sh
filename=$(date +"%m-%d-%y|||%H%M%S")
fswebcam -r 1366x768 $filename.jpg
