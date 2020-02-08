# This is a just example of socket in Python
# Dart - Security by Equinockx
import socket

print("Enter the IP address: ", end=" ")
ip = input()
print("Enter the URL: ", end=" ")
urlnew= input()

try:
    print("Full qualified doamin name: " + socket.getfqdn(ip))
    print("Hostname to IP address: " + socket.gethostbyname(urlnew))
    print("Hostname to IP address, extended: " + str(socket.gethostbyname_ex(urlnew)))
    print("Get hostname of local machine: " + socket.gethostname())

except Exception as err:
    print("Error: " + str(err))