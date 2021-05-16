import socket
import sys
import whois

website = input("Enter the website ")
web_site = f"{website}"
print("-"*60)

ip_add = socket.gethostbyname(web_site)
print("IP address = ",ip_add)
print("-"*60)

domain_name = website
domain_info = whois.whois(domain_name)
def ch_reg(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return True
    except:
        return False
ch_reg(domain_name)

domain_info = whois.whois(domain_name)
for key,value in domain_info.items():
    print(key,' : ',value,'\n')
    print("-"*60)
print("please wait for scan the port \n")
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_add, port))
        if result == 0:
            print ("Port {}: 	 Open \n".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("\nYou pressed Ctrl+C")
    sys.exit()

print("break the scan using key CTRL+C \n")

