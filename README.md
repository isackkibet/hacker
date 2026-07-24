# Concurrent Request Sender

A simple Python utility that sends repeated HTTP POST requests to a target endpoint using multiple threads. The script is designed for local testing, development, and authorized performance checks only.

## Features

- Sends a JSON payload to a configurable endpoint
- Uses Python threading to send requests in chunks
- Prints each response status code and response body
- Allows easy adjustment of request volume and concurrency

## Warning

This project can generate a large volume of traffic. Use it only against systems you own or are explicitly authorized to test. Misuse may violate laws, terms of service, and network policies.

## Requirements

- Python 3.8 or newer
- The `requests` package

Install the dependency with:

```bash
pip install requests
```

## Usage

1. Open [index.py](index.py) and review the target URL, headers, payload, and the request settings:
   - `total_requests`
   - `chunk_size`

2. Run the script:

```bash
python index.py
```

3. Monitor the terminal output for the status codes and server responses.

## Configuration Notes

- `total_requests` controls how many POST requests are sent.
- `chunk_size` controls how many requests are launched per thread batch.
- You can customize the endpoint URL, headers, and payload in the script before running it.

## Example

The script currently sends a POST request to a sample contact endpoint with a predefined payload. Update those values to match your own testing target.

## License

No license has been specified for this project yet.
