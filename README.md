# Django For APIs Chapter 2: Simple Book API

Got a mac and switched over to it. Programming is now a breeze. 

Chapter 2 of Django For APIs(D4A from now on) reviews the basic concepts from Django For Beginners(D4B) and introduces how to implement APIs with Django using the djangorestframework package.

## APIs
The Django framwork doesn't provide REST API creation out of the box but by  using the django restframework package, we can easily create APIs. 

When comparing to how Django originally does stuff these are the differences/similarities
1. urls.py, models.py -> Mostly the same
2. views.py -> Different from using templates because it doesn't point to the html template anymore. It points to the serializer
3. serializer.py -> Takes the model and turns it into a json format for the view to return.

The book showed how to get a simple GET api to return a book info in Json format and I followed along.

## Tests
They're annoying but can't forget them. The book doesn't cover them in chapter 2 so I added them just to test the API.

## Chapter 1
The previous chapter briefly touches on how TCP/IP and the internet works (the 3 way handshake to establish a connection) and an introduction to REST APIs in general. These are important topics that are common to all web development so I'll cover them here as well.

### Urls/IP
1. url gets typed in 
2. browser uses the DNS(Domain Name Service) to translate the url to an IP address
3. The IP address is used to establish a connection with the desired server

### TCP
The TCP(Transfer Control Protocol) is a method that is used to establish a connection to a remote server.

It follows 3 steps to make a connection:
1. client sends SYN asking to establish a connection
2. server respones with SYN-ACK acknowledgeing the request and passing a connection parameter
3. client sends an ACK back to the server confirming the connection

The book left out how to close a connection so here they are:

To stop a connection, there are 5 steps:
1. client sends a FIN asking to stop a connection and waits(FIN_WAIT_1)
2. server recieves a FIN and sends back ACK to client acknowledgeing that it got the FIN from client
3. while in FIN_WAIT_1, client waits for the ACK from the server and when it gets it it goes into FIN_WAIT_2 state and starts waiting for the final FIN from the server
4. the server sends a FIN after closing processes from the server
5. the client recieves the FIN signal from the server and enters TIME_WAIT state, after the wait the connection closes

### REST verbs
Create --- POST

Read --- GET

Update --- PUT

Delete --- DELETE

### HTTP
HTTP is a request response protocol between 2 computers that have an existing connection

HTTP requests can be sent with headers and a body depending on what the request wants.

A status code can be received after sending a HTTP request.
1. 2xx - success
2. 3xx - redirection
3. 4xx - client side error
4. 5xx - server side error

All HTTP is a stateless protocol meaning that each request/response pair is completely independent of the previous one.

Thus managing state is an important part of web programming. State is stored memory of past interactions.