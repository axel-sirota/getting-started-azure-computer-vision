import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

logo = "https://raw.githubusercontent.com/axel-sirota/getting-started-azure-computer-vision/main/Images/my_car.jpg"

brand_response = computervision_client.analyze_image(logo, visual_features=['Brands'], max_candidates=1)

print(f"Brands are { [brand.name for brand in brand_response.brands] }")
