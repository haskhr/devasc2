# Cisco Network Services Orchestrator (NSO) Setup
Unlike other sandboxes demonstrated in this course, NSO does not come
pre-installed and there are no test devices immediately at our disposal.
There is also no simplified "always-on" sandbox for quick testing.
You'll need to manually install NSO and build a test network to get
any meaningful value from testing the NSO REST API.

## Reservations
Reservable sandboxes, at the time of this writing, are hosted in Cisco dCloud.
When the reservation is active, you'll be given a VPN target, username,
and password. To learn more about dCloud, visit `https://dcloud.cisco.com/`

## VPN details
You'll need to install the `openconnect` Linux package so your devbox can
VPN into dCloud. If you have a graphical interface on your devbox, you can
use the Cisco Anyconnect application. If you only have the shell, you
can install it using these commands:
  * On RedHat-based distributions: `yum install openconnect`
  * On Debian-based distributions: `apt install openconnect`

> Example usage: `openconnect -b dcloud-lon-anyconnect.cisco.com`

Be sure to use your own VPN target, then answer the interactive username
and password prompts using your temporary credentials.

# Relevant files
There are (3) extra files related to the initial NSO configuration:
  * `setup.sh`: Initial NSO installation, mostly ported from the install guide
  * `build_netsim.sh`: Used to add devices to netsim and start the simulation
  * `netsim_config.txt`: NSO CLI commands to register netsim devices to NSO

## Resources
This particular tutorial was the inspiration for this demo and helps give
additional context around the setup.
`https://github.com/NSO-developer/nso-5-day-training/blob/master/Day1Labs/lab1_Creating_Your_First_Network.md`
