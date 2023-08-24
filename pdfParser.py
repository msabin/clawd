import fitz  # PyMuPDF
import xml.etree.ElementTree as ET

class QA:
    def __init__(self, question):
        self.question = question
        self.answer = ""




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
    
    # convert_pdf_to_xml(pdf_file_path, xml_file_path)



def match_question_marks():
    doc = fitz.open("input.pdf") # open a document
    out = open("output.txt", "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text() # get plain text (is in UTF-8)

        responses = []
        sentence = ""
        paragraph = ""
        question = ""
        waitingResponse = False
        firstResponse = ""
        for letter in text:
            sentence += letter

            if letter == ".":
                if waitingResponse:
                    qa.answer += sentence

                sentence = ""

            
            
            if letter == "?":
                if not waitingResponse:
                    qa = QA(sentence)
                    waitingResponse = True
                    sentence = ""
                else: break

                qa.answer = paragraph

                question = sentence
                waitingResponse = True

                sentence = ""
                paragraph = ""
                if firstResponse == "":
                    firstResponse = sentence
                responses.append(sentence)
            


    print(qa.question)
    print(qa.answer)  
    # out.write(text) # write text of page
    # out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    out.close()

match_question_marks()



