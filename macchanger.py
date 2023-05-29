import subprocess
import random

def list_devices():
    print("The Network Adapters: ")
    output = subprocess.check_output("ifconfig | grep flags | cut -d ':' -f1", shell=True)
    devices = output.decode().split("\n")

    # Print the devices with numbers
    for index, device in enumerate(devices, start=1):
        if device:
            print(f"[+] {index}. {device}")


def macchanger(network_device, mac_address):
    subprocess.run(["sudo", "ifconfig", network_device, "down"], check=True)
    subprocess.run(["sudo", "ifconfig", network_device, "hw", "ether", mac_address], check=True)
    subprocess.run(["sudo", "ifconfig", network_device, "up"], check=True)


def mac_range():
    mac_range = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F"]
    random.shuffle(mac_range)
    word = ""
    for i in range(12):
        if i % 2 == 0 and i != 0:
            word += ":"
        word += mac_range[i]
    print("[+] New Mac Address : " + word)
    return word


list_devices()
mac_address = mac_range()
#print(mac_address)
user_input = input("[+] Enter The Device Number : ")

# Validate user input
try:
    device_number = int(user_input)
    output = subprocess.check_output("ifconfig | grep flags | cut -d ':' -f1", shell=True)
    devices = output.decode().split("\n")
    if device_number < 1 or device_number > len(devices):
        raise ValueError
except ValueError:
    print("Invalid device number.")
else:
    network_device = devices[device_number - 1]  # Adjust index for zero-based indexing
    macchanger(network_device, mac_address)
