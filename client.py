# from the socket module import all
from socket import *
# from the datetime module import all - This is used to get info regarding time and date
from datetime import *
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# Acquires the host name and IP address from the computer using this program
#host_name = gethostname()
print('Welcome to the simple client and server chat program')
def connect():
    try:
        host_name = input('Please enter the name of the host that you want to connect to :: ')
        IP_address = gethostbyname(str(host_name))
        return host_name, IP_address
    except:
        print('ERROR: Failed to connect')
        connect()

host_name, IP_address = connect()
# Prints the Host name and IP address to the console
print('Host name is :: ' + host_name)
print('IP address :: ' + IP_address)

# set values for host using the host name - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
server_address = (host_name, 10000)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
sock.connect(server_address)

try:
    while True:
        # Ask for user to input a message into the console, and then send that message.
        message = input('Enter a message to send to the server :: ')
        print('sending "%s"' % message)
        print('Awaiting response from the server')
        # Data is transmitted to the server with sendall()
        # encode() function returns bytes object
        sock.sendall(message.encode())

        # Look for the response
        amount_received = 0
        # amount_expected = len(message)
        # while amount_received < amount_expected:
    	# Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(2000).decode()
        amount_received += len(data)
        # Get the current date and time
        date = datetime.today().strftime("%B %d, %Y")
        time =  datetime.now().strftime("%H:%M:%S")
        # print data received from the server, and the time and date the client got the data
        print('received "%s" on %s at %s' % (data, date, time))

finally:
    print('closing socket')
    sock.close()
