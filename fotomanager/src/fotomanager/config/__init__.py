
from decouple import AutoConfig, Csv
from shutil import which
import json


def get_appconfig(search_path=None):
    config = AutoConfig(search_path)
    appconfig = {}
    appconfig['DEBUG'] = config('DEBUG', cast=bool)
    appconfig['BIN'] = {}
    appconfig['BIN']['EXIFTOOL'] = config(
        'BIN_EXIFTOOL', default=which('exiftool'))
    appconfig['BIN']['FFMPEG'] = config(
        'BIN_FFMPEG', default=which('ffmpeg'))
    appconfig['BIN']['JPEGTRAN'] = config(
        'BIN_JPEGTRAN', default=which('jpegtran'))
    appconfig['BIN']['CJPEG'] = config(
        'BIN_MOZJPEG', default=which('cjpeg'))
    appconfig['BIN']['LEPTON'] = config(
        'BIN_LEPTON', default=which('lepton'))
    appconfig['BIN']['MAGICK'] = config(
        'BIN_MAGICK', default=which('magick'))
    appconfig['CARDMOUNT'] = config('CARDMOUNT')
    appconfig['IMAGEFOLDER'] = config('IMAGEFOLDER')
    appconfig['PHOTOROOT'] = config('PHOTOROOT')
    appconfig['RAWEXT'] = config('RAWEXT', cast=Csv())
    appconfig['COPYRIGHT'] = {}
    appconfig['COPYRIGHT']['ARTIST'] = config('CP_ARTIST')
    appconfig['COPYRIGHT']['COPYRIGHTNOTICE'] = config('CP_COPYRIGHTNOTICE')
    appconfig['COPYRIGHT']['COPYRIGHT'] = config('CP_COPYRIGHT')
    appconfig['COPYRIGHT']['USAGETERM'] = config('CP_USAGETERM')

    appconfig['STORAGE'] = {}
    appconfig['STORAGE']['NAS_ROOT'] = config('NAS_ROOT')


    print("Configuration:\n")
    print(json.dumps(appconfig,
                     sort_keys=True,
                     indent=4,
                     separators=(',', ': ')
    ))
    print("\n")
    return appconfig
