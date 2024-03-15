from colorama import Fore, Style
import pyfiglet
import requests
import webbrowser
import os

os.system('clear')

tool_banner = pyfiglet.figlet_format("INSTALLER")
color_tool_banner = f"{Fore.CYAN}{tool_banner}{Style.RESET_ALL}"
print(color_tool_banner)
print("------------------------------")
print("SCRAP ANY URL BY SCRAPPY | CYBERABHI")
print("SCRAPPY version 2.1")
print("-------------------------------")

user_key = input(f"{Fore.GREEN}[TAP] Enter your key: {Style.RESET_ALL}")
print("-------------------------------")
os.system('clear')
# Check if the key is correct
if user_key != 'iwha12':
    print(f"{Fore.RED}INCORRECT KEY! : exiting...{Style.RESET_ALL}")
    exit()

tool_banner = pyfiglet.figlet_format("SCRAPPY")
color_tool_banner = f"{Fore.CYAN}{tool_banner}{Style.RESET_ALL}"
print(color_tool_banner)
print("------------------------------")
print(f"{Fore.RED}[+] SCRAP ANY URL BY SCRAPPYI [+]{Style.RESET_ALL}")
print(f"{Fore.RED}[+] SCRAPPY version 2.0 release [+]{Style.RESET_ALL}")
print(f"{Fore.RED}[+] MADE BY CYBERABH -GIT [+]{Style.RESET_ALL}")
print("-------------------------------")

print(f"{Fore.RED}[1] Scrap Url{Style.RESET_ALL}")
print(f"{Fore.RED}[2] Scrap Cookies{Style.RESET_ALL}")
print(f"{Fore.RED}[3] Official Website cyberabhi{Style.RESET_ALL}")
print(f"{Fore.RED}[4] Exit{Style.RESET_ALL}")
print("--------------------------------")
user_reply = int(input(f"{Fore.GREEN}Select an option (1-4) : {Style.RESET_ALL}"))
print("---------------------------------")
if user_reply == 1:
    try:
        url = input(f"{Fore.GREEN}[+] Enter Url : {Style.RESET_ALL}")
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad status codes (4xx, 5xx)

        if response.status_code == 200:
            data = response.text
            print(data)
        else:
            print("Failed to retrieve data from the URL")

    except requests.exceptions.RequestException as e:
        print("Error: Invalid URL or failed to connect.")
        print(f"Exception: {e}")

elif user_reply == 2:
    try:
        url = input(f"{Fore.GREEN}[ cookies ] Enter Url : {Style.RESET_ALL}")
        response = requests.get(url)
        cookies = response.cookies
        for cookie in cookies:
            print(cookie.name, cookie.value)
    except requests.exceptions.RequestException as e:
        print("Error: Invalid URL or failed to connect.")
        print(f"Exception: {e}")

elif user_reply == 3:
    webbrowser.open('https://abhitype.blogspot.com')

elif user_reply == 4:
    exit()

