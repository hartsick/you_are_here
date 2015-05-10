from botutils import images as Image

def gen_response(status):
    text = ""

    if "where am i" in status.text.lower():
        if status.location():
            text = "Never fear, you are here:"
        else:
            text = "Location is screwed up. Maybe just look around?"
    else:
        text = "You're doing it wrong."

    return text

def get_street_view(lng, lat):
    # Image opts
    x = 600
    y = 400
    fov = 90
    heading = 235
    pitch = 10

    url = "https://maps.googleapis.com/maps/api/streetview?size={0}x{1}".format(x,y)
    url += "&location={0},{1}".format(lat, lng)
    url += "&fov={0}&heading={1}&pitch={2}".format(fov, heading, pitch)

    print "Getting image from {0}".format(url)

    img = Image.get_image_from_url(url)
    img_path = Image.save_and_get_image_path(img)

    return img_path
