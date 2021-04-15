# Import modules
import os
import sys
import wget
from colorama import Fore

if os.name == "nt":
    winpcap_url = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
    winpcap_dir = os.environ["ProgramFiles(x86)"] + "\\WinPcap"
    if not os.path.exists(winpcap_dir):
        print(
            f'{Fore.MAGENTA}[!] {Fore.YELLOW}Dikkat! "WinPcap" yüklü değil!\n   syn, udp ve diğerlerinin saldırısı için gereklidir,\n    Yalnızca sms saldırısını kullanmak istiyorsanız bunu atlayabilirsiniz,\n    Otomatik Kurulum Yapılsın mı? (y/n){Fore.RESET}'
        )
        if input(f"{Fore.MAGENTA} >>> {Fore.BLUE}").lower() in ("y", "yes", "1"):
            print(f"{Fore.YELLOW}[~] {Fore.CYAN}İndiriliyor...{Fore.BLUE}\n")
            winpcap_installer = wget.download(winpcap_url)
            os.startfile(winpcap_installer)
            print(
                f"\n\n{Fore.GREEN}[?] {Fore.YELLOW}Now please restart program{Fore.RESET}"
            )
            sys.exit(1)
