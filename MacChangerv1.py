import subprocess
import optparse
import re

def get_user_datas():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac_adress",dest="macadress",help="change to mac adress!")
    return parse_object.parse_args()
def changing_mac_adress(user_interface,user_macadress):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_macadress])
    subprocess.call(["ifconfig",user_interface,"up"])
def control_maccing(interface):
    ifconfig_output=subprocess.check_output(["ifconfig",interface])
    mac_now=re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_output))
    if mac_now:
        return mac_now.group(0)
    else:
        return None

print("Mac Changer is Started !")
(user_inputs, data_arguments) = get_user_datas()

changing_mac_adress(user_inputs.interface,user_inputs.macadress)

final_mac_adress = control_maccing(str(user_inputs.interface))

if final_mac_adress == user_inputs.macadress:
    print("Mac Changed Succesfully !")

else:
    print("Mac not Changed !")
