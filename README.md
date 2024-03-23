## Lab 5: Chat Room
Global Chat room with a chat message board, that students can connect and post chats too.
For this lab, we will be implementing various features of the chat room application as the weeks progress.
By end of this lab, the goal is that each team of students can connect to a privately hosted chat server 
using the chat client they will build, and chat with other students on the server.

The lab is structured as:  
    1. Building a local echo server.  
    2. Building a multithreaded chat client that can connect to a globally hosted chat server.  
    3. Upgrading the chat platform from basic UDP to HTTP protocol.  
    4. Adding client-side authentication and registering student ids to the chat room.  

Each student will be expected to write up the client as per the specification provided.
During the first week, you will write a local version of the server, for your reference, and for testing.


## Preparation
Create a Python venv for this project using `mkdir venv && python3 -m venv venv/`.  
If you don't have venv installed, you can install it using  `python3 -m pip install venv` and then run the above command.  
You should then activate the venv using `source venv/bin/activate`.  
Then, install the required packages using `pip install -r requirements.txt`.  

You are now ready to start coding. All the best!

## Timeline
### week 1 & week 2
_Goal_: Write a simple echo server, with the following specification:  
    1. must accept one connection.  
    2. must accept one message from the client.  
    3. must echo the received message back to the client, and quit.  

_Testing_: You will need two terminals for this.  
In the first terminal (Term1) run the command `python lab5/server.py localhost 8008` to start your server.
In the second terminal (Term2) run the command `python lab5/test/test_server.py` to test your server implementation.
You should see `received b'Hello server!' from ('127.0.0.1', 8008)` as the output in Term2.
Feel free to write more tests to help you as needed.
	
