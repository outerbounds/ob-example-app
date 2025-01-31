from outerbounds_app_client import OuterboundsAppClient
import requests
import sys

# Create a client instance with a name
client = OuterboundsAppClient()

# You can use any HTTP client to access the endpoint as usual.
# Just remember to add auth headers in the request, produced by
# get_auth_headers()
print(requests.get(sys.argv[1], headers=client.get_auth_headers()).json())
