import re
import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Read text from PDF
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def parse_resume(pdf_path):
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    lines = text.split("\n")
    
    # Assume first line is the name
    name = None
    for line in lines:
        if line.strip():
            name = line.strip()
            break
    
    # Patterns for email and phone number
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_pattern = r'\b(?:\+?\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b'
    
    # Find email and phone number
    email = re.findall(email_pattern, text)
    phone_number = re.findall(phone_pattern, text)
    
    # Skills section (example keywords)
    skills_keywords = ["Python", "Java", "SQL", "Machine Learning", "Data Analysis"]
    skills = [word for word in skills_keywords if word in text]
    
    # Prepare extracted information
    return {
        "Name": name,
        "Email": email[0] if email else None,
        "Phone Number": phone_number[0] if phone_number else None,
        "Skills": skills
    }
