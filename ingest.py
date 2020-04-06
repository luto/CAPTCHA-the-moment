#!/usr/bin/env python3

import re
from datetime import datetime

import config


def raw_captchas():
    re_filename = re.compile('Screen Shot (?P<date>[0-9-]+) at (?P<time>[0-9.]+).png')

    for f in config.RAW_CAPTCHA_DIR.glob('*.png'):
        m = re_filename.match(f.name)
        if not m:
            continue
        date, time = m.groups()
        dt = datetime.strptime(f'{date} {time}', '%Y-%m-%d %H.%M.%S')

        with open(f, 'rb') as ff:
            content = ff.read()

        yield dt, content


def ingest(raw_captchas):
    config.INGESTED_CAPTCHA_DIR.mkdir()

    for dt, content in raw_captchas:
        path = (config.INGESTED_CAPTCHA_DIR / dt.isoformat()).with_suffix('.png')

        with open(path, 'wb') as f:
            f.write(content)


def main():
    ingest(raw_captchas())

if __name__ == '__main__':
    main()
