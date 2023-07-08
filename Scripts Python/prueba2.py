import nmap
scanner = nmap.PortScanner()
ip=input("Digite la direccion ip: ")
print("Escribiste la ip: "+ip)
scanner.scan(ip)

print(scanner.all_hosts())