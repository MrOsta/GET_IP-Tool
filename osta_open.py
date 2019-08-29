# importing ~ socket libary - level-low networking interface
import socket



class colors:
    RED = '\33[31m'
    GOLD = '\33[33m'
    BLUE = '\33[34m'
    GREEN = '\33[92m'
    GHOST = '\33[5m'

    ENDC = '\033[0m'
# added function for get ip by host name tool
def getipbyhostname_tool():
    yourhostname = socket.gethostname()  # yourhostname var

    yourhostnameip = socket.gethostbyname(yourhostname)
    print(colors.GREEN + "\n Your HostName: ", yourhostname + colors.ENDC)
    print(colors.GREEN + "\n Your HostNameIP: ", yourhostnameip + colors.ENDC)
    while 1:

        try:

                print(colors.RED + "\n Type \" c \" To End The While" + colors.ENDC)


            # I LOVE YOU WHO SEE MY CODE :D < SMILE >
                gethostname = input(colors.GOLD + "\n  Give Me Website Link: " + colors.GOLD)
                if gethostname == "c":
                    print("Thanks For Try My Program <3")
                    break;

                else:
                    gethostnameip = socket.gethostbyname(gethostname)

                    print(colors.GREEN + "\n \n INFO: \n Website Link: {} \n Website Ip: {} ".format(gethostname,gethostnameip) + colors.ENDC)
        except:
            print(colors.RED + "\n \n ERROR: \n Please Check Your Input \n Or Contact Me:- \n Twitter: @MrOsta_ \n \n" + colors.ENDC)


# ITS ME , Osta :D
print("\n \n ")
print(colors.RED+ "#######  #####  #######    # " + colors.ENDC)
print(colors.GREEN+ "#     # #     #    #      # #" + colors.ENDC)
print(colors.GOLD + "#     # #          #     #   #" +colors.ENDC)
print(colors.GOLD+ "#     #  #####     #    #     #"+ colors.ENDC)
print(colors.GOLD + "#     #       #    #    #######"+ colors.ENDC)
print(colors.GREEN +"#     # #     #    #    #     #"+ colors.ENDC)
print(colors.RED + "#######  #####     #    #     # "+ colors.ENDC)


print("ــــــــــــــــــــــــــــــــــــــــــــ\n")

print(colors.GOLD + "< Welcome to Get IP By HostName Tool :D > \n" + colors.ENDC )

print(colors.GOLD + "Lets Get Started! \n " + colors.ENDC)


auth = input(colors.GREEN + "Need to try? [ONLY \" y / Y \"]: "+ colors.ENDC)

# AUTH
if (auth == "y" or auth == "Y"):
    print(colors.GREEN + "OK!" + colors.ENDC)
    getipbyhostname_tool()

else:
    print("STOP TROLLING PLEASE -.-")