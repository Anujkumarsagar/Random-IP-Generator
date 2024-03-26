import win32com.client

def change_ip_address(ip_address, subnet_mask, gateway):
    # Create a WMI object to interact with Windows networking
    wmi = win32com.client.GetObject("winmgmts:")

    # Query for network adapters
    adapters = wmi.ExecQuery("SELECT * FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled=True")

    for adapter in adapters:
        # Set IP address, subnet mask, and gateway
        adapter.SetGateways(DefaultIPGateway=[gateway])
        adapter.EnableStatic(IPAddress=[ip_address], SubnetMask=[subnet_mask])

        # Apply changes
        adapter = None

# Example usage
change_ip_address("192.168.1.100", "255.255.255.0", "192.168.1.1")
