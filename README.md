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
    - disk (also known as non-volatile storage)
        - usually referred to HDD (hard-disk drive) or SSD (solid-state drive)
        - writing data to disk means data will still exists even if database server goes down
        - SSD is far faster than HDD but also far more expensive from a financial point of view
            - hence, HDD typically used for data that is rarely accessed/updated thats stored for a long time
            - SSD will be used for data thats frequently accessed and updated
    - memory
        - writing data to memory means data will be lost if database server goes down
        - writing/reading data to memory is much faster as compared to disk

---
### Latency and Throughput
- latency
    - time it takes for a certain operation to complete in a system. mostly measures time duration (milliseconds or seconds)
        - reading 1 mb from ram: 0.25ms (read from local variable)
        - reading 1 mb from ssd: 1ms
        - transfering 1 mb over 1gbps network: 10ms (api call)
        - reading 1 mb from hdd: 20ms
        - packet inter-continental round trip: 150ms

- throughput
    - the number of operations that a system can handle properly per time unit. (eg throughput of server can be measured in requests per second, like 1gbps)
    - one way to handle throughput bottleneck is to have multiple servers

- latency and throughput are not necessarily correlated and do not have a relationship with one another

---
### Availability
- availability
    - odds of server/service being up and running at any point in time (measured in nines)
- nines
    - percentages of  uptime
    - two 9s = 99% (87.7 hours)
    - five 9s = 99.999% (5.3 minutes)
- redundancy
    - process of replicating parts of a system
    - prevents a single point of failure, eg: replicating more servers with mutliple load balancer etc
    - passive redundancy and active redundancy
- sla (service-level agreement)
    - collection of guarantees given to a customer by a service provider

---
### Caching
- cache
    - piece of hardware or software that stores data, whereby retrieving data from it will be faster
    - often used to store responses to network requests/ computationally long operations
    - data in cache can become stale if main source of truth gets updated but cache doesn't
    - cache hit: requested data found in cache
    - cache miss: requested data could have been found in cache but is not
- write back cache and write through cache
    - write back: information is written only to cache but not to main storage. modified cache only written to main storage when it is replaced
    - write through: information is written to both the cache and the main storage
- cache eviction policy
    - policy by which values get evicted or removed from cache
        - LRU (least recently used)
        - FIFO (first in first out)
        - LFU (least frequently used)
- content delivery network (CDN)
    - a third party service that acts like a cache for our servers
    - web applications can be slow for users in particular region if our servers is located in another region
        - cdn has servers all around the world
        - latency to a cdn server > latency to own server
    - cdn server often referred to as PoPs (points of presence)
    - popular CDNs: cloudfare and google cloud CDN

---
### Proxies
- forward proxy
    - a server that sits between a client and servers and acts on behalf of the client
    - used to mask client's ip address
- reverse proxy
    - a server that sits between clients and servers and acts on behalf of the servers, typicall used for logging, load balancing or caching
- nginx
    - webserver thats often used as reverse proxy and load balancer

---
### Load Balancer [works hand in hand with hashing concept]
- load balancer is a type of reverse proxy that distribute traffic across servers
- load balancers can be found in many parts of a system, from dns layer all the way to database layer
- to ensure that you do not overload server (ensures server has optimal throughput)
    - can have multiple servers
    - need a load balancer to distribute the traffic across these servers
- there are several server selection strategy that a load balancer can have
    - round-robin (go through all server in a loop continuously)
    - weighted round-robin (round robin with set weights, more weights equates to more traffic distributed)
    - random selection
    - performance-based (monitor servers performance metrics- response time/amount of traffic etc to decide how much to distribute)
    - ip-based (hashed) routing (depending on client's ip, hash and direct to selected index server of hash result, this method helps to maximise cache hits since same client ip address is always directed to same server)
        - the way you hash determines whether you are able to maximise cache hits (in cases where there is a change in your servers)
    - path-based routing (different path calls get routed to different server, for eg /api domain will be routed to a particular server and /help to another. helps with separation of concerns)
- most of the time, always good to have multiple load balancer in multiple parts of the systems (different layers) with the different selection strategy that optimise the entire system
- hot spot
    - workload might be spread unevenly when distributing across a set of servers
    - happens when sharding key or hash function are suboptimal (or workload naturally skewed)
    - some servers will receive a lot more traffic than others, hence creating a 'hot spot'
- nginx can be used as a reverse proxy and load balancer

---
### Hashing [works hand in hand in load balancer concept]
- hashing function
    - takes in a specific data type (such as string or an identifier) and outputs a number
    - diff inputs may have same outputs, but a good hashing function minimise these hashing collisions (equivalent to maximising uniformity)
- problem happens when one server crashes or new server is introduced, basic naive modolu function on hashed result will result in cache miss again (clients will be redirected to another index of servers)
- consistent hashing
    - a type of hashing that minimizes the number of keys that need to be remapped when a hash table gets resized
    - often used by load balancers to distribute traffic to servers
    - minimizes numbers of requests that get forwarded to different servers when new servers are added or existing servers are brought down; maximises cache hits
    - visualised as a circle where servers and clients are hashed to a position in the circle
        - where clients go to their nearest clockwise servers for their requests
- rendevzous hashing
    - a type of hashing also coined as highest random weight hashing
    - similarly, allows for minimal re-distribution of mappings when a server goes down or new server is brought in
    - basically each client calculate a scoreset to existing servers and choose the server with highest score; only clients who picked the server that was brought down as the highest score wil be reallocated to a new server
- secure hash algorithms (SHA)
    - a collection of cryptographic hash functions used in industry
        - SHA-3 is the popular choice to use currently

---
### Relational Databases
- database are programs that use disk or memory to do 2 things: record data and query data
    - generally are servers themselves and interact with rest of application through network
    calls
    - some db keeps records in memory, but they are aware that these records will be lost forever if machine/process dies
    - need persistence of these records, thus cannot use memory
        - hence need to write data to disk
    - some machines die often in large scale systems
        - special disk partitions or volumes are used by db processes, and those volumes get recovered even if machines were to go down permanently
-