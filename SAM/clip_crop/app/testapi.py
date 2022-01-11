import io
import requests
import json
from PIL import Image

api_url = "API_URL"

payload = {"img_url":"https://github.com/pjreddie/darknet/blob/master/data/person.jpg?raw=true",
            "search_query":"blue jacket"}

response = requests.post(api_url, data = json.dumps(payload))

bbox = response.json()['bbox']

img_bytes = requests.get(payload['img_url']).content
img = Image.open(io.BytesIO(img_bytes))

img.show()
crop = img.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
crop.show()
