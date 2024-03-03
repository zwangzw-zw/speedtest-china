# Speedtest for Chinese Servers
# By zwangzw
# This code is licensed under the BSD 3-Clause License.
#
# DISCLAIMER:
# This tool is provided "as is" and without warranties of any kind, whether express or implied.
# You use this tool at your own risk, and you are solely responsible for any consequences arising from using this tool.
#
# DESCRIPTION:
# This is a command-line tool for testing the speed of servers in China. It uses the Speedtest.net API to retrieve a list
# of servers in China and then runs the `speedtest` command for each server to measure the download and upload speeds.
#
# USAGE:
# Before running the tool, make sure you have the `speedtest` command installed on your system. You can obtain the
# `speedtest` command from the Speedtest.net website: https://www.speedtest.net/apps/cli
# Once you have the `speedtest` command, place it in a search path such as /usr/local/bin so that it can be executed
# by the tool.
#
# To use the tool, simply run `python3 speedtest.py` from the command line. By default, the tool will test all servers
# in China. You can also specify which sponsor you want to test by using the following inputs: 1 for 联通 (Unicom),
# 2 for 电信 (Telecom), and 3 for 移动 (Mobile).
#
# OUTPUT:
# The tool will output the name of the server being tested, along with the download and upload speeds in Mbps. If the
# `speedtest` command fails for a server, the tool will print an error message in red. The output will also include colored
# text to indicate the sponsor being tested and the name of the server being tested.
#
# LICENSE:
# This code is licensed under the BSD 3-Clause License. See the LICENSE file for details.


# original one line bash
# curl -A "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0" -s "https://beta.speedtest.net/api/js/servers?engine=js&search=china&limit=200" | jq -r '.[] | select(.country == "China") | "\(.name) \(.sponsor),\(.id)"' | awk -F ',' '{printf "\033[1;31m%s\033[0m\n", $1; system("/opt/speedtest -s" $2)}'

import sys
import subprocess
import json
import requests



print("\033[1mPlease use the following inputs to test sponsors:\033[0m")
print("\033[1;36m1: \033[1m联通 (Unicom)\033[0m (\033[1;34mpython3 speedtest.py 1\033[0m)")
print("\033[1;36m2: \033[1m电信 (Telecom)\033[0m (\033[1;34mpython3 speedtest.py 2\033[0m)")
print("\033[1;36m3: \033[1m移动 (Mobile)\033[0m (\033[1;34mpython3 speedtest.py 3\033[0m)")
print("\033[1;36mNo input: \033[1mTest all sponsors\033[0m (\033[1;34mpython3 speedtest.py\033[0m)\n")


# Send a GET request to the Speedtest API to get servers in China
url = "https://beta.speedtest.net/api/js/servers?engine=js&search=china&limit=200"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"}
response = requests.get(url, headers=headers)



server_data = json.loads(response.stdout.decode())

# Create a dictionary to store the servers for each sponsor
server_groups = {
    "China Unicom": [],
    "China Telecom": [],
    "China Mobile": []
}

# Iterate over the servers in China and group them by sponsor
for server in server_data:
    if server["country"] != "China":
        continue

    # Determine the sponsor of the server based on the "sponsor" field
    sponsor_name = server["sponsor"]
    if "联通" in sponsor_name or "Unicom" in sponsor_name:
        server_groups["China Unicom"].append(server)
    elif "电信" in sponsor_name or "Telecom" in sponsor_name:
        server_groups["China Telecom"].append(server)
    elif "移动" in sponsor_name or "Mobile" in sponsor_name:
        server_groups["China Mobile"].append(server)

# Select servers based on input options
if len(sys.argv) > 1:
    input_option = sys.argv[1]
else:
    input_option = ""
if input_option == "1":
    selected_servers = server_groups["China Unicom"]
    selected_sponsor = "联通 (Unicom)"
elif input_option == "2":
    selected_servers = server_groups["China Telecom"]
    selected_sponsor = "电信 (Telecom)"
elif input_option == "3":
    selected_servers = server_groups["China Mobile"]
    selected_sponsor = "移动 (Mobile)"
else:
    selected_servers = server_data
    selected_sponsor = "all sponsors"

print(f"\033[1mTesting servers hosted by {selected_sponsor}:\033[0m")


# Iterate over the selected servers and run the speedtest command
for sponsor, servers in server_groups.items():
    if not servers:
        continue
    if selected_servers != server_data and servers != selected_servers:
        continue
    #print(f"\n\033[1;33mTesting servers hosted by {sponsor}:\033[0m")
    for server in servers:
        sponsor_name = server["sponsor"]
        server_name = server["name"]
        server_id = server["id"]
        print(f"\033[1;31m{sponsor_name} {server_name}\033[0m")
        try:
            subprocess.run(["speedtest", "-s", server_id], check=True)
        except subprocess.CalledProcessError:
            print(f"\033[1;31mError:\033[0m Failed to test server {server_name} ({server_id})")
