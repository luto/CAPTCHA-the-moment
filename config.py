from pathlib import Path

ROOT_DIR=Path(__file__).resolve().parent

# collection of captchas screenshots in a flat directory
# see raw_captchas/example/*.png
# file format:  dir/Screen Shot 2017-08-10 at 21.12.06.png
#               dir/Screen Shot %Y-%m-%d at %H.%M.%S.png
RAW_CAPTCHA_DIR=ROOT_DIR / 'raw_captchas'

INGESTED_CAPTCHA_DIR=ROOT_DIR / 'ingested_captchas'
