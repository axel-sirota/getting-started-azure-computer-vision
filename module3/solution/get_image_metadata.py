from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os

# Authenticate

subscription_key = os.environ["AZURE_COMPUTER_VISION_SUBSCRIPTION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

image_url = "https://i.blogs.es/09b293/satya-nadella-microsoft-linux-2-930x550/1366_2000.jpg"

described_response = computervision_client.describe_image(image_url, max_candidates=1)

print(f"The description of the image is: {described_response.captions[0].text} with confidence {described_response.captions[0].confidence}")

tags = computervision_client.tag_image(url=image_url)

print(f"The tags are {[ tag.name for tag in tags.tags]} ")
