#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Basic consumption of Cisco ACI REST API using the
public Cisco DevNet sandbox.
"""

import requests


def main():
    """
    Execution begins here.
    """

    # Basic variables to reduce typing later. The API path is just the
    # always-on ACI simulator in DevNet. The body represents a nested dict
    # to generate a token and requires a JSON string. These login credentials
    # are available here, be sure to check for updates:
    # https://developer.cisco.com/site/aci/
    api_path = "https://sandboxapicdc.cisco.com/api"
    body = '{"aaaUser": {"attributes": {"name": "admin", "pwd": "ciscopsdt"}}}'

    # The ACI sandbox uses a self-signed cert at present, so let's ignore any
    # obvious security warnings for now.
    requests.packages.urllib3.disable_warnings()

    # Perform a POST request with the basic login information to get a token.
    # The ACI API will parse JSON from the string body for login. Then, extract
    # the token from the large JSON structure that is returned.
    response = requests.post(
        f"{api_path}/aaaLogin.json", data=body, verify=False
    )
    token = response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]

    # For future authentication, the token must be supplied inside of a cookie
    # named # "APIC-Cokkie=(token goes here)", so build a dict for these
    # headers. In this case, we are collecting a list of ACI endpoint
    # groups (EPGs).
    headers = {"Cookie": f"APIC-Cookie={token}"}
    response = requests.get(
        f"{api_path}/class/fvAEPg.json", headers=headers, verify=False
    )
    epgs = response.json()

    # The API call above returns a list of dics, so iterate over the list
    # contained in "imdata" and extract the "dn" (the distinguished name)
    # from each dict.
    print("EPGs found:")
    for epg in epgs["imdata"]:
        print(f"EPG Name: {epg['fvAEPg']['attributes']['dn']}")


if __name__ == "__main__":
    main()
