import torch
from django.shortcuts import get_object_or_404, redirect, render


def machine(request, image):
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        imgs = image# batch of images
        results = model(imgs)
        results.print()
        results.save() # or .show()
        results.xyxy[0] # img1 predictions (tensor)
        results.pandas().xyxy[0] # img1 predictions (pandas)
        return render(request, 'home.html')