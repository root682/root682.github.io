import socket
import threading
import re

# Configuración del servidor
HOST = '0.0.0.0'  # Escuchar en todas las interfaces
PORT = 12345

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# Lista de clientes conectados
clients = []

# Lista de palabras prohibidas para el bot anti-spam
palabras_prohibidas = ["spam", "publicidad", "oferta"]

# Función para manejar la recepción y retransmisión de mensajes de un cliente
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # El cliente se desconectó
                clients.remove(client_socket)
                client_socket.close()
                break
            
            if not contiene_palabras_prohibidas(message):
                print(message)
                # Retransmitir el mensaje a todos los demás clientes
                for client in clients:
                    if client != client_socket:
                        client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break

# Función para verificar si un mensaje contiene palabras prohibidas
def contiene_palabras_prohibidas(mensaje):
    for palabra in palabras_prohibidas:
        if re.search(rf'\b{palabra}\b', mensaje, re.IGNORECASE):
            return True
    return False

# Función principal para aceptar conexiones de clientes
def main():
    print(f"Servidor de chat en ejecución en {HOST}:{PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión entrante desde {client_address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()