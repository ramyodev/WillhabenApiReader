# WillhabenJsonReader
Reads and parses the received product data from the Internal API. 


# About
For each request to a Willhaben search page, Willhaben renders only the first 5 products and passes the rest as Json. This repo offers the ability to read and use this json data. The server receives this data through a request to the internal API. 

Willhaben has several internal apis. The data that is received when loading the page comes from:
https://api.willhaben.at/restapi/v2/
