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
            width,
            30,
            self.title,
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
pdf.add_page("P", "a4")  # Default is "P" and "a4"

# Print the image
pdf.image(
    "E:\CS50P\set8\shirtificate\shirtificate.png",
    5,                # Centre horizontally (image's width + 2x == 210)
    (297 - 220) / 2,  # Centre vertically (image's height + 2y == 297)
    w=200,            # Reshape the image's width
    h=220             # Reshape the image's height
    ) 

# Set font:
pdf.set_font("Helvetica", "B", 20)
width = pdf.get_string_width(cert)

# Print text:
pdf.cell(
    w=width,
    h=20,
    txt=cert,
    border=0,
    new_x="C",
    new_y="NEXT",
    align="C",
    fill=False
    )

# Generate the file
pdf.output("E:\CS50P\set8\shirtificate\\result.pdf")