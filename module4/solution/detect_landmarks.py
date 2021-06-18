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

django_response = computervision_client.analyze_image(django_image, details=["Celebrities"])

celebrities = []

for celebrity_category in django_response.categories:
    if celebrity_category.name == 'people_':
        for celebrity in celebrity_category.detail.celebrities:
            celebrities.append(celebrity.name)

print(f"Celebrities are {celebrities}")

sydney_opera_house = "https://image.shutterstock.com/image-photo/sydney-august-22-sails-opera-600w-217455298.jpg"

landmark_response = computervision_client.analyze_image(sydney_opera_house, details=["Landmarks"])

landmarks = []

for landmark_category in landmark_response.categories:
    if landmark_category.detail is not None:
        for landmark in landmark_category.detail.landmarks:
            landmarks.append(landmark.name)

print(f"Landmark are {landmarks}")
