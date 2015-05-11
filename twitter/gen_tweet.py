#!/usr/bin/env python
# -*- coding: utf-8 -*-

from botutils import images as Image

def gen_response(status):
    text = ""

    if "where am i" in status.text.lower():
        if status.location():
            text = "Never fear, you are here:"
        else:
            text = "¯\_(ツ)_/¯ . Maybe verify location is enabled for tweets and ask again https://twitter.com/youareherebot/status/597616083386781696? Or, uh, just look around?"
    else:
        text = "You're doing it wrong. Try checking out this tweet for directions: https://twitter.com/youareherebot/status/597616083386781696"

    return text

def get_street_view(status):
    # Image opts
    x = 600
    y = 400
    # fov = 90
    heading = 280
    pitch = -70

    url = "https://maps.googleapis.com/maps/api/streetview?size={0}x{1}".format(x,y)

    if status.is_exact_location():
        url += "&location={0},{1}".format(*status.location())
    else:
        url += "&location={0}".format(status.location())

    url += "&heading={0}&pitch={1}".format(heading, pitch)

    print "Getting image from {0}".format(url)

    img = Image.get_image_from_url(url)
    img_path = Image.save_and_get_image_path(img)

    return img_path
