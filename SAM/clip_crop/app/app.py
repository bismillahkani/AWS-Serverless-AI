import io
import requests
import json
from PIL import Image
from clipcrop import ClipCrop

def lambda_handler(event, context):

    print(event)

    try:
        input = json.loads(event['body'])
    except:
        input = event['body']
    
    print(input)

    img_url = input['img_url']
    search_query = input['search_query']

    img_bytes = requests.get(img_url).content
    img = Image.open(io.BytesIO(img_bytes))

    clip_crop = ClipCrop()

    scores, imgs, coords, index = clip_crop.predict(img,search_query)

    xy = coords[index][:4].astype(int).tolist()

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "bbox": xy,
            }
        )
    }
