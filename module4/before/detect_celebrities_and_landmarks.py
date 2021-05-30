from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

django_image = "https://image.shutterstock.com/image-photo/samuel-l-jackson-kerry-washington-600w-124847914.jpg"

# Input code here

sydney_opera_house = "https://image.shutterstock.com/image-photo/sydney-august-22-sails-opera-600w-217455298.jpg"

# Input code here