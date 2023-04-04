Python Server-Client Example

This project demonstrates how to create a server-client architecture using Python programming language. The project utilizes socket library to create and manage sockets for communication between a server and a client.

Features

Server class to create, start and manage server socket.
Client class to connect, send and receive messages to/from server.
Supports multiple client connections.
Usage

To use this project, follow the steps below:

Clone or download the repository to your local machine.
Install Python 3.x on your machine if not already installed.
Open a terminal and navigate to the root directory of the project.
To start the server, run the following command:

`python server.py`

Once the client is connected, you can send messages to the server using the client console.
Technical Details

The project uses the socket library to create and manage sockets for communication between server and client. The server class listens to incoming connections and spawns a new thread to handle each client. The client class connects to the server socket and sends/receives messages using the socket.

License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE.md file for details.

Contribution

Contributions are welcome! If you would like to contribute, please create a pull request with a detailed description of the changes you have made
