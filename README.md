# network-inventory-enrichment
A python based network automation project that connects to managed devices and enriches inventory data.

Project goals:
- load minimal device inventory details (hostname/IP address/Vendor platform)
- Establish an SSH connection to the network device using Netmiko.
- Collect hardware, software, interface, and neighbor information.
- normalize vendor specific outputs into a common data model that is able to exported to multiple formats.
- provide a foundational platform that can support additional vendors and inventory sources.

Planned features:
- YAML-based inventory source
- Cisco, Fortinet, Arista, and Juniper router/switch/firewall support
- Vendor neutral data model
- Logging and error handling
