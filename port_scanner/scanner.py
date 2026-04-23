import socket
from datetime import datetime

target = input("Podaj adres IP lub domenę: ")

print(f"Skanowanie: {target}")
print("Start:", datetime.now())

open_ports = []

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} jest otwarty")
        open_ports.append(port)
    
    s.close()

# zapis do pliku
with open("log.txt", "w") as f:
    f.write(f"Skanowanie: {target}\n")
    f.write(f"Data: {datetime.now()}\n")
    f.write("Otwarte porty:\n")
    for port in open_ports:
        f.write(f"{port}\n")

print("Zakończono skanowanie. Wynik zapisany w log.txt")