

from unipath import Path, FILES

from ..util import cmd
from ..util import aspectratio


def resize_for_instagram(src, app_config):
    src_p = Path(src)
    src_name = src_p.name
    if 'Insta' in src_name or 'Nas' in src_name:
        return
    output_file = Path("{}/{}_Insta{}".format(src_p.parent, src_p.stem, src_p.ext))
    # we can also use: -unsharp 0.25x0.08+8.3+0.045
    cmd_all = "{} {} -resize 1048x -sharpen 0x.6  -colorspace sRGB -strip '{}'".format(
        app_config['BIN']['MAGICK'],
        src_p,
        output_file
    )
    if not output_file.exists():
        width, height = aspectratio.get_size(src, app_config)
        if width < 1048:
            return
        print("Resizing for Instagram: {}".format(src_p.name))
        cmd.execute_cmd(cmd_all)


def resize_for_nas_storage(src, app_config):
    src_p = Path(src)
    src_name = src_p.name
    if 'Insta' in src_name or 'Nas' in src_name:
        return
    output_file = Path(
        "{}/{}_Nas{}".format(src_p.parent, src_p.stem, src_p.ext))
    # we can also use: -unsharp 0.25x0.08+8.3+0.045
    cmd_all = "{} {} -resize 3072x -sharpen 0x.6  -colorspace sRGB '{}'".format(
        app_config['BIN']['MAGICK'],
        src_p,
        output_file
    )
    if not output_file.exists():
        width, height = aspectratio.get_size(src, app_config)
        if width < 3072:
            return
        print("Resizing for Instagram: {}".format(src_p.name))
        cmd.execute_cmd(cmd_all)
        return output_file
    return None


def resize_for_flickr_storage(src, app_config):
    src_p = Path(src)
    src_name = src_p.name
    if 'Insta' in src_name or 'Nas' in src_name:
        return
    output_file = Path(
        "{}/{}_Flickr{}".format(src_p.parent, src_p.stem, src_p.ext))
    # we can also use: -unsharp 0.25x0.08+8.3+0.045
    cmd_all = "{} {} -resize 2048x -sharpen 0x.6  -colorspace sRGB '{}'".format(
        app_config['BIN']['MAGICK'],
        src_p,
        output_file
    )
    if not output_file.exists():
        width, height = aspectratio.get_size(src, app_config)
        if width < 2048:
            return
        print("Resizing for Instagram: {}".format(src_p.name))
        cmd.execute_cmd(cmd_all)
        return output_file
    return None
