import nmap

def scan_target(ip):
    nm = nmap.PortScanner()
    options = "-sV -sC"
    nm.scan(ip, arguments=options)
    
    for host in nm.all_hosts():
        print("Host: %s (%s)" % (host, nm[host].hostname()))
        print("State: %s" % nm[host].state())
        for protocol in nm[host].all_protocols():
            print("Protocol: %s" % protocol)
            port_info = nm[host][protocol]
            for port in port_info.keys():
                print("Port: %s\tState: %s" % (port, port_info[port]['state']))

def main():
    while True:
        print("\nNmap Scanner Menu")
        print("1. Enter an IP address to scan")
        print("2. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            ip = input("Enter the IP address to scan: ")
            scan_target(ip)
        elif choice == '2':
            print("Exiting the Nmap Scanner")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
