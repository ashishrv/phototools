import shutil
from unipath import Path, FILES
import re

def copy_images(src, dst):
    """
    Destination should not exist
    """
    src_p = Path(src)
    dst_p = Path(dst)
    if not src_p.exists():
        print("Source Card Directory does not exist: {}".format(src_p))
        return False
    if dst_p.exists():
        print("Destination directory already exist: {}".format(dst_p))
        return False
    dst_p.mkdir(parents=True)
    print("copying images from {} to {}".format(src_p, dst_p))
    for src_file in src_p.listdir(pattern=None, filter=FILES, names_only=False):
        print("Copying file: {}".format(src_file.name))
        dst_file = Path(dst_p, src_file.name)
        src_file.copy(dst_file, times=False, perms=False)


def copy_to_dropbox(src):
    src_p = Path(src)
    dropbox_path = Path(Path('~/Dropbox/Photos').expand_user())
    dropbox_image = Path("{}/{}".format(dropbox_path, src_p.name))
    if not dropbox_image.exists():
        print("Copying to: {}".format(dropbox_image))
        src_p.copy(dropbox_image, times=True, perms=False)


def copy_to_nas(src, image_root):
    rex = re.compile(
        '/.*/(\d\d\d\d)/(\d\d_[a-zA-Z]+)/(\d+_\d+_\d+)/.*', re.IGNORECASE)
    src_p = Path(src)
    matched = rex.match(str(src_p.parent))
    path1, path2, path3 = matched.group(1), matched.group(2), matched.group(3)
    dst_path = Path(image_root, path1, path2, path3, src_p.name)
    dst_path.parent.mkdir(parents=True)
    if not dst_path.exists():
        print("Copying to: {}".format(dst_path))
        src_p.copy(dst_path, times=False, perms=False)
