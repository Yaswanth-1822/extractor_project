import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_aadhaar_fields(image):

    text = pytesseract.image_to_string(image)

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    aadhaar = None
    dob = None
    gender = None
    name = None

    # Aadhaar number
    aadhaar_match = re.search(r'\d{4}\s?\d{4}\s?\d{4}', text)
    if aadhaar_match:
        aadhaar = aadhaar_match.group()

    for i, line in enumerate(lines):

        # Detect DOB
        if "DOB" in line or re.search(r'\d{2}/\d{2}/\d{4}', line):

            dob_match = re.search(r'\d{2}/\d{2}/\d{4}', line)

            if dob_match:
                dob = dob_match.group()

            # name usually above DOB
            if i > 0:
                name = lines[i-1]

        # Detect gender
        if "MALE" in line.upper():
            gender = "MALE"

        if "FEMALE" in line.upper():
            gender = "FEMALE"

    return {
        "applicant_name": name,
        "aadhaar_number": aadhaar,
        "dob": dob,
        "gender": gender
    }