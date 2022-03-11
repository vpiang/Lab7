# Back up a Network Device

from netmiko import ConnectHandler
from getpass import getpass

'''prompt user for username'''
user = input("Enter username: ")

'''prompt user for password'''
password = getpass("Enter your password: ")

device = {
    'ip': '192.168.108.11',
    'username': user,
    'password': password,
    'device_type': 'cisco_ios'
}

connect = ConnectHandler(**device)

output = connect.send_command('show run')
print(output)
