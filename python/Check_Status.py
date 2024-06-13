import requests

# URL of the web API endpoint
url = 'http://127.0.0.1:8082/api/status'

try:
    # Send POST request
    response = requests.post(url)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request was successful!')
        # Parse the JSON response
        response_data = response.content
        print('Response Status:', response_data)
    else:
        print('Request failed with status code:', response.status_code)
        print('Response content:', response.text)

except requests.exceptions.RequestException as e:
    print('An error occurred:', e)