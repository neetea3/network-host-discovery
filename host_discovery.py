print ("=== NETWORK HOST DISCOVERY ===")

network = input("Enter network (Example: 192.168.1): ")

start_host = int(input("Enter starting host: "))
end_host = int(input("Enter ending host: "))

hosts_found = []

print("\nGenerating hosts...")

for host in range(start_host, end_host +1): 


    ip = network + "." + str(host) 

    print(f"[FOUND]{ip}")

    hosts_found.append(ip)


print("\nHosts Generated:")

for host in hosts_found:
    print(host)

print(f"\nTotal Hosts: {len(hosts_found)}")

