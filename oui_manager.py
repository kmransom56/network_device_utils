import pickle
import os

class OUILookup:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), 'data/merged_oui.pkl')
        with open(db_path, 'rb') as f:
            self.oui_map = pickle.load(f)

    def get_manufacturer(self, mac):
        prefix = mac.upper().replace(':', '').replace('-', '')[:6]
        return self.oui_map.get(prefix, 'Unknown') 