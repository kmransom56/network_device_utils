# network_device_utils

Reusable Python package for fast OUI (MAC-to-manufacturer) lookups, device enrichment, and passive device learning for network applications.

## Features
- Fast, local OUI lookup using merged Nmap, IEEE, and Wireshark sources
- Device enrichment API (adds manufacturer info to device dicts)
- Passive device learning and caching
- Ready for use in enterprise network and security tools

## Installation
```
pip install requests apscheduler
```

## Usage

### OUI Lookup
```python
from network_device_utils.oui_manager import OUILookup
oui_lookup = OUILookup()
manufacturer = oui_lookup.get_manufacturer('00:1A:2B:3C:4D:5E')
print(manufacturer)
```

### Device Enrichment
```python
from network_device_utils.device_enrichment import enrich_device
from network_device_utils.oui_manager import OUILookup
oui_lookup = OUILookup()
device = {'mac': '00:1A:2B:3C:4D:5E', 'ip': '192.168.1.10'}
enriched = enrich_device(device, oui_lookup)
print(enriched)
```

### Passive Device Learning
```python
from network_device_utils.device_learner import DeviceLearner
learner = DeviceLearner()
device = {'mac': '00:1A:2B:3C:4D:5E', 'ip': '192.168.1.10'}
learner.learn(device)
print(learner.get_device('00:1A:2B:3C:4D:5E'))
```

## OUI Database
- Use the provided merge script to generate `data/merged_oui.pkl` from Nmap, IEEE, and Wireshark sources.
- Schedule regular updates using the provided scheduler script.

## License
MIT 