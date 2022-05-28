import os
import subprocess
import requests
import logging

from dotenv import load_dotenv

if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', None)
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = requests.get(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('config.env', 'wb+') as f:
                f.write(res.content)
                f.close()
        else:
            logging.error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        logging.error(str(e))
except TypeError:
    pass

load_dotenv('config.env', override=True)

UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO', None))
UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH')

try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_REPO = "https://github.com/tmadminz/Appeza-tg-mirror-leech-bot-07-04-2022"
    
try:
    if len(UPSTREAM_BRANCH) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_BRANCH = 'tm-mir'

if os.path.exists('.git'):
    subprocess.run(["rm", "-rf", ".git"])

subprocess.run([f"git init -q \
                  && git config --global user.email priiiiyoplus@gmail.com \
                  && git config --global user.name mlb \
                  && git add . \
                  && git commit -sm update -q \
                  && git remote add origin {UPSTREAM_REPO} \
                  && git fetch origin -q \
                  && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

