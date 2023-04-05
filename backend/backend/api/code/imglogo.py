# import cv2
# import base64
# # from ultralytics import YOLO
# import torch
# from yolov7.models.experimental import attempt_load

# from utils.general import non_max_suppression

# def getImgPred(ing_data):
#     model = attempt_load('api/code/best.pt')
#     img_file = 'temp.jpg'
#     with open(img_file,'wb') as f:
#         f.write(base64.b64decode(img_data))
#     img = cv2.imread('temp.jpg')
#     result=model.predict(source=img,save=True)
#     print(result)

from ultralytics import YOLO
import cv2
import base64
from django.http import JsonResponse
from io import BytesIO
from PIL import Image


model = YOLO('api/code/bestv8.pt')
#model.predict(source='0')
def getImgPred():

    #print(img_data)
    # base64_string = str(img_data)
    # if not base64_string:
    #     return JsonResponse({'error': 'Image not provided'}, status=400)

    # image_bytes = base64.b64decode(base64_string.split(",")[1])
    # #image_bytes = base64.b64decode(img_data)
    # print(image_bytes)
    
    # image = Image.open(BytesIO(image_bytes))
    # image.save("api/code/imgs/output.png")
    img_file = 'api/code/imgs/output.png'
    with open(img_file,'wb') as f:
        f.write(base64.b64decode(img_file))
    img = cv2.imread('api/code/imgs/output.png')
    result=model.predict(source=img,save=True)
    print(result[0])