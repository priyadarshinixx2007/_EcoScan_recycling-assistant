# EcoScan - Smart Product Recycling Assistant

## About the Project

EcoScan is a simple OCR-based application that helps users identify recycling and disposal information from product packaging. The user can upload an image of a product or package, and the application reads the text printed on it using Optical Character Recognition (OCR).

The extracted information is then analyzed to identify details related to packaging materials and recycling instructions. The application provides the available recycling information in a simple and easy-to-understand format.

The main purpose of EcoScan is to make it easier for users to understand how a product package can be recycled or disposed of based on the information available on its label.

## Objectives

* Extract text from product packaging images using OCR.
* Identify useful packaging and recycling-related information.
* Provide simple recycling or disposal guidance.
* Reduce confusion about recycling instructions on product packages.
* Create an easy-to-use application for everyday use.

## Technologies Used

* Python
* Streamlit
* Tesseract OCR
* Pytesseract
* Pillow
* GitHub

## How It Works

1. The user uploads an image of a product or package.
2. EcoScan processes the uploaded image.
3. Tesseract OCR extracts the text from the image.
4. The extracted text is analyzed for product and packaging information.
5. The application identifies available recycling-related information.
6. The result is displayed to the user along with recycling or disposal guidance.

## OCR Technology

EcoScan uses Tesseract OCR to recognize text from product packaging images. Pytesseract is used to connect the Python application with the Tesseract OCR engine.

The accuracy of the extracted information depends on the quality, clarity, orientation, and visibility of the text in the uploaded image.

## Recycling Information

The application looks for information such as:

* Plastic
* PET
* HDPE
* Paper
* Carton
* Glass
* Recycling instructions
* Disposal instructions

If sufficient information is not detected, the application informs the user that the recycling information could not be confidently identified and recommends checking the product packaging and local recycling guidelines.

## Application

EcoScan is developed using Streamlit, which provides the web interface for uploading product images and displaying the extracted information and recycling results.

## Future Improvements

* Support for camera input.
* Better product and brand identification.
* Improved extraction of ingredients and expiry information.
* Recognition of recycling symbols.
* Barcode-based product identification.
* Support for multiple languages.
* Improved recycling recommendations based on local guidelines.

## Project Structure

```text
EcoScan/
|
|-- app.py
|-- requirements.txt
|-- README.md
```

## Installation and Setup

Clone the repository and install the required Python packages.

```bash
git clone <repository-url>
cd EcoScan
pip install -r requirements.txt
```

Run the application using:

```bash
streamlit run app.py
```

The application will open in the browser and can be used to upload a product image for scanning.

## Conclusion

EcoScan demonstrates how OCR and a simple web interface can be combined to extract useful information from product packaging and assist users with recycling and disposal decisions. The project can be further improved with better image processing, product databases, barcode recognition, and more detailed recycling recommendations.
