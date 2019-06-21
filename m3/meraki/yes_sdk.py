from meraki.meraki_client import MerakiClient

x_cisco_meraki_api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
client = MerakiClient(x_cisco_meraki_api_key)

# [{'id': 681155, 'name': 'Lyoli'}, {'id': 865776, 'name': 'Cisco Live US 2019'}, {'id': 52636, 'name': 'Forest City - Other'}, {'id': 549236, 'name': 'DevNet Sandbox'}]
orgs = client.organizations.get_organizations()
cust_id = 0
for org in orgs:
    if "devnet" in org["name"].lower():
        cust_id = org["id"]

if cust_id:
