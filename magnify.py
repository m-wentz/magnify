import os
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from requests.exceptions import RequestException
import logging

for logger in [logging.getLogger(name) for name in logging.root.manager.loggerDict]:
    logger.setLevel(logging.WARNING)

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

banner = (WHITE + r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⢉⣉⣉⣉⡉⠛⠷⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣠⣴⣿⣿⣿⣿⣿⡿⣿⣶⣌⠹⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠉⠻⣧⠘⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⠀⢹⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⠛⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⢿⡆⠈⠛⠻⠟⠛⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣦⠀⠀⠈⠉⠛⠓⠲⠶⠖⠚⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠁                             v 1.0
""" + RESET)

parser = argparse.ArgumentParser(
    prog='magnify.py',
    description='Take screenshots of typosquatted domains to identify potential phishing pages.')

parser.add_argument('-f', '--file', type=str, required=True,
                    help="Path to the file containing a list of domains.")
parser.add_argument('-o', '--output', type=str, default='screenshots',
                    help='Output directory for screenshots captured.')
parser.add_argument('--headless', action='store_true',
                    help='Run browser in headless mode.')

args = parser.parse_args()
print(banner)

if not os.path.exists(args.output):
    os.makedirs(args.output)

driver_arguments = (
    '--log-level=3',
    '--ignore-certificate-errors',
    '--disable-gpu',
    '--disable-notifications',
    '--window-size=1920,1080',
    '--no-default-browser-check',
    '--disable-client-side-phishing-detection',
    '--disable-ipc-flooding-protection',
    '--disable-renderer-backgrounding',
    '--no-sandbox',
    '--disable-dev-shm-usage',
)

options = Options()
for arg in driver_arguments:
    options.add_argument(arg)

if args.headless:
    options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

total_domains = sum(1 for line in open(args.file, 'r'))

with open(args.file, 'r') as domains:
    for domain in domains:
        url = domain.strip()
        full_url = 'https://' + url
        screenshot_path = os.path.join(args.output, url + '.png')
        try:
            response = requests.get(full_url, timeout=1, allow_redirects=True)
            response.raise_for_status()
            final_url = response.url
            driver.get(final_url)
            time.sleep(1)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
            driver.save_screenshot(screenshot_path)
            print(
                f"{GREEN}({total_domains} - {url}) Screenshot captured!{RESET} {BLUE}{screenshot_path}{RESET}")
            total_domains -= 1
        except RequestException as e:
            print(f"{RED}({total_domains} - {url}) Connection refused.{RESET}")
            total_domains -= 1
        except Exception as e:
            print(f"{RED}({total_domains} - {url}) ERROR: {e}{RESET}")
            total_domains -= 1

print(f"{YELLOW}Done!{RESET}")
driver.quit()
