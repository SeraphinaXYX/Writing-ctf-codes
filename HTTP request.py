import requests
import json
import time
from datetime import datetime

def log_request(method, url, **kwargs):
    """Send a request and log status code, Content-Type, and latency."""
    start = time.time()
    response = requests.request(method, url, **kwargs)
    latency = round(time.time() - start, 4)

    return {
        "timestamp": datetime.now().isoformat(),
        "method": method,
        "url": url,
        "status_code": response.status_code,
        "content_type": response.headers.get("Content-Type", "N/A"),
        "latency_seconds": latency
    }

def main():
    base_url = "https://httpbin.org"
    results = []

    # GET requests
    print("Sending GET /get ...")
    results.append(log_request("GET", f"{base_url}/get"))

    print("Sending GET /headers ...")
    results.append(log_request("GET", f"{base_url}/headers"))

    print("Sending GET /status/200 ...")
    results.append(log_request("GET", f"{base_url}/status/200"))

    print("Sending GET /status/404 ...")
    results.append(log_request("GET", f"{base_url}/status/404"))

    # POST requests
    print("Sending POST /post (JSON body) ...")
    results.append(log_request("POST", f"{base_url}/post",
                               json={"name": "Alice", "age": 25}))

    print("Sending POST /post (form data) ...")
    results.append(log_request("POST", f"{base_url}/post",
                               data={"username": "bob", "password": "secret"}))

    # Save results to JSON
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nDone! {len(results)} requests logged to results.json")

    # Print summary
    for r in results:
        print(f"  {r['method']} {r['url']} -> {r['status_code']} "
              f"({r['content_type']}) {r['latency_seconds']}s")

if __name__ == "__main__":
    main()
