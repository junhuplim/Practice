# System Designs Fundamentals

### Client and Server
- client and server paradigm
    - client is a machine or process that requests data or service from a server
    - server is a machine or process that provides data or service for a client, usually by listening for incoming network calls

- ip address
    - an address given to each machine connected to public internet
    - ipv4 addresses consist of four numberse separated by dots:
        - 127.0.0.1: localhost
        - 192.168.x.y: private network (machines on your private wifi network usually have the 192.168 prefix)

- port
    - for multiple programs to lsiten for new network connections on same machine without colliding, they pick a port to listen on
    - port is an integer between 0 and 65,535 (2^16 ports total)
    - typically ports 0-1023 are reserved for system ports and should not be used by user-level processes
    - some ports have pre-defined uses
        - 22: secure shell
        - 53: dns lookup
        - 80: http
        - 443: https

- dns (domain name system)
    - describes the entities and protocols involved in the translation from domain names to ip addresses
    - machines typically make a dns query to a well known entity which is responsible for returning the ip address of the requested domain name in the response

---
### Network Protocols
- IP (Internet Protocol)
    - IP packets has header and data
    - header contains src and dest IP address
    - IP packets are limited in size of 2^16 bytes
        - limited size means need to send multiple packets
        - higher chance of packets loss
        - IP does not guarantee order of packets sent

- TCP (transmission control protocol)
    - built on top of IP, meant to solve issues above
        - ensures order of packets in an error free way (knows if packets are corrupted)
        - also knows when packets keep failing to get received
    - tcp header part of the ip packet
    - communicate with other machines through handshake
    - problem with tcp is it is not robust for developers

- HTTP (hyper text transfer protocol)
    - machines communicates with a request-response paradigm
    - request contains
        - host and port which determines destination machine
        - method (post/get/put/delete etc)
        - path (server might have multiple paths for different services/logics)
        - headers (key-value pair which contains important metadata)
        - body (the data)
    - response contains
        - status code (type of responses eg: 404 means data not found)
        - headers (key-value pair which contains important metadata)
        - body (the data)

ip, tcp were more of transportation of data. http introduces the opportunity to add business logic

---
### Storage
- data persistence
    - disk
        - writing data to disk means data will still exists even if database server goes down
    - memory
        - writing data to memory means data will be lost if database server goes down
        - writing/reading data to memory is much faster as compared to disk

---
