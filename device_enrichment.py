def enrich_device(device, oui_lookup):
    mac = device.get('mac')
    if mac:
        device['manufacturer'] = oui_lookup.get_manufacturer(mac)
    else:
        device['manufacturer'] = 'Unknown'
    return device 