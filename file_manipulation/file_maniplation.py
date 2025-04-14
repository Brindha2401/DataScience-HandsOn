import csv
import pandas as pd
from PyPDF2 import PdfReader
from openpyxl import Workbook

# ---------- TEXT FILE OPERATIONS ----------
def text_file_operations():
    print("Text File Operations:")
    with open("file_manipulation_folder/sampleTextFile.txt", "w") as file:
        file.write("Hello, this is a text file.\nLet's manipulate files!")

    with open("file_manipulation_folder/sampleTextFile.txt", "r") as file:
        #content = file.read()
        print("Text file content:\n", file.read())

# ---------- CSV FILE OPERATIONS ----------
def csv_operations():
    print("\nCSV Operations (using csv module and pandas):")
    # Write CSV
    data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
    with open("file_manipulation_folder/sampleCsvFile.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # Read CSV using csv module
    with open("file_manipulation_folder/sampleCsvFile.csv", "r") as file:
        reader = csv.reader(file)
        print("CSV content (csv module):")
        for row in reader:
            print(row)

    # Read CSV using pandas
    df = pd.read_csv("file_manipulation_folder/sampleCsvFile.csv")
    print("\nCSV content (pandas):")
    print(df)

    # Add a new column
    df["Country"] = ["USA", "Canada"]
    df.to_csv("file_manipulation_folder/sample_updated_csvFile.csv", index=False)

# # ---------- EXCEL FILE OPERATIONS ----------
def excel_operations():
    print("\nExcel File Operations:")
    # Create a sample Excel file
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    ws.append(["Item", "Price"])
    ws.append(["Apple", 1.2])
    ws.append(["Banana", 0.5])
    wb.save("file_manipulation_folder/sampleExcelFile.xlsx")

    # Read Excel file using pandas
    df = pd.read_excel("file_manipulation_folder/sampleExcelFile.xlsx")
    print("Excel content (pandas):")
    print(df)

# ---------- PDF FILE OPERATIONS ----------
def pdf_operations():
    print("\nPDF File Operations:")
    try:
        # Create a simple PDF using fpdf (optional)
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="This is a PDF file created with Python.", ln=True)
        pdf.output("file_manipulation_folder/samplePdfFile.pdf")

        # Read from the created PDF
        reader = PdfReader("file_manipulation_folder/samplePdfFile.pdf")
        print("Number of pages in PDF:", len(reader.pages))
        print("Text from first page:")
        print(reader.pages[0].extract_text())
    except Exception as e:
        print("PDF operation failed:", e)

# ---------- MAIN ----------
if __name__ == "__main__":
    text_file_operations()
    csv_operations()
    excel_operations()
    pdf_operations()
