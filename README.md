# Login-microservice

## This is my login microservice using [fastapi](https://fastapi.tiangolo.com/)

**although not perfect this is a good example of a microservice you could deploy to something like aws with this example i will walk through the process of deploying to aws as a serverless application perfect for a microservice**


reasons why i did this; when i heard about serverless and microservices i thought they were a great idea, moving away from giant code bases, into smaller well managed _chunks_ of code.

I found fastapi after looking for more information about Flask and thought it would be a great stepping off point and moved into looking into fastapi instead.

_first you will need to clone the repo_
**next you will need to install a virtual enviroment, for this example i used virtualenv**

[1] pip install virtualenv

[2] virtualenv venv

[3] source venv/bin/activate

[4] pip install pip install -r requirements.txt

[5] _ensure everything is working_

[6] uvicorn app.main:app --reload

[7] in a web browser go to [localhost:8000/docs](127.0.0.1:8000/docs)

## Creating the lambda function zip
* first you will need all of the source code and modules in a zip folder.
* cd venv/lib/python3.8 "or your python version" /site-packages
* zip -r9 ../../../../functions.zip .
* zip -g ./functions.zip -r app

## On aws

### [1] s3 bucket
* go to s3 bucket and upload that functions.zip


### [2] lambda
* to go aws lambda follow create function author from scratch
* find function code then upload from s3
* once upload go to basic settings > edit
* change handler to app.main.handler
* change the amount of memory if you like this should be fine on the default 128MB
* at the top of the page test the function
* select apigateway-aws-proxy as the event template and choose a name for this text
* get / should be find and return a variation of hi
* if this is working, then you've done the lambda section


### [3] api gateway
* now to go api gateway
* select rest api
* choose rest and new api, then give it a name
* click action create method and select any
* check proxy intergration then select the lambda function you created
* go to action again create resource
* check configure as a proxy
* check enable api gateway CORS
* create resource
* choose the same lambda function
* save
* deploy api
* choose stage and give it a name
* you should now have something that looks like https://something.execute-api.eu-west-1.amazonaws.com/stagename

**with this you can now connect this api to anything you like websites and native applications**

_you just need to add any endpoints onto that url_ 

you can test this on something like post man do a get request for your-endpoint/stagename/lambda-endpoint

**additional steps would be to add a database base like aws rds as its a zipped file within s3 so the database wouldnt be accessable**