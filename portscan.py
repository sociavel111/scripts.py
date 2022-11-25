import socket

ports = [21, 22, 80, 443, 445, 3306, 25]

adress = str(input("Digite um endereço: "))
for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	code = client.connect_ex((adress, port))
	if code == 0:
		print(f"Porta {port} OPEN.")
	else:
		print(f"Porta {port} CLOSED.")
