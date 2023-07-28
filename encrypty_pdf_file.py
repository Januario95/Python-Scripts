# pip install pypdf2

import PyPDF2



# Encrypt

# pdf = open('hbr-org-2020-07-sarcasm-self-deprecation-and-inside-jokes-a-users-guide-to-humor.pdf', 'rb')

# input_pdf = PyPDF2.PdfFileReader(pdf)
# pages_no = input_pdf.numPages
# output_pdf = PyPDF2.PdfFileWriter()


# for i in range(pages_no):
#     input_pdf = PyPDF2.PdfFileReader(pdf)
#     output_pdf.addPage(input_pdf.getPage(i))
#     output_pdf.encrypt('Jaci1995')
    
#     with open('hbr-org-2020-07-sarcasm-self-deprecation-and-inside-jokes-a-users-guide-to-humor-PROTECTED.pdf', 'wb') as f:
#         output_pdf.write(f)
        
# pdf.close()



# Decrypt

# with open('hbr-org-2020-07-sarcasm-self-deprecation-and-inside-jokes-a-users-guide-to-humor-PROTECTED.pdf', 'rb') as f:
#     input_pdf = PyPDF2.PdfFileReader(f)
    
# output_file = PyPDF2.PdfFileWriter()
# output_file.appendPagesFromReader(input_pdf)
# output_file.decrypt('Jaci1995')

# with open('hbr-org-2020-07-sarcasm-self-deprecation-and-inside-jokes-a-users-guide-to-humor-DECRYPTED.pdf', 'wb') as f:
#     output_file.write(f)





from PyPDF2 import PdfFileWriter, PdfFileReader

with open("hbr-org-2020-07-sarcasm-self-deprecation-and-inside-jokes-a-users-guide-to-humor-PROTECTED.pdf", "rb") as in_file:
    input_pdf = PdfFileReader(in_file)

output_pdf = PdfFileWriter()
output_pdf.appendPagesFromReader(input_pdf)
output_pdf.decrypt("password")

with open("hbr-org-2020-07-sarcasm-self-deprecation-and-inside-jokes-a-users-guide-to-humor-DECRYPTED.pdf", "wb") as out_file:
        output_pdf.write(out_file)























