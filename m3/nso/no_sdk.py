#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Basic consumption of Cisco NSO REST API using the
public Cisco DevNet sandbox (requires reservation).
"""

import requests
import json


def main():
    """
    Execution begins here.
    """

    # Basic variables to reduce typing later. At this time, there is not
    # a NSO always-on DevNet instance, so this is an example from a
    # reserved sandbox. As such, the IP addressing in the URL may change.
    # Check the DevNet NSO site for more information:
    # https://developer.cisco.com/site/nso/
    api_path = "http://198.18.134.28:8080/api"

    # Basic authentication (no tokens) works for our simple example
    basic_auth = ("admin", "admin")

    # For HTTP GET, we need to accept a variety of YANG data encoded as JSON.
    # This technique joins all the list elements together with a comma to
    # create a single, comma-delineated string value for the Accept header.
    accept_list = [
        "application/vnd.yang.api+json",
        "application/vnd.yang.datastore+json",
        "application/vnd.yang.data+json",
        "application/vnd.yang.collection+json",
    ]
    get_headers = {"Accept": ",".join(accept_list)}

    # For HTTP POST, we will only be including JSON encoded YANG data
    post_headers = {"Content-Type": "application/vnd.yang.data+json"}

    # First, issue HTTP GET to collect a list of NSO-managed devices
    get_resp = requests.get(
        f"{api_path}/running/devices/device",
        auth=basic_auth,
        headers=get_headers,
    )
    devices = resp.json()["collection"]["tailf-ncs:device"]

    # Handy debugging output to see device list as JSON
    # print(json.dumps(devices, indent=2))

    # Iterate over list of devices
    for dev in devices:

        # We don't need the full config, so let's just grab the loopbacks
        loopbacks = dev["config"]["tailf-ned-cisco-ios:interface"]["Loopback"]

        # Need to transform a list of dictionaries into a simple list.
        # We could use more advanced techniques here, but a simple
        # loop to append the loopback names to a list works just fine.
        lbs = []
        for lb_dict in loopbacks:
            lbs.append(lb_dict["name"])

        # Print out the basic stats about the device, including loopback list
        # This all prints on a single line for neatness
        print(f"Name: {dev['name']}  IP: {dev['address']}", end="  ")
        print(f"SSH port: {dev['port']}  LB: {lbs}")

        # Add a new loopback interface with the same number as the SSH port
        data = json.dumps(
            {"tailf-ned-cisco-ios:Loopback": [{"name": dev["port"]}]}
        )

        # Issue HTTP POST to apply this change to the specific device, carrying
        # the JSON string defined above as the HTTP body.
        post_resp = requests.post(
            f"{api_path}/running/devices/device/{dev['name']}/config/interface",
            auth=basic_auth,
            headers=post_headers,
            data=data,
        )

        # The POST will fail if the loopback already exists, in which case,
        # do nothing. If the POST succeeds, print out a message stating that
        # a new interface was added.
        if post_resp.ok:
            print(f"  - New loopback added to {dev['name']}")


if __name__ == "__main__":
    main()
