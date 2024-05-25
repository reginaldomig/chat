import socket
import threading

# Configurações do cliente
HOST = '192.168.0.113'  # Endereço IP do servidor (localhost)
PORT = 12345  # Porta do servidor


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                break
        except:
            print("Erro ao receber mensagem.")
            client_socket.close()
            break


def send_messages(client_socket):
    while True:
        message = input("")
        if message:
            client_socket.send(message.encode('utf-8'))
        else:
            break


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Conectado ao servidor.")

    # Thread para receber mensagens
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Thread para enviar mensagens
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client_socket.close()


if __name__ == "__main__":
    start_client()
