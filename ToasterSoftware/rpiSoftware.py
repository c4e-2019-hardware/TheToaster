#
#
import sys
sys.path.append('../../ToasterHardware')
import rpiToaster
#
#
#
#
class SoftBread:
    def __init__(self):
        """ Init stuff goes here """

    def testSoftwareStuff(self,foo=None,bar=None):
        theString = str("Something " + foo)
        return str("Software Class " + theString)

    def toastNotify(self,inEmail=None):
        if not inEmail:
            import smtplib
            # Import the email modules we'll need
            # https://docs.python.org/2/library/email-examples.html
            from email.mime.text import MIMEText
            msg['Subject'] = ''
            msg['From'] = ''
            msg['To'] = inEmail
            s = smtplib.SMTP('localhost')
            s.sendmail(me, [you], msg.as_string())
            s.quit()
            return True
        else:
            return None

    def ejectToast(self,inSide=None):
        """ For chi to fill out """

