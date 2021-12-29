import nmap

while True:
    # User menu
    print("""\nWhat do you want to do?\n
                1 - Get detailed info about a device
                2 - Scan the network for open ports
                e - Exit the application""")

    user_input = input("\nEnter your option: ")

    if user_input == "1":
        nmap_instance = nmap.PortScanner()

        ip = input("\nPlease enter the IP address to scan: ")

        print("\nThis may take a couple of minutes...\n")

        scan = nmap_instance.scan(ip, '1-1024', '-v -sS -sV -O -A')

        print("\n= = = = = = = HOST {} = = = = = = =".format(ip))

        print("\n\nGENERAL INFO")

        # MAC address
        try:
            mac = scan['scan'][ip]['addresses']['mac']
            print("\n-> MAC address: {}".format(mac))
        except KeyError:
            pass

        # OS
        os = scan['scan'][ip]['osmatch'][0]['name']
        print("-> Operating system: {}".format(os))

        # Uptime
        uptime = scan['scan'][ip]['uptime']['lastboot']
        print("-> Device uptime: {}".format(uptime))

        # Port states
        print("\n\nPORTS\n")

        for port in list(scan['scan'][ip]['tcp'].items()):
            print("-> {} | {} | {}".format(port[0], port[1]['name'], port[1]['state']))

        print("\n\nOTHER INFO\n")

        print("-> NMAP command: {}".format(scan['nmap']['command_line']))

        version = str(nmap_instance.nmap_version()[0]) + "." + str(nmap_instance.nmap_version()[1])
        print("-> NMAP version: {}".format(version))

        print("-> Time elapsed: {}".format(scan['nmap']['scanstats']['elapsed'] + "seconds"))

        print("-> Time of scan: {}".format(scan['nmap']['scanstats']['timestr']))
        print("\n\n")

        continue

    elif user_input == "2":
        nmap_instance = nmap.PortScanner()

        print("\nThis may take a couple of minutes...\n")

        scan = nmap_instance.scan(ports='1-1024', arguments='-sS -iL ip.txt')

        for device in scan['scan']:
            print("\nPorts open on {}:".format(device))
            for port in scan['scan'][device]['tcp'].items():
                if port[1]['state'] == 'open':
                    print("-->" + str(port[0]) + "|" + port[1]['name'])

        continue

    elif user_input == "e":
        print('\nExiting program...\n')

        break

    else:
        print("\nInvalid input. Try again!\n")

        continue
