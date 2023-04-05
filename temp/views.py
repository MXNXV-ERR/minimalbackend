from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from pymongo import MongoClient
from io import BytesIO
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
import base64




# @api_view(['GET'])
# def getData(request):
#     person = {'name':'maitri','age':21}
#     return Response(person)


@csrf_exempt
@api_view(['POST'])
def upload_image(request):
    base64_string = str(request.data['image'])
    if not base64_string:
        return JsonResponse({'error': 'Image not provided'}, status=400)

    image_bytes = base64.b64decode(base64_string.split(",")[1])


    image = Image.open(BytesIO(image_bytes))
    image.save("output.png")

    return JsonResponse({'data' : base64_string})
