
from ..util import cmd


def update_copyright(src, app_config):
    if app_config['BIN']['EXIFTOOL'] == None:
        print("exiftool does not exist. Please install it.")
        return
    artist = app_config['COPYRIGHT']['ARTIST']
    notice = app_config['COPYRIGHT']['COPYRIGHTNOTICE']
    copy_right = app_config['COPYRIGHT']['COPYRIGHT']
    usage_term = app_config['COPYRIGHT']['USAGETERM']
    TOOL_CMD = r"{} "
    OPT_ARTIST = r'-artist="{}" '
    OPT_NOTICE = r"-d %Y -IPTC:CopyrightNotice'<© $createdate {}' "
    OPT_COPYRIGHT = r"-Copyright'<© $CreateDate {}' "
    OPT_USAGE = r'-usageterms="{}" -r -P -progress -overwrite_original {}'
    cmd_all = TOOL_CMD.format(app_config['BIN']['EXIFTOOL']) + \
                OPT_ARTIST.format(artist) + \
                OPT_NOTICE.format(notice) + \
                OPT_COPYRIGHT.format(copy_right) + \
                OPT_USAGE.format(usage_term, src)
    cmd.execute_cmd(cmd_all, shell=True)


def remove_tags_from_flickr(src, app_config):
    #exiftool * .jpg - Software = -SerialNumber = -LensSerialNumber = -InternalSerialNumber = -CameraID =

    TOOL_CMD = r"{} "
    OPT_SOFTWARE = r'-Software= '
    OPT_SNUM = r'-SerialNumber= '
    OPT_LENSSNUM = r'-LensSerialNumber= '
    OPT_ISNUM = r'-InternalSerialNumber= '
    OPT_CID = r'-CameraID= '
    SRC = "-P -overwrite_original {}".format(src)
    cmd_all = TOOL_CMD.format(app_config['BIN']['EXIFTOOL']) + \
        OPT_SOFTWARE + OPT_SNUM + OPT_LENSSNUM + \
        OPT_ISNUM + OPT_CID + SRC
    cmd.execute_cmd(cmd_all, shell=True)
