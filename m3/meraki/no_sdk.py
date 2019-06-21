#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Basic consumption of Cisco Meraki REST API using the
public Cisco DevNet sandbox.
"""

import requests


def main():
    """
    Execution begins here.
    """

    # Basic variables to reduce typing later. Since Meraki is cloud-based,
    # we target the main Meraki site rather than a dedicated resource. Our
    # API key identifies who we are (in this case, an exploratory read-only
    # user in the DevNet sandbox. The API key is provided by DevNet
    # on their website, but may change over time. Be sure to check here:
    # https://developer.cisco.com/meraki/
    api_path = "https://dashboard.meraki.com/api/v0"
    headers = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
    }

    # This variable will store the DevNet organization ID. We need this to
    # drill deeper to get a list of networks within our environment.
    devnet_id = 0

    # Perform a GET request to collect the list of organizations from
    # the sandbox. You'd think there would only be one, but ...
    response = requests.get(f"{api_path}/organizations", headers=headers)
    orgs = response.json()
    print("Organizations discovered:")

    # Iterate over each org. This loop does double-duty. It prints out each
    # discovered organization, but also performs a linear search for the
    # DevNet ID. If the ID is found, it is stored in the variable above.
    for org in orgs:
        print(org["name"])
        if "devnet" in org["name"].lower():
            devnet_id = org["id"]

    # If the devnet ID has been defined (ie, is not 0 in this context)
    # then we will perform another GET request to collect the DevNet
    # networks.
    if devnet_id:
        response = requests.get(
            f"{api_path}/organizations/{devnet_id}/networks", headers=headers
        )
        networks = response.json()

        # Print out the networks along with their network IDs
        print(f"\nNetworks seen for DevNet org ID {devnet_id}:")
        for network in networks:
            print(f"Network ID: {network['id']}  Name: {network['name']}")


if __name__ == "__main__":
    main()
