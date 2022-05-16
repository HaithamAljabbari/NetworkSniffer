try:
    import scapy.all as scapy
    from termcolor import cprint
    import pyfiglet
    from rich.console import Console
except ImportError:
    print("You do not have at least one of the following libraries: scapy, rich, termcolor, pyfiglet")
logo = pyfiglet.figlet_format("SOSAKORNUT")
cprint(logo, "cyan", "on_blue")

# this is a variable for the console 
console = Console()

# This sniffs packets in a while loop per second
while True:
    try:
        capture = scapy.sniff(count=1)
        scapy.wrpcap("sniffed.pcap", capture)
        console.log(capture.summary())
    except KeyboardInterrupt:
        cprint("Exited", "cyan", "on_red")
        exit(0)
