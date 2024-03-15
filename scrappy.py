
# 		< copyright 2024 cyberabhigit >
#		github.com tool  by cyberabhi
# 		it is used to extract data from url



from colorama import  Fore , Style
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
print("SCRAPPY version 2.0 release")
print("-------------------------------")

user_key = input("Enter your key: ")
print("-------------------------------")
os.system('clear')
# Check if the key is correct
if user_key != 'iwha12':
    print("INCORRECT KEY! : exiting...")
    exit()
    os.system('clear')
tool_banner = pyfiglet.figlet_format("SCRAPPY")
color_tool_banner = f"{Fore.CYAN}{tool_banner}{Style.RESET_ALL}"
print(color_tool_banner)
print("------------------------------")
print("SCRAP ANY URL BY SCRAPPYI")
print("SCRAPPY version 2.0 release")
print("[+] MADE BY CYBERABHI-GIT")
print("-------------------------------")

print("1) Scrap Url")
print("2) Scrap Cookies")
print("3) Official Website cyberabhi")
print("4) Exit")
print("--------------------------------")
user_reply = int(input("Select an option (1-4) : "))
print("---------------------------------")
if user_reply == 1:
	url = input("[+] Enter Url : ")
	response = requests.get(url)
	if response.status_code == 200:
		data = response.text
		print(data)
	else:
		print("Failed to retrieve data from the URL")
elif user_reply == 2:
	url = input("[ cookies ] Enter Url : ")
	response = requests.get(url)
	cookies = response.cookies
	for cookie in cookies:
		print(cookie.name, cookie.value)
elif user_reply == 3:
	webbrowser.open('https://abhitype.blogspot.com')
elif user_reply == 4:
	os.system('exit')



