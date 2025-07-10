import pickle
import os

class DeviceLearner:
    def __init__(self, cache_file='device_cache.pkl'):
        self.cache_file = cache_file
        self.cache = self._load_cache()

    def _load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'rb') as f:
                return pickle.load(f)
        return {}

    def learn(self, device):
        mac = device.get('mac')
        if mac:
            self.cache[mac] = device
            self._save_cache()

    def _save_cache(self):
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.cache, f)

    def get_device(self, mac):
        return self.cache.get(mac) 