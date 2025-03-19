from datetime import datetime
import cv2
import numpy as np
from deepface import DeepFace
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from .models import Photo
from .serializers import PhotoSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_photos(request):
    files = request.FILES.getlist('images')

    #identifiant pour l'événement
    event_id = request.data.get('event_id', datetime.now().strftime("event_%Y%m%d_%H%M%S"))

    photos = []

    for file in files:
        #l'image avec son event_id
        photo = Photo.objects.create(image=file, event_id=event_id)
        file_path = photo.image.path


        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        # netteté de l'image
        nettete = cv2.Laplacian(image, cv2.CV_64F).var()

        # detection des visages
        detecteur = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # un model deja existant
        visages = detecteur.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        nombre_visages = len(visages)

        # la luminosité
        luminosite = np.mean(image)

        # émotions
        try:
            analyse = DeepFace.analyze(file_path, actions=['emotion'], enforce_detection=False)
            emotion = analyse[0]['dominant_emotion']
        except:
            emotion = "inconnu"

        # score Global
        score = (nettete * 0.5) + (nombre_visages * 10) + (luminosite * 0.2)

        # Sauvegarde
        photo.score = score
        photo.save()
        photos.append(photo)

    return Response({
        "message": "Images analysées",
        "event_id": event_id,
        "total_images": len(photos)
    })

@api_view(['GET'])
def best_photos(request, event_id):
    top_photos = Photo.objects.filter(event_id=event_id).order_by('-score')[:3]
    serializer = PhotoSerializer(top_photos, many=True)
    return Response(serializer.data)
