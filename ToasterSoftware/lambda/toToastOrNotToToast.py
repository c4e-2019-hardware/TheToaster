import boto3, json, logging, os, random, copy, ast
from base64 import b64decode
from urlparse import parse_qs
ENCRYPTED_EXPECTED_TOKEN = os.environ['kmsEncryptedToken']
kms = boto3.client('kms')
ssm = boto3.client('ssm')
expected_token = kms.decrypt(CiphertextBlob=b64decode(ENCRYPTED_EXPECTED_TOKEN))['Plaintext']
logger = logging.getLogger()
logger.setLevel(logging.INFO)

inEmail='foo@bar.org'
inSide='Left'

def respond(err=None, res=None, inEmail=None, inSide=None):
    return {
        'statusCode': '403' if err else '200',
        'body': err.message if err else json.dumps({'loadSide': str(res[0]), 'sendEmail':str(res[1])}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def check4Toast():
    useLeft = None
    useRight = None
    thetoaster_trigger_left_email_dict = ssm.get_parameter(Name='thetoaster_trigger_left_email', WithDecryption=True)
    thetoaster_trigger_right_email_dict = ssm.get_parameter(Name='thetoaster_trigger_right_email', WithDecryption=True)
    thetoaster_trigger_left_dict = ssm.get_parameter(Name='thetoaster_trigger_left', WithDecryption=True)
    thetoaster_trigger_right_dict = ssm.get_parameter(Name='thetoaster_trigger_right', WithDecryption=True)
    
    thetoaster_trigger_left_email = str(thetoaster_trigger_left_email_dict['Parameter']['Value'])
    thetoaster_trigger_right_email = str(thetoaster_trigger_right_email_dict['Parameter']['Value'])
    thetoaster_trigger_left = str(thetoaster_trigger_left_dict['Parameter']['Value'])
    thetoaster_trigger_right = str(thetoaster_trigger_right_dict['Parameter']['Value'])

    if not "false" in thetoaster_trigger_left:
        useLeft = "true"
        print str(ssm.put_parameter(Name='thetoaster_trigger_left',Value='false',Type='String',Overwrite=True))
        print str(ssm.put_parameter(Name='thetoaster_trigger_left_email',Value='None',Type='String',Overwrite=True))
        print str('We reset the Left Side')
        return ['Left',str(thetoaster_trigger_left_email)]
    else:
        if not "false" in thetoaster_trigger_right:
            useRight = "true"
            print str(ssm.put_parameter(Name='thetoaster_trigger_right',Value='false',Type='String',Overwrite=True))
            print str(ssm.put_parameter(Name='thetoaster_trigger_right_email',Value='None',Type='String',Overwrite=True))
            print str('We reset the Right Side')
            return ['Right',str(thetoaster_trigger_right_email)]
        else:
            useRight = None
            return ['None','donotrespond@lighthca.org']
    
    useLeft = None
    useRight = None
        
    return ['None','donotrespond@lighthca.org']

def lambda_handler(event, context):
    params = event
    return respond(err=None,res=check4Toast(),inEmail=inEmail,inSide=inSide)
