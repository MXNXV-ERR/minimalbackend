from rest_framework.response import Response
from rest_framework.decorators import api_view
from .code import pickleissour,tensorcaller,imglogo
import os
import shutil
from django.http import JsonResponse
from io import BytesIO
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
import base64
from ultralytics import YOLO
model = YOLO('api/code/bestv8.pt')

@api_view(['POST'])
def getPredPickelReview(request):
    review = request.data
    pred=pickleissour.getJoblibModelPred(review)
    ret={"pred":pred}
    return Response(ret)


@api_view(['POST'])
def getPredTensorReview(request):
    review = request.data['input_text']
    pred=tensorcaller.getTensorModelPred(review)
    ret={"pred":pred}
    return Response(ret)


@api_view(['POST'])
def getImagePred(request):
    img_data=request.data['img']
    ret = imglogo.getImgPred(img_data)
    return Response(ret)


@csrf_exempt
@api_view(['POST'])
def getImagePred(request):
    base64_string = str(request.data['image'])
    if not base64_string:
        return JsonResponse({'error': 'Image not provided'}, status=400)
    try:
        image_bytes = base64.b64decode(base64_string.split(",")[1])
    except:
        return Response({"name":"Not good file/Not uploaded anything","conf":0.0})

    image = Image.open(BytesIO(image_bytes))
    image.save("output.png")
    res=model.predict(source='output.png',save=True,save_txt=True,save_conf=True)
    try:
        with open("runs/detect/predict/labels/output.txt") as f:
            t=f.readline().split()
            clas = t[0]
            conf = t[5]
            print(clas,conf)
        names=['Adidas', 'Apple', 'BMW', 'Citroen', 'Cocacola', 'DHL', 'Fedex', 'Ferrari', 'Ford', 'Google', 'Heineken', 'HP', 'Intel', 'McDonalds', 'Mini', 'Nbc', 'Nike', 'Pepsi', 'Porsche', 'Puma', 'RedBull', 'Sprite', 'Starbucks', 'Texaco', 'Unicef', 'Vodafone', 'Yahoo']
        restul = {"name" :names[int(clas)],"conf":conf}
        print(type(res))
        shutil.rmtree("runs/detect/predict")
    except:
        shutil.rmtree("runs/detect/predict")
        return Response({"name":"No logo detected","conf":0.0})
    return Response(restul)

    # # return Response({'data' : base64_string})
    # ret =imglogo.getImgPred()
    # return Response(ret)
