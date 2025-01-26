import os
import pdfplumber
import pandas as pd
import re

pdf_dir = 'Path_to_PDF_Folder'

# Initialize a list to store data
sections = [
    "General Information", "Risk Factors", "Introduction", "About Our Company", "Financial Information", 
    "Legal and Other Information", "Our Group Companies", "Other Regulatory and Statutory Disclosures", 
    "Offer Information", "Description of Equity Shares and Terms of Articles of Association", "Other Information"
]

# Initialize a list to store the extracted data
data = []

# Function to extract company name from the first few lines of the text
def extract_company_name(full_text):
    lines = full_text.split("\n")
    company_name = None
    # Assuming the company name appears in the first 10 lines
    for line in lines[:10]:
        if "limited" in line.lower() or "company" in line.lower():  # Adjust this as per the document format
            company_name = line.strip()
            break
    return company_name if company_name else "Unknown Company"

# Function to extract sections from a PDF
def extract_sections_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + '\n'
    
    # Extract company name
    company_name = extract_company_name(full_text)
    
    # Split text into sections based on keywords
    extracted_sections = {section: "" for section in sections}
    current_section = None
    for line in full_text.split("\n"):
        for section in sections:
            if section.lower() in line.lower():
                current_section = section
                break
        if current_section:
            extracted_sections[current_section] += line + '\n'
    
    extracted_sections['company_name'] = company_name  # Add company name to extracted sections
    return extracted_sections

# Loop through each PDF and extract text
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith('.pdf') or pdf_file.endswith('.PDF'):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        print(f"Processing {pdf_file}...")
        
        # Extract sections and company name from the PDF
        extracted_sections = extract_sections_from_pdf(pdf_path)
        
        # Add the extracted sections to the data list
        extracted_sections['file_name'] = pdf_file
        data.append(extracted_sections)

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# View the DataFrame
print(df.head())

df.to_csv('DRHP_Filings.csv', index=False)