
from ..util import cmd

def organize_photos(src, dst, app_config):
    if app_config['BIN']['EXIFTOOL'] == None:
        print("exiftool does not exist. Please install it.")
        return
    TOOL_CMD = r"{} -o . '-Directory<FileModifyDate' '-Directory<DateTimeOriginal' "
    DST_OPT = r'-d "{}/%Y/%m_%B/%Y_%m_%d" '
    FILE_OPT = r"'-filename<${datetimeoriginal}__${FileName;}%-c'"
    SRC_OPT = ' -r -progress {}'
    cmd_all = TOOL_CMD.format(app_config['BIN']['EXIFTOOL']) + \
        DST_OPT.format(dst) + \
        FILE_OPT + \
        SRC_OPT.format(src)
    cmd.execute_cmd(cmd_all, shell=True)
