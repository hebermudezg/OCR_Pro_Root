from pdf2image import convert_from_path
import pytesseract

def convert_pdf_to_text(pdf_path):
    images = convert_from_path(pdf_path)
    output_txt_path = pdf_path.replace(".pdf", "_output.txt")

    with open(output_txt_path, 'w') as txt_file:
        for image in images:
            text = pytesseract.image_to_string(image)
            txt_file.write(text)
            txt_file.write("\n\n")

    return output_txt_path
