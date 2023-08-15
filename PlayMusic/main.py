import socket
import threading
import pyaudio
import pygame


IP_ADDRESS = 'localhost'
PORT_NUMBER = 5000


# Initialize pyaudio and pygame
pa = pyaudio.PyAudio()
pygame.mixer.init()


# Create a socket connection for the chat room
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP_ADDRESS, PORT_NUMBER))
sock.listen(5)


# Define a function to handle incoming connections
def handle_connection(conn, addr):
    # Start a new thread for each incoming connection
    t = threading.Thread(target=handle_connection, args=(conn, addr))
    t.start()


# Set up a pyaudio stream for audio input and output
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, output=True, frames_per_buffer=1024)

# Play a music file in the chat room
pygame.mixer.music.load("PlayMusic\demo.mp3")
pygame.mixer.music.play()

# Loop to keep the connection open
connections = []

while True:
    # Read audio data from the stream
    data = stream.read(1024)
    
    # Send the audio data to all connected users
    for conn in connections:
        conn.sendall(data)
    
        # Receive audio data from other users
        data = conn.recv(1024)
    
        # Play the received audio data
        stream.write(data)

        # Close the stream and connection
        stream.close()
        conn.close()
    break


while True:
    # Accept incoming connections
    conn, addr = sock.accept()
    connections.append(conn)

    # Handle the incoming connection
    handle_connection(conn, addr)
