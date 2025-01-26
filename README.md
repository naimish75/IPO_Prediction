DRHP Reports Analysis
A Python-based project that automates the extraction and analysis of Draft Red Herring Prospectus (DRHP) reports. This tool parses PDF documents, extracts predefined sections, and organizes the data into a structured format. It is designed for professionals working with public offerings and regulatory filings to streamline workflows and enhance productivity.

Table of Contents
Features
Project Workflow
Technologies Used
Setup and Usage
Output Example
Data Source
Connect
Features
Automated PDF Parsing: Extracts text from DRHP PDFs using pdfplumber.
Section Segmentation: Identifies and extracts key sections:
General Information
Risk Factors
Financial Information
About Our Company
Legal and Other Information
Company Name Detection: Automatically extracts the company name from the introductory text of the DRHP.
Data Structuring: Converts extracted text into a structured Pandas DataFrame.
CSV Export: Saves results into a CSV file for easy analysis.
Project Workflow
PDF Processing: Scans a directory for DRHP PDFs and processes them one by one.
Text Extraction: Reads and extracts content from the PDFs using pdfplumber.
Section Parsing: Splits content into predefined sections using regular expressions.
Data Aggregation: Organizes the extracted sections into a Pandas DataFrame.
Export: Saves the structured data as a CSV file.
Technologies Used
Python: The core language for this project.
pdfplumber: A library for extracting text and metadata from PDFs.
Pandas: For data manipulation and CSV export.
Regular Expressions (re): For matching and extracting specific content.
Setup and Usage
Prerequisites
Ensure you have the following installed:

Python 3.8 or higher
Required Python packages: pdfplumber, pandas
Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/naimish75/drhp-reports-analysis.git
cd drhp-reports-analysis
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Download DRHP PDFs
Download DRHP reports from the official SEBI DRHP Reports Listing.

Place Files in Directory
Save the PDFs into a folder. By default, the script looks in:

javascript
Copy
Edit
C:/Rutgers/Textual Analysis/Final Proj/DRHP_PDFs
Run the Script
Execute the script to process the PDFs:

bash
Copy
Edit
python DRHP_Reports.py
View Output
After processing, the script generates a CSV file named DRHP_Filings.csv in the current working directory. This file contains the extracted and structured data.

Output Example
The generated CSV file contains data in the following format:

File Name	Company Name	Risk Factors	Financial Information	...
Example1.pdf	ABC Ltd.	Details on risks...	Metrics and trends...	...
Example2.pdf	XYZ Corp.	Comprehensive risks	Revenue breakdown...	...
Data Source
The DRHP PDFs can be downloaded from the SEBI DRHP Reports Listing at the following URL:
https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&ssid=15&smid=10

Download the PDFs and place them into the specified directory before running the script.

