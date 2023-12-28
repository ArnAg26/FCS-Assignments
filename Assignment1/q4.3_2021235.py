import nmap
def scan_network(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, arguments='-6 -sV',timeout=600)
    return nm

def analyze_scan_results(ip,scan_results):
    print("Open Ports:")
    # print(scan_results[host])
    for port, protocol in scan_results[ip]['tcp'].items():
        if protocol['state'] == 'open':
            print(f"  Port {port}  {protocol['name']} is open")

target_ipv6 = "fe80::f55e:ddc6:6352:aff2"
# target_ipv6_range="fe80::"
scan_results=scan_network(target_ipv6)
print(scan_results)
analyze_scan_results(target_ipv6,scan_results)