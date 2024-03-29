import os

api_key= os.environ.get("API_KEY")

if api_key:
    print(f"API Key: {api_key}")
else:
    print("API KEY IS NOT set.")
