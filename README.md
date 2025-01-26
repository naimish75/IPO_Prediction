# DRHP Reports Analysis

A Python-based project that automates the extraction and analysis of Draft Red Herring Prospectus (DRHP) reports. This tool parses PDF documents, extracts predefined sections, and organizes the data into a structured format. It is designed for professionals working with public offerings and regulatory filings to streamline workflows and enhance productivity.

---

## Table of Contents
- [Features](#features)
- [Project Workflow](#project-workflow)
- [Technologies Used](#technologies-used)
- [Setup and Usage](#setup-and-usage)
- [Output Example](#output-example)
- [Data Source](#data-source)
- [Connect](#connect)

---

## Features

- **Automated PDF Parsing**: Extracts text from DRHP PDFs using `pdfplumber`.
- **Section Segmentation**: Identifies and extracts key sections:
  - General Information
  - Risk Factors
  - Financial Information
  - About Our Company
  - Legal and Other Information
- **Company Name Detection**: Automatically extracts the company name from the introductory text of the DRHP.
- **Data Structuring**: Converts extracted text into a structured Pandas DataFrame.
- **CSV Export**: Saves results into a CSV file for easy analysis.

---

## Project Workflow

1. **PDF Processing**: Scans a directory for DRHP PDFs and processes them one by one.
2. **Text Extraction**: Reads and extracts content from the PDFs using `pdfplumber`.
3. **Section Parsing**: Splits content into predefined sections using regular expressions.
4. **Data Aggregation**: Organizes the extracted sections into a Pandas DataFrame.
5. **Export**: Saves the structured data as a CSV file.

---

## Technologies Used

- **Python**: The core language for this project.
- **pdfplumber**: A library for extracting text and metadata from PDFs.
- **Pandas**: For data manipulation and CSV export.
- **Regular Expressions (re)**: For matching and extracting specific content.

---

## Setup and Usage

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- Required Python packages: `pdfplumber`, `pandas`

