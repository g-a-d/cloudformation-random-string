import boto3
import random
import string
import uuid
import httplib
import urlparse
import json

"""
If included in a Cloudformation build as a CustomResource, generate a random string of length
given by the 'length' parameter.
By default the character set used is upper and lowercase ascii letters plus digits.
If the 'punctuation' parameter is specified this also includes punctuation
"""

def send_response(request, response, status=None, reason=None):
    if status is not None:
        response['Status'] = status

    if reason is not None:
        response['Reason'] = reason

    if 'ResponseURL' in request and request['ResponseURL']:
        url = urlparse.urlparse(request['ResponseURL'])
        body = json.dumps(response)
        https = httplib.HTTPSConnection(url.hostname)
        https.request('PUT', url.path+'?'+url.query, body)

    return response


def lambda_handler(event, context):

    response = {
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'Status': 'SUCCESS'
    }

    if 'PhysicalResourceId' in event:
        response['PhysicalResourceId'] = event['PhysicalResourceId']
    else:
        response['PhysicalResourceId'] = str(uuid.uuid4())

    if event['RequestType'] == 'Delete':
        return send_response(event, response)

    try:
        length = int(event['ResourceProperties']['Length'])
    except KeyError:
            return send_response( event, response, status='FAILED', reason='Must specify a length')
    except:
            return send_response( event, response, status='FAILED', reason='Length not an integer')
    try:
        punctuation = event['ResourceProperties']['Punctuation']
    except KeyError:
        punctuation = False
    valid_characters = string.ascii_letters+string.digits
    if punctuation:
        valid_characters = valid_characters + string.punctuation

    random_string = ''.join(random.choice(valid_characters) for i in range(length))
    response['Data']   = { 'RandomString': random_string }
    response['Reason'] = 'Successfully generated a random string'
    return send_response(event, response)
