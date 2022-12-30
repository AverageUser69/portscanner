#!/usr/bin/python3
import socket
import colorama
#defining user defined url and port 
def user_defined():
    def is_port_open(host,port):
        s = socket.socket()
        try:
            s.connect((host,port))
        except:
            return False
        else:
            return True
    host = "127.0.0.1"
    port = 5000
    closed_ports = []
    open_ports = []
    for port in range (1,port):
        if is_port_open(host,port):
            open_ports.append(port)
        else:
            closed_ports.append(port)
    colorama.init()
    if closed_ports:
        print(colorama.Fore.RED + f'The following ports are closed: {closed_ports}')
    else:
        print(colorama.Fore.RED + "No closed ports were found.")
    if open_ports:
        print(colorama.Fore.GREEN + f'The following ports are open: {open_ports}')
    else:
        print(colorama.Fore.GREEN + "No open ports were found.")
    colorama.deinit()

#defining the input from user 
import socket

def user_input():
    def is_port_open(host,port):
        s = socket.socket()
        try:
            s.connect((host,port))
        except:
            return False
        else:
            return True
    print("\n")
    host = input("Enter the name of host: ")
    prt = int(input("Enter the range of port: "))

    closed_ports = []
    open_ports = []

    for port in range (1,prt):
        if is_port_open(host,port):
            open_ports.append(port)
        else:
            closed_ports.append(port)

    colorama.init()

    if closed_ports:
        print(colorama.Fore.RED + f'The following ports are closed: {closed_ports}')
    else:
        print(colorama.Fore.RED + "No closed ports were found.")
    if open_ports:
        print(colorama.Fore.GREEN + f'The following ports are open: {open_ports}')
    else:
        print(colorama.Fore.GREEN + "No open ports were found.")

    colorama.deinit()

#defining for specific port in the list
def portin_listt():
    def is_port_open(host,port):
        s = socket.socket()
        try:
            s.connect((host,port))
        except:
            return False
        else:
            return True

    host = input("Enter the name of the Host: ")
    port = []
    n = int(input("Enter number of port to be scanned: "))
    for i in range(0, n):
        ele = int(input())
        port.append(ele)

    closed_ports = []
    open_ports = []

    print("Your Port list are as follows\n")
    print(port)
    for p in port:
        if is_port_open(host,p):
            open_ports.append(p)
        else:
            closed_ports.append(p)

    colorama.init()

    if closed_ports:
        print(colorama.Fore.RED + f'The following ports are closed: {closed_ports}')
    else:
        print(colorama.Fore.RED + "No closed ports were found.")
    if open_ports:
        print(colorama.Fore.GREEN + f'The following ports are open: {open_ports}')
    else:
        print(colorama.Fore.GREEN + "No open ports were found.")
    colorama.deinit()

#scanning the range of ports 
def port_userrange():
    def is_port_open(host, port):
        s = socket.socket()
        try:
            s.connect((host, port))
        except:
            return False
        else:
            return True
    print("\n\n")
    host = input("Enter the name of host: ")

    port_range = input("Enter the range of ports to scan (e.g. 100-200): ")
    start_port, end_port = map(int, port_range.split("-"))

    closed_ports = []
    open_ports = []

    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            open_ports.append(port)
        else:
            closed_ports.append(port)

    colorama.init()

    if closed_ports:
        print(colorama.Fore.RED + f'The following ports are closed: {closed_ports}')
    else:
        print(colorama.Fore.RED + "No closed ports were found.")

    if open_ports:
        print(colorama.Fore.GREEN + f'The following ports are open: {open_ports}')
    else:
        print(colorama.Fore.GREEN + "No open ports were found.")

    colorama.deinit()


#ask user for Ip and scan all 65535 ports
def all_ports():
    def is_port_open(host, port):
        s = socket.socket()
        try:
            s.connect((host, port))
        except:
            return False
        else:
            return True
    print("\n")
    host = input("Enter the name of host: ")
    port = 65535
    
    closed_ports = []
    open_ports = []
    
    for port in range(1, port+1):
        if is_port_open(host, port):
            open_ports.append(port)
        else:
            closed_ports.append(port)

    colorama.init()
    if closed_ports:
        print(colorama.Fore.RED + f'The following ports are closed: {closed_ports}')
    else:
        print(colorama.Fore.RED + "No closed ports were found.")
    if open_ports:
        print(colorama.Fore.GREEN + f'The following ports are open: {open_ports}')
    else:
        print(colorama.Fore.GREEN + "No open ports were found.")
    colorama.deinit()
#defining the port scanner
def port_scanner():
    
    print("\n" + "+"*40)
    print("+"*10 + " "*20 + "+"*10)
    print("+"*10 + "    PORT SCANNER    " + "+"*10)
    print("+"*10 + " "*20 + "+"*10)
    print("+"*40)

port_scanner()
while True:
    
    print(colorama.Style.RESET_ALL)
    print("\n" + "-"*75)
    print("\n" + colorama.Fore.BLUE + "Choose [1] to scan all ports of ip 127.0.0.1. \n")
    print("Choose [2] to Enter Ip and ports and scan them.\n")
    print("CHoose [3] to Enter Ip and to specify a lisst of ports.\n")
    print("Choose [4] to ENter Ip and specify the range.\n")
    print("Choose [5] to Enter Ip and scan all ports.\n")
    print("Choose [6] to Exit.\n")
    choice = int(input("Enter your choice : "+ colorama.Fore.GREEN))
    print(colorama.Style.RESET_ALL)
    print("\n" + "-"*75)
    if choice == 1:
        user_defined()
    elif choice == 2:
        user_input()
    elif choice == 3:
        portin_listt()
    elif choice == 4:
        port_userrange()
    elif choice == 5:
        all_ports()
    elif choice == 6:
        break
        print(colorama.Fore.RED + "You have choosed to exit.")
        print(colorama.Style.RESET_ALL)
    else :
        print("Invalid choice . Please enter a valid choice.")

colorama.deinit()




