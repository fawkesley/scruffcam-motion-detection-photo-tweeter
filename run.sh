#!/bin/sh -ex

THIS_DIR=$(dirname $0)

. ${THIS_DIR}/credentials.sh
. ${THIS_DIR}/venv/bin/activate

exec ${THIS_DIR}/tweet_photo.py $*
