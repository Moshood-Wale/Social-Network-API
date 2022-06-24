# Social-Network-API

### Objective of this task is to create a simple REST API based social network in Django where Users can sign up and create text posts, as well as view, like, and unlike other Users’ posts. 
### Functional requirements 
##### ● on signup, validate email formatting and only allow signups with valid emails 
##### ● once signed up, enrich the User with geolocation data of the IP that the signup originated from 
##### ● based on geolocation of the IP, check if the signup date coincides with a holiday in the User’s country, and save that info 
### Technical requirements 
##### ● use JWT for user authentication 
##### ● data enrichment must be performed asynchronously, i.e. independently of the signup route API request processing 
##### ● API endpoints functionality must be suitably covered with tests 
##### ● use django-rest-framework library for API 
##### ● implement retries for requests towards 3rd party API 
#### Except for Django and DRF, the candidate is free to choose the rest of the solution stack (libraries, databases, etc.). Design of the API and data model is up to the candidate, with at least the following API endpoints: 
##### ● user signup 
##### ● user login 
##### ● get user data 
##### ● post CRUD 
##### ● post like/unlike 
