import os
import fitz
pth = r'Path\FolderContainingPDFs'
savepath = r"C:\Path\FolderToStoreMarkdownFiles"

# list to store files
res = []
# Iterate directory
for file in os.listdir(pth):
    # check only text files
    if file.endswith('.pdf'):
        res.append(file)



for docname in res:
    #print(docname)
    toOpen = pth + "\\" + docname
    flagg = os.path.getsize(toOpen) # I was getting an error for some pdfs
    if flagg>0: 
        doc = fitz.open(pth + "\\" + docname)
        page = doc.load_page
        htext = []
        for page in doc:
            for annot in page.annots():
                text = page.get_textbox(annot.rect)
                htext.append(text)
                htext.append("\n \n")

        if htext:
            newname = savepath + "\\" + docname[:-4] + ".md"   
            with open(newname, 'w', encoding = "utf-8") as f:
                for t in htext:
                    f.write(t)        