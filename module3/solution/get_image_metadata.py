import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

image_url = "https://upload.wikimedia.org/wikipedia/commons/1/15/Microsoft_Linux.jpg"

described_response = computervision_client.describe_image(image_url, max_candidates=1)

print(f"The description of the image is: {described_response.captions[0].text} with confidence {described_response.captions[0].confidence}")

tags = computervision_client.tag_image(url=image_url)

print(f"The tags are {[ tag.name for tag in tags.tags]} ")
