import boto3, json, logging, os, random, copy, ast
from base64 import b64decode
from urlparse import parse_qs
ENCRYPTED_EXPECTED_TOKEN = os.environ['kmsEncryptedToken']
kms = boto3.client('kms')
expected_token = kms.decrypt(CiphertextBlob=b64decode(ENCRYPTED_EXPECTED_TOKEN))['Plaintext']
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def respond(err=None, res=None, inEmail=None, inSide=None):
    print "respond inEmail: " + str(inEmail)
    print "respond inSide: " + str(inSide)
    return {
        'statusCode': '403' if err else '200',
        'body': err.message if err else json.dumps({"response_type": "Test"}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def check4Toast(inEmail=None,inSide=None):
    print "inEmail: " + str(inEmail)
    print "inSide: " + str(inSide)

    #
    if ('directmessage' in str(channel_name)) and (len(str(text)) > 0):
        return brd_list[random.randrange(0,len(brd_list))]
    else:
        return br_list[random.randrange(0,len(br_list))]

def lambda_handler(event, context):
    params = event.get('body')

    if isinstance(params,dict):
        params = ast.literal_eval(str(params))
    else:
        params = parse_qs(params)
    print "String: " + str(params)
    token = params.get('token')[0]
    inEmail = params.get('inEmail')[0]
    print "If inEmail: " + str(params.get('inEmail'))
    if not params.get('inEmail'):
        inEmail = ""
    else:
        inEmail = params.get('inEmail')[0]

    if token != str(expected_token).split("/")[0]:
        logger.error("Request token (%s) does not match expected", token)
        return respond(Exception('Invalid token'),res=None,inEmail=inEmail,inSide=inSide)
    return respond(err=None,res=check4Toast(inEmail=inEmail,inSide=inSide),inEmail=inEmail,inSide=inSide)