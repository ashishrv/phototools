import fire
import os
from ..config import get_appconfig
from ..tasks import imagecopy
from ..tasks import organize
from ..tasks import tag

def card_rawimage_hanndler(configdir=None, image_subfolder=None):
  app_path = os.path.abspath(os.curdir)
  config_path = configdir or app_path
  app_config = get_appconfig(search_path=config_path)
  src = app_config['CARDMOUNT']
  dst = os.path.join(app_config['PHOTOROOT'], app_config['IMAGEFOLDER'])
  imagecopy.copy_images(src, dst)
  tag.update_copyright(dst, app_config)
  dst_organized = app_config['PHOTOROOT']
  if image_subfolder:
    dst_organized = os.path.join(app_config['PHOTOROOT'], image_subfolder)
  organize.organize_photos(dst, dst_organized, app_config)



def main():
  fire.Fire(card_rawimage_hanndler)
