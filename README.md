<div align="center">
   <h1>ID Document Recognition Linux SDK</h1>
   <img src=https://miniai.live/wp-content/uploads/2024/02/logo_name-1-768x426-1.png alt="MiniAiLive Logo"
   width="300">
</div>

## Welcome to the [MiniAiLive](https://www.miniai.live/)!
Welcome to the ID Document Recognition SDK! This SDK provides powerful tools for recognizing and extracting information from ID documents. The SDK is available for both Windows and Linux platforms and includes an API for integration.

Reduce drop-off and boost conversions with ID scanning and verification solutions. Quickly and securely capture, extract, and verify data from diverse ID cards, passports, driver’s licenses, and other documents with our proven, AI-first approach. Designed to fit seamlessly together, our technology can be integrated as a fully-bundled identity document verification solution or as separate modules via developer-friendly mobile or server SDK. Try it out today!

> **Note**
>
> - Our SDK is fully on-premise, processing all happens on hosting server and no data leaves server.
> - 10,000+ document templates covering IDs issued in 200+ countries and territories.
> - Support of 100+ languages and special characters via sophisticated neural networks.

## Table of Contents

- [Installation Guide](#installation-guide)
- [API Details](#api-details)
- [Gradio Demo](#gradio-demo)
- [Python Test API Example](#python-test-api-example)

## IDSDK Installation Guide

### Prerequisites

- Python 3.6+
- Linux
- CPU: 2cores or more
- RAM: 4GB or more

### Installation Steps

1. **Download the ID Document Recognition Linux Server Installer:**

   Download the Server installer for your operating system from the following link:
   
   [Download the On-premise Server Installer](https://drive.google.com/file/d/1NnZ-Ows3eI8O0TPTbJZcuIYUmVwXr-vV/view?usp=sharing)

2. **Install the On-premise Server:**

   Run the installer and follow the on-screen instructions to complete the installation. Go to the Download folder and run this command.
   ```sh
   $ cd Download
   $ sudo dpkg -i --force-overwrite MiniAiLive-IDSDK-LinuxServer.deb
   ```
<div align="center">
   <img src=https://github.com/MiniAiLive/ID-DocumentRecognition-Linux/assets/127708602/5547b656-e5ad-463b-a1b8-4107cdaed556 alt="MiniAiLive Installer">
</div>
   You can refer our Documentation here. https://docs.miniai.live

3. **Request License and Update:**

   You can generate the License Request file by using this command:
   ```sh
   $ cd /opt/miniai/dr-webapi
   $ sudo ./MiRequest request /home/ubuntu/Download/trial_key.miq
   ```
<div align="center">
   <img src=https://github.com/MiniAiLive/ID-DocumentRecognition-Linux/assets/127708602/7001cbe2-d246-40bf-acab-12786cc2d2e0 alt="MiniAiLive Installer">
</div>
   Then you can see the license request file on your directory, and send it to us via email or WhatsApp. We will send the license based on your Unique Request file, then you can upload the license file to allow to use. Refer the below images.
   
   ```sh
   $ sudo ./MiRequest update /home/ubuntu/Download/trial_30.mis
   ```
<div align="center">
   <img src=https://github.com/MiniAiLive/ID-DocumentRecognition-Linux/assets/127708602/e600fd00-895d-48d8-9228-396cd2fc6d98 alt="MiniAiLive Installer">
</div>

4. **Verify Installation:**

   After installation, verify that the On-premise Server is correctly installed by using this command:
   ```sh
   $ systemctl list-units --state running
   ```
   If you can see 'Mini-drsvc.service', 'Mini-idsvc.service', the server has been installed successfully. Refer the below image.
<div align="center">
   <img src=https://github.com/MiniAiLive/ID-DocumentRecognition-Linux/assets/127708602/18edc1d1-ddf4-48a7-86c8-eb48e01b4317 alt="MiniAiLive Installer">
</div>

## IDSDK API Details

### Endpoint

- `POST http://127.0.0.1:8082/api/check_id` ID Document Recognition API
- `POST http://127.0.0.1:8082/api/check_id_base64` ID Document Recognition API
  
- `POST http://127.0.0.1:8082/api/check_credit` Bank & Credit Card Reader API
- `POST http://127.0.0.1:8082/api/check_credit_base64` Bank & Credit Card Reader API
  
- `POST http://127.0.0.1:8082/api/check_mrz` MRZ & Barcode Recognition API
- `POST http://127.0.0.1:8082/api/check_mrz_base64` MRZ & Barcode Recognition API

### Request

- **URL:** `http://127.0.0.1:8082/api/check_id`
- **Method:** `POST`
- **Form Data:**
  - `image`: The image file (PNG, JPG, etc.) to be analyzed. This should be provided as a file upload.
<img width="1049" alt="Screenshot 2024-07-16 at 5 12 01 AM" src="https://github.com/user-attachments/assets/fa954d58-d623-4db3-8a65-1df2d5c28baf">

- **URL:** `http://127.0.0.1:8082/api/check_id_base64`
- **Method:** `POST`
- **Raw Data:**
  - `JSON Format`:
    {
       "image": "--base64 image data here--"
    }
<img width="1049" alt="Screenshot 2024-07-16 at 5 11 34 AM" src="https://github.com/user-attachments/assets/fa6f5e12-0abc-4e5f-a078-f541e3c546a7">

### Response

The API returns a JSON object with the recognized details from the ID document. Here is an example response:
   <div align="center">
      <img src="https://github.com/user-attachments/assets/fa954d58-d623-4db3-8a65-1df2d5c28baf" />
   </div>

## Gradio Demo

We have included a Gradio demo to showcase the capabilities of our ID Document Recognition SDK. Gradio is a Python library that allows you to quickly create user interfaces for machine learning models.

### How to Run the Gradio Demo

1. **Install Gradio:**

   First, you need to install Gradio. You can do this using pip:

   ```sh
   git clone https://github.com/MiniAiLive/ID-DocumentRecognition-Linux-SDK.git
   pip install -r requirement.txt
   cd gradio
   ```
2. **Run Gradio Demo:**
   ```sh
   python app.py
   ```
## Python Test API Example

To help you get started with using the API, here is a comprehensive example of how to interact with the ID Document Recognition API using Python. You can use API with another language you want to use like C++, C#, Ruby, Java, Javascript, and more

### Prerequisites

- Python 3.6+
- `requests` library (you can install it using `pip install requests`)

### Example Script

This example demonstrates how to send an image file to the API endpoint and process the response.

```python
import requests

# URL of the web API endpoint
url = 'http://127.0.0.1:8082/api/check_id'

# Path to the image file you want to send
image_path = './test_image.jpg'

# Read the image file and send it as form data
files = {'image': open(image_path, 'rb')}

try:
    # Send POST request
    response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request was successful!')
        # Parse the JSON response
        response_data = response.json()
        print('Response Data:', response_data)
    else:
        print('Request failed with status code:', response.status_code)
        print('Response content:', response.text)

except requests.exceptions.RequestException as e:
    print('An error occurred:', e)
```


## Request license
Feel free to [Contact US](https://www.miniai.live/contact/)  to get a trial License. We are 24/7 online on WhatsApp: [+19162702374](https://wa.me/+19162702374).

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
```java 
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.
```

## Face & IDSDK Online Demo, Resources
<div style="display: flex; justify-content: center; align-items: center;"> 
   <table style="text-align: center;">
      <tr>
         <td style="text-align: center; vertical-align: middle;"><a href="https://github.com/MiniAiLive"><img src="https://miniai.live/wp-content/uploads/2024/10/new_git-1-300x67.png" style="height: 60px; margin-right: 5px;" title="GITHUB"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://huggingface.co/MiniAiLive"><img src="https://miniai.live/wp-content/uploads/2024/10/new_hugging-1-300x67.png" style="height: 60px; margin-right: 5px;" title="HuggingFace"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://demo.miniai.live"><img src="https://miniai.live/wp-content/uploads/2024/10/new_gradio-300x67.png" style="height: 60px; margin-right: 5px;" title="Gradio"/></a></td> 
      </tr> 
      <tr>
         <td style="text-align: center; vertical-align: middle;"><a href="https://docs.miniai.live/"><img src="https://miniai.live/wp-content/uploads/2024/10/a-300x70.png" style="height: 60px; margin-right: 5px;" title="Documentation"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://www.youtube.com/@miniailive"><img src="https://miniai.live/wp-content/uploads/2024/10/Untitled-1-300x70.png" style="height: 60px; margin-right: 5px;" title="Youtube"/></a></td> 
         <td style="text-align: center; vertical-align: middle;"><a href="https://play.google.com/store/apps/dev?id=5831076207730531667"><img src="https://miniai.live/wp-content/uploads/2024/10/googleplay-300x62.png" style="height: 60px; margin-right: 5px;" title="Google Play"/></a></td>
      </tr>
   </table>
</div>

## Our Products
No | Project | Feature
---|---|---|
1 | [FaceRecognition-Android](https://github.com/MiniAiLive/FaceRecognition-Android) | 1:N Face Matching, 3D Face Passive LivenessDetection
2 | [FaceRecognition-LivenessDetection-Windows](https://github.com/MiniAiLive/FaceRecognition-LivenessDetection-Windows) | 1:N Face Matching, 3D Face Passive LivenessDetection
3 | [FaceLivenessDetection-Android](https://github.com/MiniAiLive/FaceLivenessDetection-Android) | 2D & 3D Face Passive LivenessDetection
4 | [FaceLivenessDetection-Linux](https://github.com/MiniAiLive/FaceLivenessDetection-Linux) | 2D & 3D Face Passive LivenessDetection
5 | [FaceLivenessDetection-Windows](https://github.com/MiniAiLive/FaceLivenessDetection-Windows) | 2D & 3D Face Passive LivenessDetection
6 | [FaceMatching-Android](https://github.com/MiniAiLive/FaceMatching-Android) | 1:1 Face Matching
7 | [FaceMatching-Windows](https://github.com/MiniAiLive/FaceMatching-Windows) | 1:1 Face Matching
8 | [FaceAttributes-Android](https://github.com/MiniAiLive/FaceAttributes-Android) | Face Attributes, Age & Gender Estimation
9 | [ID-DocumentRecognition-Android](https://github.com/MiniAiLive/ID-DocumentRecognition-Android) | IDCard, Passport, Driver License, Credit, MRZ Recognition
10 | [ID-DocumentRecognition-Linux](https://github.com/MiniAiLive/ID-DocumentRecognition-Linux) | IDCard, Passport, Driver License, Credit, MRZ Recognition
11 | [ID-DocumentRecognition-Windows](https://github.com/MiniAiLive/ID-DocumentRecognition-Windows) | IDCard, Passport, Driver License, Credit, MRZ Recognition
12 | [ID-DocumentLivenessDetection-Linux](https://github.com/MiniAiLive/ID-DocumentLivenessDetection-Linux) | ID Document LivenessDetection
13 | [ID-DocumentLivenessDetection-Windows](https://github.com/MiniAiLive/ID-DocumentLivenessDetection-Windows) | ID Document LivenessDetection

## About MiniAiLive
[MiniAiLive](https://www.miniai.live/) is a leading AI solutions company specializing in computer vision and machine learning technologies. We provide cutting-edge solutions for various industries, leveraging the power of AI to drive innovation and efficiency.

## Contact US
For any inquiries or questions, please [Contact US](https://www.miniai.live/contact/)

<p align="center">
<a target="_blank" href="https://t.me/Contact_MiniAiLive"><img src="https://img.shields.io/badge/telegram-@MiniAiLive-blue.svg?logo=telegram" alt="www.miniai.live"></a>&emsp;
<a target="_blank" href="https://wa.me/+19162702374"><img src="https://img.shields.io/badge/whatsapp-MiniAiLive-blue.svg?logo=whatsapp" alt="www.miniai.live"></a>&emsp;
<a target="_blank" href="https://join.skype.com/invite/ltQEVDmVddTe"><img src="https://img.shields.io/badge/skype-MiniAiLive-blue.svg?logo=skype" alt="www.miniai.live"></a>&emsp;
</p>
