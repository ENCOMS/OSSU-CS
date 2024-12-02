from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #Rendering logo:
        self.image("fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style='B', size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align='C')
        # Performing a line break (ln is deprecated, use new_x, new_y):
        self.ln(20)
        # ~ self.cell(0,20, new_x='LMARGIN', new_y='NEXT')

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style='I', size=8)
        # Printing page number:
        self.cell( 0, 10 , f"Page {self.page_no()}/{{nb}}", border=1, align='C')

def main():
    # Instantiation of inherited class
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    for i in range(1, 41):
        pdf.cell(0, 10, f"Printing line number {i}", new_x='LMARGIN', new_y='NEXT')
    pdf.output("new-tuto2.pdf")


if __name__ == "__main__":
    main()
