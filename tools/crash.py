# Import modules
import os
import sys
import platform
from time import ctime
from colorama import Fore

""" This function will stop the program when a critical error occurs """


def CriticalError(message, error):
    print(f"""
    {Fore.RED}:=== : İletişim
    {Fore.MAGENTA} İnstagram : https://www.instagram.com/byh4cker
    {Fore.MAGENTA} WhatsApp : +90 535 075 3174  
    {Fore.MAGENTA} Telegram : t.me/byh4cker
    {Fore.MAGENTA} ICQ : https://icq.im/byh4cker
    {Fore.MAGENTA} WebSite : https://www.byh4cker.com/
    {Fore.RED}:=== System info:
    {Fore.RESET}
    """)
    sys.exit(5)
