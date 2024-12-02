from fpdf import FPDF
from fpdf.enums import Align

# create a class and inherit FPDF
class Shirtificate_Creator(FPDF):
    # Create a header
    def header(self):
        # Setting font:
        self.set_font("helvetica", size=48)
        # Get title width
        title_width = self.get_string_width(self.title)
        # Setting cursor position relative of center
        self.set_x((self.w - title_width) /2)
        # Print title in center horizontal position
        self.cell(title_width, 57, self.title, new_x="LMARGIN", new_y="NEXT", align="C")
        self.cell(0,1, new_x="LMARGIN", new_y="NEXT", align="C")
 
    # create a footer
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", size=15)
        self.cell(0, 10, align="C")

    # create page_body
    def page_body(self, name, shirt):
        # Setting imagen center horizontal
        self.image(shirt, x=Align.C, y=70, w=190)
        # Set font
        self.set_font("helvetica", size=24)
        # Set text color
        self.set_text_color(255,255,255)
        # Set cursor to y position
        self.set_y(128.5)
        # Get string with
        name_width = self.get_string_width(name)
        # Calculate the set_x position
        self.set_x((self.w - name_width) /2)
        # Print the text
        self.cell(name_width, 15, name, new_x="LMARGIN", new_y="NEXT",align="C")
        self.set_auto_page_break(auto=False)

    @staticmethod
    def get_name():
        user_name = input("Name: ")
        if not isinstance(user_name, str) or not all(part_of_string.isalpha() for part_of_string in user_name.split()):
            raise ValueError("Need a Valid Name")
        return f"{user_name.title().strip()} took CS50"


def main():
    shirtificate = Shirtificate_Creator()
    shirtificate.set_title("CS50 Shirtificate")
    shirtificate.add_page()
    # ~ shirtificate.print_shirt("Ricardo Garcia took CS50", "shirtificate.png")
    shirtificate.page_body(shirtificate.get_name(), "shirtificate.png")
    shirtificate.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
