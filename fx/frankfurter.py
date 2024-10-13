import pickle, os

# https://www.frankfurter.app/docs/


class Frankfurter:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w"):
                pass

    def get(self, k):
        # Read cache
        cache = dict()
        with open(self.path, "rb") as f:
            if os.fstat(f.fileno()).st_size != 0:
                cache = pickle.load(f)
        if k in cache:
            return cache[k]

        # Get from API
        value = self.read(k)

        # Write cache
        if value is not None:
            cache[k] = value
            with open(self.path, "wb") as f:
                pickle.dump(cache, f)

        return value

    def read(self, k):
        return 2
