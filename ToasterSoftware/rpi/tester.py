import sys
sys.path.append('../../ToasterHardware')
import rpiToaster

def main():
    ### I am a link to the Utilities Class in the rpiToaster.py file
    rpT = rpiToaster.Utilities()

    print str(rpT.checkHardware())

    print str("jellybean rules")

    return str("Main Function")

if __name__ == "__main__":
    main()
