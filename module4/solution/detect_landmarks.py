from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

eiffel_tower = "https://raw.githubusercontent.com/axel-sirota/getting-started-azure-computer-vision/main/Images/eiffel.jpg"

landmark_response = computervision_client.analyze_image(eiffel_tower, details=["Landmarks"])

landmarks = []

for landmark_category in landmark_response.categories:
    if landmark_category.detail is not None:
        for landmark in landmark_category.detail.landmarks:
            landmarks.append(landmark.name)

print(f"Landmarks are {landmarks}")
