# Kutty- an AI to manage Menu card in hotels

## Introduction
Kutty is an AI to manage Menu card in hotels. It is a chatbot which can be used to order food in hotels. It can also be used to get the details of the food items in the menu card. It also has a feature to get the details of customer's wish and check the availability of the food item in the hotel. It is a very user friendly chatbot which can be used by anyone.

## Requirements
* Python 3.9 or above
* pip3 (to install the required packages)
* html (to parse the html code)
* openai (to use the GPT-3 API)
* langchain (framework to create the chatbot)

## Working

### 1. QR Code Scanner

The QR Code Scanner is used to scan the QR Code of the hotel. The QR Code contains the details of the hotel. Menu card can also be accessed in the QR Code. The QR Code Scanner is created using the `pyzbar` module. The `pyzbar` module is used to decode the QR Code. The `cv2` module is used to capture the video from the web

### 2. Chatbot

GPT-3.5 Turbo with vector DB is used to create chat application

### 3. TTS and STT

The `gTTS` module is used to convert the text to speech. The `speech_recognition` module is used to convert the speech to text.
for speech to text we can use open source api like google, ibm, etc

### 4. GUI

html and css is used to create the GUI
