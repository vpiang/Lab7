import datetime, pathlib, os, netmiko
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException


user = input("Enter username: ")
password = getpass("Enter your password: ")

device = {
    'ip': '192.168.108.11',
    'username': user,
    'password': password,
    'device_type': 'cisco_ios'
}
try:
    connect = ConnectHandler(**device)
    output = connect.send_command('show run')
    f = open('backup.config', 'x')
    f.write(output)
    f.close()

except (AuthenticationException):
    print("An authentication error occured while connecting to: " + device['ip'])
except (SSHException):
    print("An error occured while connecting to device " + device ['ip'] + " via ssh. Is SSH enable?")
except (NetMikoTimeoutException):
    print("The device " + device['ip'] + " timed out when attempting to connect")
