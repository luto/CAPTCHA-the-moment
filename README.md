# CAPTCHA-the-moment

Someone collected multiple hundred screenshots of ReCaptacha challenges; mostly
from cloudflare. This repo contains a group of scripts to normalize their
filenames, dimensions and cropping.

Later, we'll maybe make some kind of art or science out of them.

## Scripts

* `ingest.py`: copy screenshots from `RAW_CAPTCHA_DIR` to `INGESTED_CAPTCHA_DIR`
  while normalizing their filename.
