# from PIL import Image
# Take data about the image shirtificate.png for adjustment
# shirt = Image.open("E:\CS50P\set8\shirtificate\shirtificate.png")
# print(shirt.size)
from fpdf import FPDF


class PDF(FPDF):
    def header(self) -> None:
        # Set the font of the header/title
        self.set_font("Helvetica", "B", 45)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)  # Put the cursor to a place where the title when printed will be centered
        # Setting colors for text:
        self.set_text_color(0, 0, 0)  # black
        # Printing title:
        self.cell(
            w=width,
            h=45,
            txt=self.title,
            border=0,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=False,
        )


cert = f"{input('Your name: ')} took CS50"

# Set the pdf's properties
pdf = PDF()
pdf.set_title("CS50 Shirtificate")
# Add a page which automatically add the header
pdf.add_page("P", "a4")  # Default is "P" and "a4"

# Print the image
pdf.image(
    "E:\CS50P\set8\shirtificate\shirtificate.png",
    x=5,                # Centre horizontally (image's width + 2x == 210)
    y=(297 - 210) / 2,  # Centre vertically (image's height + 2y == 297)
    w=200,            # Reshape the image's width
    h=210             # Reshape the image's height
    ) 

# The part below is to generate the text on the shirt
# Set font and a new title:
pdf.set_title(cert)
pdf.set_font("Helvetica", "B", 32)

# Set color for the text
pdf.set_text_color(255, 255, 255)

# Calculating width of text and setting cursor position:
pdf.set_y((297 / 2) - (210 / 4)) # Put the cursor vertically so that it lands on top of the shirt
width = pdf.get_string_width(cert) + 6
pdf.set_x((210 - width) / 2)  # Change the x-coordinate of the cursor so that the text when printed will be centered

# Print text:
pdf.cell(
    w=width,
    h=32,
    txt=cert,
    border=0,
    new_x="LMARGIN",
    new_y="NEXT",
    align="C",
    fill=False
    )

# Generate the file
pdf.output("shirtificate.pdf")
