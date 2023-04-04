from tool.client import *


# Server tarafı

server = Server("localhost", 5000)
server.start()

# Client tarafı
client = Client("localhost", 5000)
client.send_message("Merhaba, bu bir mesajdır.")
