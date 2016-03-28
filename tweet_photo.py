#!/usr/bin/env python
# tweetpic.py take a photo with the Pi camera and tweet it
# Adapted from code by Alex Eames http://raspi.tv/?p=5918

import os
import sys

import tweepy

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']


def main(argv):
    if len(argv) != 2:
        raise RuntimeError('Usage: {} <path to motion capture photo>'.format(
            argv[0]))

    photo_filename = argv[1]

    api = get_authenticated_api()

    status = ""
    api.update_with_media(photo_filename, status=status)


def get_authenticated_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)

if __name__ == '__main__':
    main(sys.argv)
