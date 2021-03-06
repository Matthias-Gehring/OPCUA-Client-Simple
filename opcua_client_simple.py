# Install on windows:
# pip install opcua

import sys
sys.path.insert(0, "..")

from opcua import Client
from opcua import ua

import logging
logging.basicConfig()
#logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    
    logging.info("Read/Write variable with OPC-UA")
    
    client = Client("opc.tcp://localhost:4840")
    #client = Client("opc.tcp://admin@192.168.2.1:4840") #connect using a user
    try:
        client.connect()

        # Get UA nodes in root
        root = client.get_root_node()

        # get a specific variable node knowing its node id
        #-----------------------------------------------------------------------------
        # read int16 variable
        var = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.uiCycleCounter")
        print("Value read from int16 variable: %s" % var.get_value())
        logging.info("Value read from int16 variable")

        # write int16 value
        newValue = var.get_value() + 1
        var.set_value(newValue, ua.VariantType.Int16)
        print("Value read from int16 variable (after write +1) : %s" % var.get_value())

        # read string variable
        var1 = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.sInfoMsg")
        print("Value read from string variable: %s" % var1.get_value())

        # write string value
        var1.set_value("Cool, I can write the value", ua.VariantType.String)
        print("Value read from string variable (after write): %s" % var1.get_value())
        
        # Now getting a variable node using its browse path
        #-----------------------------------------------------------------------------
        myvar = root.get_child(["0:Objects", "2:DeviceSet", "4:CODESYS Control Win V3 x64", "4:Resources", "4:Application", "3:GlobalVars", "4:GVL", "4:uiCycleCounter"])
        print("Value read from int16 variable using its browse path: %s" % myvar.get_value())

    finally:
        client.disconnect()
