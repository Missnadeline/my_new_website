# Don't forget to "pip install requests"
# Could be "sudo pip install request"
import requests

# Get this from http://app.mailgun.com/app/dashboard
def sendmail(sendto,contact,message):
    sender = "Nadelina"
    domain_name = "sandboxbd727a3fd9554694a61fbb98084527ef.mailgun.org"
    a = "f05d7e3cfba42"
    b = "b3ba7d5e4ef3eab21bb-6"
    c = "140bac2-8e96cd93"
    api_key = a + b + c
    
    send_table = {"London":'nadelina.georgieva@ig.com',
                  "Birmingham":'nadelina.georgieva@ig.com',
                  "Manchester":'nadelina.georgieva@ig.com'}
    
    def send_simple_message(sendto,contact,message):
        print("sending email")
        return requests.post(
                "https://api.mailgun.net/v3/{}/messages".format(domain_name),
                auth=("api",api_key),  # authorisation token 
                data={
                        "from": "Nadelina <{0}@{1}>".format(sender, domain_name),
                        "to": [send_table[sendto]],
                        "subject": "Call for Help",
                        "text": message + "\n\nPlease call me back on " + contact
                    },
                        verify='C:\Users\georgin\Desktop\Python\zscaler.cer'
                )
    
    send_simple_message(sendto,contact,message)