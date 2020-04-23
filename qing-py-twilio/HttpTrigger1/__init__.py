import logging
from twilio.rest import Client
import azure.functions as func
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #skeleton starts
   #1 account_sid = "AC2016968f3f79de24cfc298fcc2ac19d8" #need to substitute
   #1 auth_token  = "c07eafcffe01e315d9572cfb22283bc6" #need to substitute
   #1 client = Client(account_sid, auth_token)
   #1 message = client.messages.create(
   #1     to="+8613304843608", #need to substitute
   #1     from_="+19798594714", #need to substitute
   #1     body="Hello from Python!") #need to substitute

   #1 print(message.sid)

    #skeleton ends

    #sendgrid starts#

    message = Mail(
        from_email='v-yuran@microsoft.com',
        to_emails='v-yuran@microsoft.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    #try:
   # message.add_bcc("v-yuran@microsoft.com")
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
   # except Exception as e:
   #     print(e.message)
    #sendgrid ends#
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
