import os
import requests
import webbrowser
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from colorama import Fore, Style
import re

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + r"""
 ____   _______________.____       _____ __________.___ ____ ___  _____   
 \   \ /   /\_   _____/|    |     /  _  \\______   \   |    |   \/     \  
  \   Y   /  |    __)_ |    |    /  /_\  \|       _/   |    |   /  \ /  \ 
   \     /   |        \|    |___/    |    \    |   \   |    |  /    Y    \
    \___/   /_______  /|_______ \____|__  /____|_  /___|______\/\____|__  /
                    \/         \/       \/       \/                    \/ 

              VELARIUM v1.1 — By ValiasXD
""" + Style.RESET_ALL)

username_sites = [
    "https://github.com/{}", "https://twitter.com/{}", "https://www.reddit.com/user/{}",
    "https://www.instagram.com/{}", "https://www.tiktok.com/@{}", "https://www.pinterest.com/{}",
    "https://www.tumblr.com/{}", "https://vimeo.com/{}", "https://soundcloud.com/{}",
    "https://www.snapchat.com/add/{}", "https://www.behance.net/{}", "https://www.flickr.com/people/{}",
    "https://dribbble.com/{}", "https://www.goodreads.com/{}", "https://www.last.fm/user/{}",
    "https://letterboxd.com/{}", "https://medium.com/@{}", "https://about.me/{}",
    "https://www.quora.com/profile/{}", "https://dev.to/{}", "https://www.producthunt.com/@{}",
    "https://www.kongregate.com/accounts/{}", "https://www.patreon.com/{}", "https://ko-fi.com/{}",
    "https://500px.com/p/{}", "https://ello.co/{}", "https://forum.freecodecamp.org/u/{}",
    "https://www.codecademy.com/profiles/{}", "https://www.tripadvisor.com/members/{}",
    "https://www.wattpad.com/user/{}", "https://www.strava.com/athletes/{}", 
    "https://replit.com/@{}", "https://scratch.mit.edu/users/{}", "https://www.okcupid.com/profile/{}",
    "https://www.twitch.tv/{}", "https://bsky.app/profile/{}", "https://www.roblox.com/users/profile?username={}",
    "https://www.canva.com/{}","https://www.hackster.io/{}", "https://www.instructables.com/member/{}",
    "https://www.deviantart.com/{}", "https://stackoverflow.com/users/{}", "https://hub.docker.com/u/{}",
    "https://myanimelist.net/profile/{}", "https://www.chess.com/member/{}", "https://leetcode.com/{}",
    "https://www.npmjs.com/~{}", "https://crates.io/users/{}", "https://gitlab.com/{}"
]

def help_menu():
    print(Fore.YELLOW + """
Available Commands:
────────────────────────────────────────────────────────────
username <name>        - Search username on 50 websites
geoip <ip>             - Locate IP and open Google Maps
webcam <ip|country>    - Search for public webcams (via Insecam)
exif <image>           - Extract EXIF and GPS metadata
help                   - Show help menu
exit                   - Exit Velarium
""" + Style.RESET_ALL)

def geo_ip_lookup(ip):
    print(f"[+] Locating IP: {ip}")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data['status'] == 'success':
                print(f"  IP       : {data['query']}")
                print(f"  Country  : {data['country']}")
                print(f"  Region   : {data['regionName']}")
                print(f"  City     : {data['city']}")
                print(f"  ISP      : {data['isp']}")
                print(f"  Location : {data['lat']},{data['lon']}")
                webbrowser.open(f"https://www.google.com/maps?q={data['lat']},{data['lon']}")
            else:
                print("  [!] IP lookup failed.")
        else:
            print(f"  [!] Error {r.status_code}")
    except Exception as e:
        print(f"  [!] Error: {e}")

def webcam_lookup(target):
    print(f"[+] Finding webcams near {target}")
    try:
        if re.match(r"^\d{1,3}(?:\.\d{1,3}){3}$", target):
            url = f"http://www.insecam.org/en/byip/{target}/"
        else:
            url = f"http://www.insecam.org/en/bycountry/{target[:2].upper()}/"
        webbrowser.open(url)
    except Exception as e:
        print(f"[!] Error: {e}")

def extract_exif(image_path):
    print(f"[+] Extracting EXIF from {image_path}")
    try:
        img = Image.open(image_path)
        exif = img._getexif()
        if not exif:
            print("  [!] No EXIF data found.")
            return
        for tag, val in exif.items():
            decoded = TAGS.get(tag, tag)
            print(f"  {decoded:25}: {val}")
    except Exception as e:
        print(f"[!] Error: {e}")

def username_search(name):
    print(f"[+] Searching for username: {name}")
    for site in username_sites:
        url = site.format(name)
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                print(f"  [✔] Found: {url}")
        except:
            continue

def main():
    banner()
    help_menu()
    while True:
        cmd = input(Fore.GREEN + "\nVELARIUM > " + Style.RESET_ALL).strip()
        if cmd.startswith("username "):
            _, name = cmd.split(" ", 1)
            username_search(name)
        elif cmd.startswith("geoip "):
            _, ip = cmd.split(" ", 1)
            geo_ip_lookup(ip)
        elif cmd.startswith("webcam "):
            _, target = cmd.split(" ", 1)
            webcam_lookup(target)
        elif cmd.startswith("exif "):
            _, path = cmd.split(" ", 1)
            extract_exif(path)
        elif cmd == "help":
            help_menu()
        elif cmd == "exit":
            print("Exiting Velarium.")
            break
        else:
            print("[!] Unknown command. Type 'help'.")

if __name__ == "__main__":
    main()