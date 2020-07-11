# Namespace-Mininet-OVS

##Problem 1: Socket Programming
Create a network topology with single switch and two-hosts using both Network-Namespaces and Mininet.
Further program following two client-server applications. Execute the client and server codes on different hosts
created in the earlier step. Now analyze and compare the performance of your client-server applications in networks
created by Network-Namespace and Mininet.

Hint: Use Wireshark for analyzing performance in both the cases.

a. Write a server program which sends the time of day information to the client. Also develop a client interface
for interacting with the server. The client should first send a request message to the server asking for the
time of day information. The server in turn responds to the client with its time of day information. The IP
address and port number of the server is to be passed as command line arguments to the client code. Use
proper display messages on both the client and server consoles. Use UDP sockets. (Naming Convention –
TimeOfDayClient.c, TimeOfDayServer.c).

b. The goal of this assignment is to implement a TCP client and server. Your TCP client/server will communicate over the network and exchange data. The user interface (i.e., what’s displayed to the user) should look
the same for both the TCP applications.

Write a program named CalcClientTCP.c that performs the following functions:
1. Connect to the server at the given hostname and port using TCP.
2. Print the IP address and port of the server.
3. Ask the user for a simple arithmetic expression to calculate.
4. Send the expression to the server.
5. Read the answer from the server.
6. Display the answer to the user.
7. Repeat the steps 3-6 until the user enters the sentinel value given in the user prompt. When the user enters
the sentinel, the client must close the connection to the server and quit.
Write a program named CalcServerTCP.c that performs the following functions:
1. Take a port number as a command-line argument.
2. Listen for a TCP connection on the port specified.
3. Print the IP address and port of the connected client.
4. Receive data from the client.
5. Evaluate the arithmetic expression.
6. Send the result back to the client.
7. If the connection is still open, repeat the steps 4-6 until the user presses Ctrl-C. If the connection is closed,
repeat steps 2-6 until the user presses Ctrl-C.
1

Problem 2: Network-Namespace and Mininet

In this problem you have to create the given network topology (as shown in Figure 1) using both NetworkNamespace and Mininet. After creating the topology, analyze and compare the performance of the networks on
basis of different parameters like throughput, bandwidth, avg. rtt. etc. using Wireshark.

• Consider the switches S1, S2, S3 and S4 shown in the figure as ovs-switches.
• Consider R as the router and r-eth1, r-eth2, r-eth3 and r-eth4 as the different interfaces of the router with
different networks connected to each interface.
• Consider H1, H2, H3 and H4 as host with given IP addresses. Host needs to be configured with default
gateways as shown in the figure.
Figure 1: Network Topology for Problem 2

Hint: The router in both the cases will be a simple host. You need to add 4 different interfaces to the host
and configure the interfaces as required. Further, you also need to add routes to the routing table in the router for
different networks and disable the firewall daemon running at router.
2
