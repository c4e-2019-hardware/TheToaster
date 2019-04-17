import sys
sys.path.append('../../ToasterHardware')
sys.path.append('../../ToasterSoftware')
import rpiToaster
import rpiSoftware

def main():
    ### I am a link to the Utilities Class in the rpiToaster.py file
    rpT = rpiToaster.Utilities()
    rpS = rpiSoftware.SoftBread()

    print str(rpT.checkHardware())


    if rpT.triggerPullDown(side="Left"):
        rpS.toastNotify(inEmail='zach@thegiezens.com')
    else:
        str(error)

    print str("Victory Royale")

    return str("Main Function")

if __name__ == "__main__":
    main()
