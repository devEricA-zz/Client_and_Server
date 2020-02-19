# from the socket module import all
from socket import *
# from the datetime module import all - This is used to get info regarding time and date
from datetime import *
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Acquires the host name and IP address from the computer using this program
host_name = gethostname()
IP_address = gethostbyname(host_name)

# Prints the Host name and IP address to the console
print('Host name is :: ' + host_name)
print('IP_address :: ' + IP_address)

# set values for host using the host name - meaning this machine and port number 10000
server_address = (host_name, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# we want the server to run all the time, so set up a forever true while loop
client_available = input("Is your client online? Type Y if he/she is :: ")
if client_available == 'Y' or  client_available == 'y':
    while True:
        # Now the server waits for a connection
        print('*** Waiting for a connection ***')
        print('Please wait for your client to connect, as he/she will talk first')
        # accept() returns an open connection between the server and client, along with the address of the client
        connection, client_address = sock.accept()
        # Opens the log file for appending - we don't want old log data to be overwritten
        file = open('client_output.txt', 'a')
        try:
            print('connection from', client_address)
            print('type EXIT() during the session to end your session with the client')
            # Writes the time and date that the client jotted the message to the log file
            file.write('Chat logged at ' + date.today().strftime("%B %d, %Y") + ' at ' + datetime.now(). strftime("%H:%M:%S") + ' reads\n')
            # Receive the data in small chunks and retransmit it
            while True:
                # decode() function returns string object
                data = connection.recv(2000).decode()
                if data != 'EXIT()':
                    print('received "%s"' % data)
                    # Client message is logged
                    file.write('Client : ' + data)
                    file.write('\n')
                    # print('sending data back to the client')
                    # encode() function returns bytes object
                    # connection.sendall(data.encode())
                    reply = input('Enter a message to send back to the client :: ')
                    # Server message is sent, and the server awaits a response
                    connection.sendall(reply.encode())
                    if reply == 'EXIT()':
                        print('You have requested an end to the session with this client')
                        print('Exiting program')
                        break
                    else:
                        # Server message is logged
                        file.write('Server : ' + reply)
                        file.write('\n')
                        print('Awaiting response from the client')
                else:
                    print('no more data from', client_address)
                    print('The client has requested an end to the session')
                    # We write a blank line in order to ensure the log file formats the next message from the client neatly
                    file.write('\n')
                    # File is then closed.
                    file.close()
                    # Notice from server stating that the message has been logged to a file
                    print('This chat has been logged to a file')
                    print('Check client_output.txt to see the logged chat')
                    break

        finally:
            # Clean up the connection
            connection.close()
        want_exit = input('Do you wish to close the server? Type Y if you do ::')
        if want_exit == 'Y' or want_exit =='y':
            break

# now close the socket
print('Closing Server')
sock.close();
