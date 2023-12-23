import requests
from colorama import Style, Fore
import re


# IP:PORT chc
def check_ip(ip_address, port):
    try:
        response = requests.get(f'http://{ip_address}:{port}', timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

#URL for Data
url = 'https://warbandmain.taleworlds.com/handlerservers.ashx?type=list'



#GET response
response = requests.get(url)

# (status code 200)
if response.status_code == 200:
   
    content = response.text
    
    ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b', content)
    
    # Her bir IP adresini ve portu kontrol etme
    for ip_port in ip_addresses:
        ip, port = ip_port.split(':')  # IP :  PORT
        if check_ip(ip, port):
            print(Fore.GREEN + f'{ip}:{port} Server Active')
            output = ip
            output_port = port          
           
        else:
            print(f'\033[91m{ip}:{port} is not active\033[0m')  
else:
    print('Failed to Receive Data')
