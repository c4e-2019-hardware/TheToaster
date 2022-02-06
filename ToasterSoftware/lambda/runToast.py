import boto3, json, logging, re, os, random, copy, ast
import base64
from base64 import b64decode
from urlparse import parse_qs
ENCRYPTED_EXPECTED_TOKEN = os.environ['kmsEncryptedToken']
kms = boto3.client('kms')
ssm = boto3.client('ssm')
expected_token = kms.decrypt(CiphertextBlob=b64decode(ENCRYPTED_EXPECTED_TOKEN))['Plaintext']
logger = logging.getLogger()
logger.setLevel(logging.INFO)



def respond(err=None, res=None, inEmail=None, inSide=None):
    return {
        'statusCode': '500' if err else '200',
        'body': err if err else json.dumps({"Engageing Toast on Side": str(inSide), "Requester Email was":str(inEmail)}),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

def updateState(inEmail,inSide):
    print("The Stuff: ",inEmail," ",inSide)
    if "left" in inSide.upper().lower():
        print str(ssm.put_parameter(Name='thetoaster_trigger_left',Value='Left',Type='String',Overwrite=True))
        print str(ssm.put_parameter(Name='thetoaster_trigger_left_email',Value=inEmail.upper().lower(),Type='String',Overwrite=True))
    else:
        print str(ssm.put_parameter(Name='thetoaster_trigger_right',Value='Right',Type='String',Overwrite=True))
        print str(ssm.put_parameter(Name='thetoaster_trigger_right_email',Value=inEmail.upper().lower(),Type='String',Overwrite=True))

def makeToast(inEmail=None,inSide=None):
    if not inEmail:
        return respond(err="{'Error':'Bad Email'}",res="no email",inEmail=inEmail,inSide=inSide)
    else:
        result = re.match('(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])', inEmail)
        if result:
            side_result = re.match('([l|L][e|E][f|F][t|T])|([R|r][I|i][G|g][H|h][T|t])',inSide)
            if side_result:
                updateState(inEmail=inEmail,inSide=inSide)
                return respond(err=None,res="{'State':'Updated'}",inEmail=inEmail,inSide=inSide)
            else:
                return respond(err="{'Error':'bad side argument'}",res="make toast",inEmail=inEmail,inSide=inSide)
        else:
            return respond(err="{'Error':'Bad Email'}",res="Bad Email",inEmail=inEmail,inSide=inSide)





def lambda_handler(event, context):
    params=event
    if isinstance(params,dict):
        params = ast.literal_eval(str(params))
    else:
        params = parse_qs(params)

    if not params.get('inEmail'):
        t = ast.literal_eval(params['body'].decode('utf-8', 'ignore'))
        inEmail = t['inEmail']
    else:
        inEmail = params.get('inEmail')
        
    if not params.get('token'):
        t = ast.literal_eval(params['body'].decode('utf-8', 'ignore'))
        token = t['token']
    else:
        token = params.get('token')

    if not params.get('inSide'):
        t = ast.literal_eval(params['body'].decode('utf-8', 'ignore'))
        inSide = t['inSide']
    else:
        inSide = params.get('inSide')
        
    if token != str(expected_token):
        logger.error("Request token (%s) does not match expected", token)
        return respond(Exception('Invalid token '+str(t)+' value, crap'),res=None,inEmail=inEmail,inSide=inSide)
    return makeToast(inEmail=inEmail,inSide=inSide)
