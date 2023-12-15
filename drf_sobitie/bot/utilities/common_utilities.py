import urllib.request

import emoji


def emojify_text(text, my_moji, surround: bool = False):
    if not surround:
        return f"{emoji.emojize(my_moji)} {text}"
    return f"{emoji.emojize(my_moji)} {text} {emoji.emojize(my_moji)}"


def read_photo_url(image_url: str):
    return urllib.request.urlopen(image_url).read()
