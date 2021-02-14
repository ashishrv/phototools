
from unipath import Path

from .cmd import get_cmd_otput

def get_resolution(src, app_config):
    width, height = 0, 0
    src_p = Path(src)
    cmd_all = r"{} -p '$XResolution,$YResolution' '{}'".format(
        app_config['BIN']['EXIFTOOL'], src_p)
    if src_p.exists() and src_p.isfile:
        w, h = get_cmd_otput(cmd_all).split(',')
        return int(w), int(h)
    return width, height


def get_size(src, app_config):
    width, height = 0, 0
    src_p = Path(src)
    cmd_all = r"{} -p '$ImageWidth,$ImageHeight' '{}'".format(
        app_config['BIN']['EXIFTOOL'], src_p)
    if src_p.exists() and src_p.isfile:
        w, h = get_cmd_otput(cmd_all).split(',')
        return int(w), int(h)
    return width, height
