import sys
sys.path.append('../../ToasterHardware')
sys.path.append('../../ToasterSoftware')
import rpiToaster
import rpiSoftware

def main():
    ### I am a link to the Utilities Class in the rpiToaster.py file
    rpT = rpiToaster.Utilities()
<<<<<<< HEAD
<<<<<<< HEAD
    print str("huvbycvdrszawsdfg")
=======

>>>>>>> 8723f8ea8576c9539a516c6052f54165d202d10e
    print str("rpT.checkHardware"()
    print str("charge!!!!!!!")
    print str("chi rules")
    print str("penguins are awsome")
    print str("what is your name?")
=======
    rpS = rpiSoftware.SoftBread()

    print str(rpT.checkHardware())


    if rpT.triggerPullDown(side="Left"):
        rpS.toastNotify(inEmail='zach@thegiezens.com')
    else:
        str(error)

    print str("Victory Royale")

    return str("Main Function")

>>>>>>> master
if __name__ == "__main__":
    main()
