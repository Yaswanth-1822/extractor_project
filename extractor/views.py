from django.http import JsonResponse
#from PIL import Image
import pytesseract
#import re
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .ocr_preprocess import preprocess_image
from .aadhaar_extractor import extract_aadhaar_fields
def loan_form(request):
    return render(request, "form.html")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
@csrf_exempt
def extract_aadhaar(request):

    if request.method == "POST":

        file = request.FILES.get("document")

        processed_image = preprocess_image(file)

        data = extract_aadhaar_fields(processed_image)

        return JsonResponse(data)

    return JsonResponse({"error":"POST request required"})