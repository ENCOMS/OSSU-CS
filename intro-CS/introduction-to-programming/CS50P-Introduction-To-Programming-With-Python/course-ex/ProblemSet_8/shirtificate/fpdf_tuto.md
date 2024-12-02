# fpdf library

[fpdf tutorial](https://py-pdf.github.io/fpdf2/Tutorial.html)

**Tip:**
In a Cartesian coordinate system a point x, y (3, 5)
+ The abscissa is 3 (the horizontal or x-coordinate).
+ The ordinate is 5 (the vertical or y-coordinate).

## Example 1 - Simple page:

```python
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

```

Notes:
## import the library

`from fpdf import FPDF`

## Create an instance of FPDF
[FPDF reference](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF)

`pdf = FPDF()`,

FPDF is the PDF Generation class

Where the FPDF constructor work by defaul like:

`pdf = FPDF(orientation="P", unit="mm", format="A4")`

Per Documentation:

```
 class FPDF (orientation='portrait', unit='mm', format='A4', 
 font_cache_dir='DEPRECATED') 
```

**FPDF arguments:**

**orientation** : str
    possible values are "portrait" (can be abbreviated "P") or 
    "landscape" (can be abbreviated "L"). Default to "portrait".

**unit** : str, int, float
    possible values are "pt", "mm", "cm", "in", or a number. A point 
    equals 1/72 of an inch, that is to say about 0.35 mm (an inch being 
    2.54 cm). This is a very common unit in typography; font sizes are 
    expressed in this unit. If given a number, then it will be treated 
    as the number of points per unit. (eg. 72 = 1 in) Default to "mm".

**format** : str
    possible values are "a3", "a4", "a5", "letter", "legal" or a tuple 
    (width, height) expressed in the given unit. Default to "a4".

**font_cache_dir** : Path or str
    [DEPRECATED since v2.5.1] unused 

 + Where we can change orientation to landscape `"L"`
 + Units `pt`, `cm`, `in`
 + Page formats `Letter` or `Legal`

## add_page

`pdf.add_page`, optional set the margins with `set_margins`

Adds a new page to the document. If a page is already present, the 
FPDF.footer() method is called first. Then the page is added, the 
current position is set to the top-left corner, with respect to the 
left and top margins, and the FPDF.header() method is called.

Per documentation:

`def add_page(self, orientation='', format='', same=False, duration=0, transition=None)`

add_page arguments:

**orientation** : str
    "portrait" (can be abbreviated "P") or "landscape" (can be 
    abbreviated "L"). Default to "portrait".

**format** : str
    "a3", "a4", "a5", "letter", "legal" or a tuple (width, height). 
    Default to "a4".

**same** : bool
    indicates to use the same page format as the previous page. Default 
    to False.

**duration** : float
    optional page’s display duration, i.e. the maximum length of time, 
    in seconds, that the page is displayed in presentation mode, before 
    the viewer application automatically advances to the next page. Can 
    be configured globally through the .page_duration FPDF property. As 
    of june 2021, onored by Adobe Acrobat reader, but ignored by 
    Sumatra PDF reader.

**transition** : Transition child class
    optional visual transition to use when moving from another page to 
    the given page during a presentation. Can be configured globally 
    through the .page_transition FPDF property. As of june 2021, onored 
    by Adobe Acrobat reader, but ignored by Sumatra PDF reader.

## set_margin

Sets the document right, left, top & bottom margins to the same value.

Per documentation:

`def set_margin(self, margin)`

set_margin arguments:

margin : float
    margin in the unit specified to FPDF constructor

## set_margins

Sets the document left, top & optionaly right margins to the same 
value. By default, they equal 1 cm. Also sets the current FPDF.y on the 
page to this minimum vertical position.

Per documentation:

`def set_margins(self, left, top, right=-1)`

set_margins arguments:

**left** : float
    left margin in the unit specified to FPDF constructor
**top** : float
    top margin in the unit specified to FPDF constructor
**right** : float
    optional right margin in the unit specified to FPDF constructor 

## set_font

`pdf.set_font('Helvetica', style='B', size=16)`

or therwise the document would be invalid.

Sets the font used to print character strings. It is mandatory to call 
this method at least once before printing text.

Default encoding is not specified, but all text writing methods accept 
only unicode for external fonts and one byte encoding for standard.

Standard fonts use Latin-1 encoding by default, but Windows encoding 
cp1252 (Western Europe) can be used with self.core_fonts_encoding = 
encoding.

The font specified is retained from page to page. The method can be 
called before the first page is created.


Per documentation:

`def set_font(self, family=None, style='', size=0)`

set_font arguments:

**family** : str
    name of a font added with FPDF.add_font(), or name of one of the 14 
    standard "PostScript" fonts: Courier (fixed-width), Helvetica (sans 
    serif), Times (serif), Symbol (symbolic) or ZapfDingbats (symbolic) 
    If an empty string is provided, the current family is retained.

**style** : str
    empty string (by default) or a combination of one or several 
    letters among B (bold), I (italic) and U (underline). Bold and 
    italic styles do not apply to Symbol and ZapfDingbats fonts.

**size** : float
    in points. The default value is the current size.

 + We can change the font to `Helvetica` or the other build-in fonts
 `Times`, `Courier`, `Symbol`, `ZapfDingbats`
 + Style can be change to `style='B'` where bold `'B'`, italic `'I'` or underlined `'U'` or a regular
 font with an empty string.
 + We can change font size with `size=16` where number is in points, not millimeters.

## Cell

Prints a cell (rectangular area) with optional borders, background 
color and character string. The upper-left corner of the cell 
corresponds to the current position. The text can be aligned or 
centered. After the call, the current position moves to the selected 
new_x/new_y position. It is possible to put a link on the text. A cell 
has an horizontal padding, on the left & right sides, defined by 
the.c_margin property.

If automatic page breaking is enabled and the cell goes beyond the 
limit, a page break is performed before outputting.

Per documentation:
```
def cell(self, w=None, h=None, text='', border=0, ln='DEPRECATED', 
    align=Align.L, fill=False, link='', center=False, markdown=False, 
    new_x=XPos.RIGHT, new_y=YPos.TOP)
```

**Cell arguments:**

**w** : float
    Cell width. Default value: None, meaning to fit text width. If 0, 
    the cell extends up to the right margin. (take all the row)

**h** : float
    Cell height. Default value: None, meaning an height equal to the 
    current font size.

**text** : str
    String to print. Default value: empty string.

border
    Indicates if borders must be drawn around the cell. The value can 
    be either a number (0: no border ; 1: frame) or a string containing 
    some or all of the following characters (in any order): L: left ; 
    T: top ; R: right ; B: bottom. Default value: 0.

**new_x** : XPos, str
    New current position in x after the call. Default: RIGHT

**new_y** : YPos, str
    New current position in y after the call. Default: TOP

**ln** : int
    DEPRECATED since 2.5.1: Use new_x and new_y instead.

**align** : Align, str
    Set text alignment inside the cell. Possible values are: L or empty 
    string: left align (default value) ; C: center; X: center around 
    current x position; R: right align

**fill** : bool
    Indicates if the cell background must be painted (True) or 
    transparent (False). Default value: False.

**link** : str
    optional link to add on the cell, internal (identifier returned by 
    FPDF.add_link()) or external URL.

**center** : bool
    center the cell horizontally on the page.

**markdown** : bool
    enable minimal markdown-like markup to render part of text as bold 
    / italics / underlined. Supports \ as escape character. Default to 
    False.

We can print a cell with `cell` method.

`pdf.cell(40,10, 'Hello World!')`

+ A cell is arectangular area, possible framed, which contains some text.
+ It is rendered at the current position.
+ We specify its dimensions, its text (centered or aligned), if 
 borders should be drawn, and where the current position moves after it 
 (to the right, below or to the beginning of the next line).

We can add a frame:

`pdf.cell(40,10, 'Hello World!',1)`

+ where `40` state the width, `10` state the height of the cell
+ The string of text to be print `Hello World!`
+ The integer after the string, `1` indicate border size.

To add a new cell next to it with centered text and place cursor to 
the left in the next line.

`pdf.cell(60, 10, 'Powered by FPDF.', 1, new_x="LMARGIN", new_y="NEXT", align='C')`

Where new_x and new_y:

`new_x="LMARGIN"`

**Purpose:**
This parameter sets the x-coordinate (horizontal position) of the next 
cell or text block to the left margin of the page.

**Usage:**
It's useful for aligning subsequent text blocks or cells with the left 
margin, ensuring consistent alignment on the page.

new_x arguments

The new_x argument specifies the new x-coordinate (horizontal position) 
for the cursor after the cell is rendered. It can have the following 
values:

    "RIGHT": Moves the cursor to the right of the cell.

    "LEFT": Moves the cursor to the left margin.

    "LMARGIN": Moves the cursor to the left margin.

    "RMARGIN": Moves the cursor to the right margin.

    A float value: You can also specify a specific x-coordinate by 
    providing a float value, which sets the cursor position to that 
    exact x-coordinate.

`new_y="NEXT"`

**Purpose:**
This parameter sets the y-coordinate (vertical position) of the next 
cell or text block to the beginning of the next line.

**Usage:**  
It's helpful for ensuring that the next cell or text block starts on a 
new line, preventing overlap with the current cell.

new_y arguments:

The new_y argument specifies the new y-coordinate (vertical position) 
for the cursor after the cell is rendered. It can have the following 
values:

    "TOP": Moves the cursor to the top of the cell.

    "BOTTOM": Moves the cursor to the bottom of the cell.

    "NEXT": Moves the cursor to the beginning of the next line.

    A float value: You can also specify a specific y-coordinate by 
    providing a float value, which sets the cursor position to that 
    exact y-coordinate.

+ Combining `new_x="LMARGIN"` and `new_y="NEXT"` ensures that the next 
cell or text block starts at the left margin of the next line, 
providing consistent layout and alignment.

## output()

`pdf.output("tuto1.pdf")`

the document is closed and saved under the provided file path using 
output. Without any parameter provide, output() returns the PDF 
bytearray buffer. if a name is given, the pdf is written to a new file.

Per documentation

```
def output(self, name='', dest='', linearize=False, 
output_producer_class=fpdf.output.OutputProducer)
```

output() arguments:

**name** : str
    optional File object or file path where to save the PDF under

**dest** : str
    [DEPRECATED since 2.3.0] unused, will be removed in a later version

**output_producer_class** : class
    use a custom class for PDF file generation


# Example 2 - Header, footer, page break and image

```python
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

```

Notes:
+ First we create a class PDF where we inherit from FPDF
`class PDF(FPDF)`
+ We create the header and footer instance methods to process page 
headers and footers. They are called automatically when we use 
FPDF.add_page(). 
They already exist in the FPDF class but do nothing, therefore we have 
to extend the class and override them.
`def header(self):`
`def footer(self):`

The header contains certain methods:

## image()
`self.image("../docs/fpdf2-logo.png", 10, 8, 33)`

Where:

+ name: "../docs/fpdf2-logo.png"
+ x: 10
+ y:  8
+ w: 33

Per documentation:
```
def image(self, name, x=None, y=None, w=0, h=0, type='', link='', 
title=None, alt_text=None, dims=None, keep_aspect_ratio=False)
```

Put an image on the page.

The size of the image on the page can be specified in different ways: 
* explicit width and height (expressed in user units)
* one explicit dimension, the other being calculated automatically in 
order to keep the original proportions
* no explicit dimension, in which case the image is put at 72 dpi. 
* explicit width and height (expressed in user units) and 
keep_aspect_ratio=True 

Remarks: 
* if an image is used several times, only one copy is embedded in the 
file. 
* when using an animated GIF, only the first frame is used.
 

image() arguments:

**name**
    either a string representing a file path to an image, an URL to an 
    image, bytes, an io.BytesIO, or a instance of PIL.Image.Image

**x** : float, Align
    optional horizontal position where to put the image on the page. If 
    not specified or equal to None, the current abscissa is used. 
    Align.C can also be passed to center the image horizontally; and 
    Align.R to place it along the right page margin

**y** : float
    optional vertical position where to put the image on the page. If 
    not specified or equal to None, the current ordinate is used. After 
    the call, the current ordinate is moved to the bottom of the image

**w** : float
    optional width of the image. If not specified or equal to zero, it 
    is automatically calculated from the image size. Pass pdf.epw to 
    scale horizontally to the full page width.

**h** : float
    optional height of the image. If not specified or equal to zero, it 
    is automatically calculated from the image size. Pass pdf.eph to 
    scale horizontally to the full page height.

**type** : str
    [DEPRECATED since 2.2.0] unused, will be removed in a later version.

**link** : str
    optional link to add on the image, internal (identifier returned by 
    FPDF.add_link()) or external URL.

**title** : str
    optional. Currently, never seem rendered by PDF readers.

**alt_text** : str
    optional alternative text describing the image, for accessibility 
    purposes. Displayed by some PDF readers on hover.

**dims** : Tuple[float]
    optional dimensions as a tuple (width, height) to resize the image 
    before storing it in the PDF. Note that those are the intrinsic 
    image dimensions, but the image will still be rendered on the page 
    with the width (w) and height (h) provided as parameters. Note also 
    that the .oversized_images attribute of FPDF provides an automated 
    way to auto-adjust those intrinsic image dimensions.

**keep_aspect_ratio** : bool
    ensure the image fits in the rectangle defined by x, y, w & h while 
    preserving its original aspect ratio. Defaults to False. Only 
    meaningful if both w & h are provided.

If y is provided, this method will not trigger any page break; 
otherwise, auto page break detection will be performed.

Returns: an instance of a subclass of ImageInfo.

## set_y

`self.set_y(-15)`

Moves the current abscissa back to the left margin and sets the 
ordinate. If the value provided is negative, it is relative to the 
bottom of the page.

Per documentation:

`def set_y(self, y)`
 
set_y arguments:

**y** : float
the new current ordinate

##  page_no()

`self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")`

Per documentation:

`def page_no(self)`

Get the current page number

## alias_nb_pages {nb}

`self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")`

Per documentation:

`def alias_nb_pages(self, alias='{nb}')`

Defines an alias for the total number of pages. It will be substituted 
as the document is closed.

This is useful to insert the number of pages of the document at a time 
when this number is not known by the program.

This substitution can be disabled for performances reasons, by calling 
alias_nb_pages(None).

alias_nb_pages {nb} arguments:

    alias : str
        the alias. Defaults to "{nb}". 

## set_auto_page_break()

Set auto page break mode and triggering bottom margin. By default, the 
mode is 'on' and the bottom margin is 2 cm.

Per documentation:

`def set_auto_page_break(self, auto, margin=0)`

set_auto_page_break arguments:

    auto : bool
        enable or disable this mode
    margin : float
        optional bottom margin (distance from the bottom of the page) in the unit specified to FPDF constructor

# Example 3 - Line breaks and colors

```python


```

Notes:

## get_string_width()

`width = self.get_string_width(self.title) + 6`

Returns the length of a string in user unit. A font must be selected. 
The value is calculated with stretching and spacing. 
Note that the width of a cell has some extra padding added to this 
width, on the left & right sides, equal to the .c_margin property.

Per documentation:

`def get_string_width(self, s, normalized=False, markdown=False)`

get_string_width arguments:

    s : str
        the string whose length is to be computed.
    normalized : bool
        whether normalization needs to be performed on the input string.
    markdown : bool
        indicates if basic markdown support is enabled

# Color

## set_draw_color()

`self.set_draw_color(0, 80, 180)`

Defines the color used for all stroking operations (lines, rectangles 
and cell borders). Accepts either a single greyscale value, 3 values as 
RGB components, a single #abc or #abcdef hexadecimal color string, or 
an instance of DeviceCMYK, DeviceRGB or DeviceGray. The method can be 
called before the first page is created and the value is retained from 
page to page.

Per documentation:

`def set_draw_color(self, r, g=-1, b=-1)`

set_draw_color arguments:

    r : int, tuple, DeviceGray, DeviceRGB
        if g and b are given, this indicates the red component. Else, this indicates the grey level. The value must be between 0 and 255.
    g : int
        green component (between 0 and 255)
    b : int
        blue component (between 0 and 255)


## set_fill_color()

`self.set_fill_color(230, 230, 0)`

Defines the color used for all filling operations (filled rectangles 
and cell backgrounds). Accepts either a single greyscale value, 3 
values as RGB components, a single #abc or #abcdef hexadecimal color 
string, or an instance of DeviceCMYK, DeviceRGB or DeviceGray. The 
method can be called before the first page is created and the value is 
retained from page to page.

Per documentation:

`def set_fill_color(self, r, g=-1, b=-1)`

set_fill_color arguments:

    r : int, tuple, DeviceGray, DeviceRGB
        if g and b are given, this indicates the red component. Else, this indicates the grey level. The value must be between 0 and 255.
    g : int
        green component (between 0 and 255)
    b : int
        blue component (between 0 and 255)




## set_text_color

`self.set_text_color(220, 50, 50)`

Defines the color used for text. Accepts either a single greyscale 
value, 3 values as RGB components, a single #abc or #abcdef hexadecimal 
color string, or an instance of DeviceCMYK, DeviceRGB or DeviceGray. 
The method can be called before the first page is created and the value 
is retained from page to page.

Per documentation:

`def set_text_color(self, r, g=-1, b=-1)`


set_text_color arguments:

    r : int, tuple, DeviceGray, DeviceRGB
        if g and b are given, this indicates the red component. Else, this indicates the grey level. The value must be between 0 and 255.
    g : int
        green component (between 0 and 255)
    b : int
        blue component (between 0 and 255)

## set_line_width()

`self.set_line_width(1)`

Defines the line width of all stroking operations (lines, rectangles and cell borders). By default, the value equals 0.2 mm. The method can be called before the first page is created and the value is retained from page to page.

`def set_line_width(self, width)`

set_line_width arguments:

    width : float
        the width in user unit

##  set_x()

Defines the abscissa of the current position. If the value provided is 
negative, it is relative to the right of the page.

Per documentation:

`def set_x(self, x)`

set_x arguments:

    x : float
        the new current abscissa




