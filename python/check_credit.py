import requests

# URL of the API endpoint
url = 'http://127.0.0.1:8082/api/check_credit'

# Path to the image file you want to send
image_path = './test_image/bank_card_image.png'

# Read the image file and encode it as a base64 string
files = {'image': open(image_path, 'rb')}

try:
    # Send POST request
    response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request was successful!')
        # Parse the JSON response
        response_data = response.content
        print('Response Data :', response_data)
    else:
        print('Request failed with status code:', response.status_code)
        print('Response content:', response.text)

except requests.exceptions.RequestException as e:
    print('An error occurred:', e)
