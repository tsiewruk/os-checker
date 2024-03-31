import subprocess

def get_system_uptime():
    uptime = subprocess.run(['uptime'], capture_output=True, text=True)        
    uptime_line = uptime.stdout.strip().split(',')[0]
    return print(uptime_line)

def get_hostname():
    hostname = subprocess.run(['hostname'], capture_output=True, text=True)
    hostname_line = hostname.stdout.strip().split(',')[0]
    return print(hostname_line)

def get_network_interfaces():
    network_interfaces = subprocess.run(['ifconfig'], capture_output=True, text=True)
    return network_interfaces


def main():
    get_system_uptime()
    get_hostname()

if __name__ == "__main__":
    main()