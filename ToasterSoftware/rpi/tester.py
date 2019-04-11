from ToasterHardware import rpiToaster as rpiToaster

def main():
    print rpiToaster.Utilities.checkHardware()
    return str("Main Function")

if __name__ == "__main__":
    main()
