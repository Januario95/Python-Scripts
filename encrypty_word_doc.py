# pip install aspose-words 


import aspose.words as aw

# load document
doc = aw.Document("document1.docx")

# create document options
options = aw.saving.OoxmlSaveOptions(aw.SaveFormat.DOCX)

# set password
options.password = "password"

# save updated document
doc.save("document.docx", options)

