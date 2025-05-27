from py.functions import Generate_Key

try:
    #Writes Key in Keyfile
    with open("./key/key.key", "r") as key_file:
        if key_file.read() != "":
            input = input("do you want to Renew your Key? [y, n] ")
            if input == "y":
                Generate_Key()
        else:
            Generate_Key()

except Exception as e:
    print('Error by checking Key: ', e)
