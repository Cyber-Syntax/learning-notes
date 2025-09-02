# Benchmark results:
# json took 0.000151 seconds
# ujson took 0.000090 seconds
# orjson took 0.000084 seconds
#
# json took 0.000136 seconds
# ujson took 0.000082 seconds
# orjson took 0.000071 seconds

import time
import json
import ujson
import orjson
import requests

# Fetch latest GitHub release data (example repo: python/cpython)
url = "https://api.github.com/repos/AppFlowy-IO/AppFlowy/releases/latest"
response = requests.get(url)
data = response.json()


# Benchmark function
def benchmark_lib(name, dumps_func, loads_func):
    start = time.time()
    # Serialize
    serialized = dumps_func(data)
    # Write to file (for json, ujson use str, for orjson bytes)
    with open(f"latest_release_{name}.json", "wb" if name == "orjson" else "w") as f:
        if name == "orjson":
            f.write(serialized)
        else:
            f.write(serialized)
    # Deserialize
    if name == "orjson":
        loaded = loads_func(serialized)
    else:
        loaded = loads_func(serialized)
    duration = time.time() - start
    print(f"{name} took {duration:.6f} seconds")


if __name__ == "__main__":
    # json functions
    json_dumps = json.dumps
    json_loads = json.loads

    # ujson functions
    ujson_dumps = ujson.dumps
    ujson_loads = ujson.loads

    # orjson functions (orjson.dumps returns bytes)
    orjson_dumps = orjson.dumps
    orjson_loads = orjson.loads

    benchmark_lib("json", json_dumps, json_loads)
    benchmark_lib("ujson", ujson_dumps, ujson_loads)
    benchmark_lib("orjson", orjson_dumps, orjson_loads)
