import fire
import os

from unipath import Path, FILES

from ..tasks import imagecopy
from ..config import get_appconfig
from ..tasks import resize
from ..tasks import tag

def backup_to_amazon(configdir=None):
    pass


def backup_to_nas(configdir=None, subdir='ashish'):
    app_path = os.path.abspath(os.curdir)
    config_path = configdir or app_path
    print("Working path: {}\n".format(config_path))
    app_config = get_appconfig(search_path=config_path)
    image_root = Path(app_config['STORAGE']['NAS_ROOT'], subdir)
    image_root.mkdir(parents=True)
    app_path_p = Path(app_path)
    for src_file in app_path_p.listdir(pattern="*_Nas.jpg", filter=FILES, names_only=False):
        if src_file.isfile:
            imagecopy.copy_to_nas(src_file, image_root)


def backup_to_dropbox(configdir=None):
    app_path = os.path.abspath(os.curdir)
    config_path = configdir or app_path
    print("Working path: {}\n".format(config_path))
    app_config = get_appconfig(search_path=config_path)
    app_path_p = Path(app_path)
    for src_file in app_path_p.listdir(pattern="*_Insta.jpg", filter=FILES, names_only=False):
        if src_file.isfile:
            imagecopy.copy_to_dropbox(src_file)


def createfor_instagram(configdir=None):
    app_path = os.path.abspath(os.curdir)
    config_path = configdir or app_path
    print("Working path: {}\n".format(config_path))
    app_config = get_appconfig(search_path=config_path)
    app_path_p = Path(app_path)
    for src_file in app_path_p.listdir(pattern="*.jpg", filter=FILES, names_only=False):
        if src_file.isfile:
            resize.resize_for_instagram(src_file, app_config)


def createfor_nas(configdir=None):
    app_path = os.path.abspath(os.curdir)
    config_path = configdir or app_path
    print("Working path: {}\n".format(config_path))
    app_config = get_appconfig(search_path=config_path)
    app_path_p = Path(app_path)
    for src_file in app_path_p.listdir(pattern="*.jpg", filter=FILES, names_only=False):
        if src_file.isfile:
            output_file = resize.resize_for_nas_storage(src_file, app_config)


def createfor_flickr(configdir=None):
    app_path = os.path.abspath(os.curdir)
    config_path = configdir or app_path
    print("Working path: {}\n".format(config_path))
    app_config = get_appconfig(search_path=config_path)
    app_path_p = Path(app_path)
    for src_file in app_path_p.listdir(pattern="*.jpg", filter=FILES, names_only=False):
        if src_file.isfile:
            output_file = resize.resize_for_flickr_storage(src_file, app_config)
            if output_file:
                tag.remove_tags_from_flickr(output_file, app_config)



def main():
  fire.Fire({
      'backup_to_dropbox': backup_to_dropbox,
      'backup_to_nas': backup_to_nas,
      'createfor_instagram': createfor_instagram,
      'createfor_nas': createfor_nas,
      'createfor_flickr': createfor_flickr,
  })
