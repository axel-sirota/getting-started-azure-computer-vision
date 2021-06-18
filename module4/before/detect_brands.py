from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

logo = "https://image.shutterstock.com/image-photo/calodyne-mauritius-april-30-2016-600w-761081275.jpg"
