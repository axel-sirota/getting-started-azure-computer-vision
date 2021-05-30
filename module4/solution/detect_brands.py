from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

microsoft_shirt = "https://image.shutterstock.com/image-photo/redmond-washington-usa-march-28-600w-1357496909.jpg"

brand_response = computervision_client.analyze_image(microsoft_shirt, visual_features=['Brands'], max_candidates=1)

print(f"Brands are { [brand.name for brand in brand_response.brands] }")
