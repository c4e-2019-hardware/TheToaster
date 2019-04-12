import sys
sys.path.append('../../ToasterHardware')
import rpiToaster

def main():
    ### I am a link to the Utilities Class in the rpiToaster.py file
    rpT = rpiToaster.Utilities()

    print str("rpT.checkHardware"())
    print str("charge!!!!!!!")
    print str("chi rules")
    print str("penguins are awsome")
    print str("what is your name?")
if __name__ == "__main__":
    main()