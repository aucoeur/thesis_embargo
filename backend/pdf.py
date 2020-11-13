# NOTE: THIS IS NOT WORKING CODE
# TESTING CODE FOR CREATING A PDF
# PURPOSE IS TO SEE WHAT CAN BE USED

# from https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# create a cell
# pdf.cell(200, 10, txt = "This is a Test for Team Porculion",
#          ln = 1, align = 'C')

#going to create a var that uses a text file for pdf
file = open("Template_testing.txt","r")
#iterate over text file to insert into pdf
for i in file:
    pdf.cell(200, 10, txt = i,
         ln = 1, align = 'C')
# add another cell
# pdf.cell(200, 10, txt = "This code works and can be used.",
#          ln = 2, align = 'C')

# save the pdf with name .pdf
pdf.output("GFG.pdf")
