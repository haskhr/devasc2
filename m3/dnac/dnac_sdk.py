#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Basic consumption of the Cisco Digital Network Architecture
(DNA) Center software development kit (SDK).
"""

from dnacentersdk import api



def main():
    """
    Execution begins here.
    """

    dnac = api.DNACenterAPI(
        username="devnetuser",
        password="Cisco123!",
        base_url='https://sandboxdnac.cisco.com'
    )

    devices = dnac.devices.get_device_list()
   
    # Debugging line; pretty-print JSON to see structure
    import json; print(json.dumps(devices, indent=2))

    new_device_dict = {
        "ipAddress": ["192.0.2.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": 1,
        "snmpTimeout": 60,
        "cliTransport": "ssh",
        "userName": "nick",
        "password": "secret123!",
        "enablePassword": "secret456!",
    }

    # Unpack the new device dictionary into keyword arguments (kwargs) and
    # pass into the SDK. This also performs data validation, so if we
    # have the wrong data or miss a required field, it tells us.
    # add_resp = dnac.devices.add_device(**new_device_dict)

    # Debugging line; pretty-print JSON to see structure
    # import json; print(json.dumps(add_resp, indent=2))

   
    # del_resp = dnac.devices.delete_device_by_id("5c20971b-6c4a-4fa4-9dc9-2f7babe54b0b")


if __name__ == "__main__":
    main()
