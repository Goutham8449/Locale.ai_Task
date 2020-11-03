# Locale.ai_Task
# **Backend Task**

XRides, delivers about a 200 rides per minute or 288,000 rides per day. Now, they want to send this data to your system via an API. Your task is to create this API and save the data into PostgreSQL.
The API should be designed, keeping in mind the real-time streaming nature of data and the burst of requests at peak times of the day. The user of this API expects an acknowledgment that the data is accepted and a way to track if the request fails.

## **My Solution**
I have used django rest framework to solve the task. The code base a simple serializer-viewset design to accept and list the data being entered through the endpoints. I mainly used two models, one User Model for authentication and Trip model to store the details.

Used JWT authentication for security purposes, the user has to send the login credentials to the /token endpoint in a POST request to get the access and refresh tokens. Upon which the tokens can be used accordingly for Bearer authorization.

| Endpoint | Request method | Request Body | Response |
|--|--|--|--|
|/v1/user/  | GET |  | user_id, username	|
|/v1/user/  | POST| username, password | user_id, username|
|/v1/trip/	| GET | | Trip Object|
|/v1/trip/  | POST |"vehicle_model_id":2, "package_id": 2, "travel_type_id":  2, "from_area_id":  2, "to_area_id":  2, "from_city_id":  2, "to_city_id":  2, "from_date":  "2020-11-02T07:25:50Z", "to_date":  "2020-11-02T07:25:54Z", "online_booking":  true, "mobile_site_booking":  false, "from_lat":  "70.123450", "from_long":  "110.296570", "to_lat":  "71.976500", "to_long":  "108.976300", "car_cancellation":  false,"user":1| Trip Object

## **Ideal Solution**

 

**Handling Data Bursts**
Inorder to handle data bursts I suggest we use a design where all the requests made are stored in an AWS Simple Queue Service(SQS). We can implement a lambda function to pull the messages from this queue at a rate we can set and then handle these messages by inserting the data into the database.

## Comparing Message Queues versus APIs

APIs (application program interface) basically allows for different applications to have a two-way communication with each other. In the API world, when you send a request, you expect a response.


![Image for post](https://miro.medium.com/max/331/1*2YGyF7jXI_RfvqQLd5D1sQ.png)

APIs are 2-way communication.

On the other hand, in the message queue world, when you send a request, you don’t expect a response. Messages sent get stored in a queue until it is read.


![Image for post](https://miro.medium.com/max/401/1*oreexHeQT3t-SI0SwQ_pOg.png)

Message Queues are 1-way communication.

There are pros and cons to both methods — and we use both depending on the situation — but for our current requirement, using message queues made more sense because:

1.  **Decoupled Architecture —** The sender’s job is to send messages to the queue and the receiver’s job is to receive messages from the queue. This separation allows for components to operate independently, while still communicating with each other.
2.  **Fault tolerant**  — If the consumer server is down, the messages would still be stored in queue until the server goes back up and retrieves it
3.  **Scalability** —We can push all the messages in the queue and configure the rate at which the consumer server pulls from it. This way, the receiver won’t get overloaded with network requests and can instead maintain a steady stream of data to process.
4.  **Serverless** — AWS SQS is easy to set up. No administrative overhead and infrastructure to support.
5.  **Single Consumer**  — we only have one microservice pulling from the queue. Once the message is consumed, it is removed from the queue. This is the reason why we opted for SQS instead of SNS (Simple Notification Service) with Pub/Sub messaging.

## **Querying Data for Analytics**
In the solution provided I just used DecimalField to store the location co-ordinates. But if given time and resources, I would suggest we could go for a PostGIS implementation which allows us to handle locations in a more effeciently.

For example, If we get a co-ordinate where the traffic is found to be high, we can retrieve all the nearby trips using the following ORM filter:

`trips_within_radius = queryset.filter
						(  
							location__distance_lt=(  
							Point(-0.2153 45.6402),  
							Distance(m=5000)  
							)  
						)`

