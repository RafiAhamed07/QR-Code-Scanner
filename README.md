# QR Code Scanner

This application captures video from a camera, detects and decodes QR codes, and performs Optical Character Recognition (OCR) on the frames.

## Features
- Real-time QR code detection and decoding.
- Optical Character Recognition (OCR) on the video frames.
- Automatically opens detected QR code URLs in a web browser.

## Requirements
- Python 3.7 or higher
- OpenCV 4.5.5
- pytesseract 0.3.9
- pyzbar 0.1.8
- tkinter (included with standard Python installations)

## Installation

### Prerequisites
Ensure you have [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) installed on your system. For Windows, download the installer from [here](https://github.com/tesseract-ocr/tesseract/wiki/Downloads).

### Python Packages
You can install the required Python packages using pip:

```sh
pip install opencv-python-headless==4.5.5.64 pytesseract==0.3.9 pyzbar==0.1.8
```

## Usage
Clone the repository or download the script.

Run the script:
```sh
python qr_ocr_scanner.py
```

## Instructions:

  - A message box will appear with instructions to press 'q' to quit the application.
  - The application will start capturing video from the camera.
  - It will display the video with OCR bounding boxes and detected QR codes.
  - If a QR code is detected, its URL will automatically open in the default web browser.
  - Press 'q' to exit the application.

## Create your own QR Code
CLick here : [QR_Code_Generator](https://github.com/RafiAhamed07/QR_Code_Generator)
