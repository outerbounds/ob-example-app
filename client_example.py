from ob_app_client import OuterboundsAppClient
import requests
import sys

# Create a client instance with a name
client = OuterboundsAppClient()

print(requests.get(sys.argv[1], headers=client.get_auth_headers()).json())
