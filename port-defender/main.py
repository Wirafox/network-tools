from concurrent.futures import ThreadPoolExecutor
import socket

def handle_intruder(client_socket, addr):
    print(f"--- Analiza intruza {addr[0]} ---")
    #zapisywanie do pliku
    with open("logi.txt", "a") as logi:
        logi.write(f"pruba połączenia, {client_socket}, adrr {addr}\n")
    #jak by coś wywaliło
    try:
        client_socket.send(b"Connection refusec by security system.\n")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Przypisje konkretny adres i port na którym nsłuchuje 
    server.bind(('0.0.0.0', 8888))
    #poczekalnia
    server.listen(10)

    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            #czekamy az ktos przyjdzie
            client, addr = server.accept()
            #wysyłamy "pacjeta" do "lekarza"
            executor.submit(handle_intruder, client, addr)
            
def main():
    start_server()

if __name__ == "__main__":
    main()