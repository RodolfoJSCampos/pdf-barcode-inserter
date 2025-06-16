# 📄 PDF Barcode Inserter

This project processes incoming PDF files (sales orders), extracts the order number, generates a Code128 barcode, stamps it into the PDF, and automatically sends the modified PDF to a network printer.

---

## ✅ Project Background and Motivation

After identifying a need within the company to speed up the process of sending sales orders to customers, I developed this system to accelerate the internal registration of sales invoices. The solution works by inserting a **barcode into the sales order PDFs**, allowing operators to **scan the order code using a barcode reader instead of typing it manually**.

This change significantly **reduced processing time** and **minimized human error** during data entry.

The choice for a **local processing solution** was primarily driven by **time constraints** and **cost considerations**, as implementing this feature through the external ERP vendor would have been expensive and time-consuming.

Another key factor was to ensure **minimal disruption to employee workflows**:  
Now, staff members only need to **select the virtual printer** (which runs this script automatically) when printing the sales orders — or leave it as the default printer.

As a result, the company achieved the goal with **zero additional cost** and **without requiring major operational changes**.

---

## ✅ Features:
- PDF text extraction
- Automatic barcode generation (Code128)
- PDF overlay with barcode
- Silent network printing

---

## ✅ Technologies:
- Python
- PyPDF2
- ReportLab
- pdfplumber
- pywin32

---

## ✅ Results:
### 📥 Original Input PDF (Before Processing):
![entrada](https://github.com/user-attachments/assets/1191ebd9-a4de-4281-acb8-c28a4bd30b25)


### 📤 Output PDF with Barcode (After Processing):
![saida](https://github.com/user-attachments/assets/64f5f977-63ec-4b1e-9c5d-f8c35aee6625)

_Disclaimer:
These sample images were intentionally modified to hide sensitive data.
They are meant only to illustrate the visual effect of the barcode insertion process._
