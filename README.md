# code-21-04-2021-anujaggarwal

I have written solution for batch system.
In this you will provide the location of the file containing all the json data for which we have to find the required data and it will 
produce a data.json containing the required data for which you can create a metrics according to business logic.For scaling, we can use spark for file distributing.

Also, if we want to build a live system where we create a server and through api, we can take the json request and give the json response to the user.
For scaling such system, we just need to take a distributed system concept where the load balancer will distribute the apis hits and give the output in less time. The logic 
will be same as I have written.
