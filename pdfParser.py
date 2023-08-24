import fitz  # PyMuPDF
import xml.etree.ElementTree as ET

def convert_pdf_to_xml(pdf_path, xml_path):
    # Load the PDF document
    pdf_document = fitz.open(pdf_path)
    
    # Create the root element of the XML document
    root = ET.Element('pdf_content')
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        page_element = ET.SubElement(root, 'page', number=str(page_num + 1))
        
        # Extract text from the PDF page
        page_text = page.get_text("text")
        text_element = ET.SubElement(page_element, 'text')
        text_element.text = page_text
    
    # Create an ElementTree from the root element
    tree = ET.ElementTree(root)
    
    # Write the XML to the specified file
    tree.write(xml_path, encoding='utf-8', xml_declaration=True)

    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    pdf_file_path = "input.pdf"  # Provide the path to your PDF file
    xml_file_path = "output.xml"  # Provide the desired path for the output XML file
    
    convert_pdf_to_xml(pdf_file_path, xml_file_path)
