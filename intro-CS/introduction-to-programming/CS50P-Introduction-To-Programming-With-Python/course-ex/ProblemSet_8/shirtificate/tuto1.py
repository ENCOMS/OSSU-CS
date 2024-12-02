from fpdf import FPDF

pdf = FPDF()
print(type(pdf))
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Hello World!", 1)
pdf.cell(40, 10, 'Hello World!', 1, align='C')
pdf.cell(40, 10, 'Hello World!', 1, new_x="LMARGIN", new_y="NEXT", 
align='R')
pdf.cell(60, 10, 'Powered by FPDF.', 1, new_x="LMARGIN", new_y="NEXT", 
align='C')
pdf.cell(40, 10, "Hello World!", 1)
pdf.output("tuto1.pdf")
