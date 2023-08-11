import os
import requests
from django.core.files import File

OCR_API_TOKEN_HEADER = os.environ.get("OCR_API_TOKEN_HEADER")
OCR_API_ENDPOINT = os.environ.get('OCR_API_ENDPOINT')

def extract_text_via_ocr_service(file_obj:File=None):
    # get image
    # send image through HTTP POST 
    # return dict {}
    data = {}
    if OCR_API_TOKEN_HEADER is None:
        return data
    if OCR_API_ENDPOINT is None:
        return data
    if file_obj is None:
        return data
    headers = {
        'Authorization': f'Bearer {OCR_API_TOKEN_HEADER}'
    }
    with file_obj.open('rb') as f:
        r = requests.post(OCR_API_ENDPOINT,files={'file':f},headers=headers)
        print(r,100000000000000000000000000000000000)
        print(r.status_code,11111111111111111111111)
        if r.status_code in range(500,599):
            if r.headers.get('content-type') == 'application/json':
                print(r.headers,2222222222222222222)
                data = r.json()
    return data