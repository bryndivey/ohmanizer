import labels
import os.path
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont, stringWidth
from reportlab.graphics import shapes
from reportlab.lib import colors

# Create an A4 portrait (210mm x 297mm) sheets with 2 columns and 8 rows of
# labels. Each label is 90mm x 25mm with a 2mm rounded corner. The margins are
# automatically calculated.
specs = labels.Specification(210, 297, 5, 13, 38.1, 21.2,
                             #left_margin=4.2,
                             #right_margin=4,
                             column_gap=2.8,
                             top_margin=14,
                             #bottom_margin=10.7,
                             row_gap=0,
                             corner_radius=2)

def shrink_font(text, width, start_size=10):
    font_size = start_size
    text_width = width - 10
    name_width = stringWidth(text, "Helvetica", font_size)
    while name_width > text_width:
        font_size *= 0.8
        name_width = stringWidth(text, "Helvetica", font_size)
    return font_size

def write_part(label, width, height, part):
    # Measure the width of the name and shrink the font size until it fits.
    s = shapes.String(3, height-15, part.component.name)
    s.fontName = "Helvetica"
    s.fontSize = shrink_font(part.component.name, width)
    label.add(s)

    s = shapes.String(3, height-30, part.component.type.name)
    s.fontName = "Helvetica"
    s.fontSize = shrink_font(part.component.name, width, 8)
    label.add(s)

    ref_width = stringWidth(part.tag, "Helvetica", 6)
    s = shapes.String(width-3-ref_width, height-12, part.tag)
    s.fontName = "Helvetica"
    s.fontSize = 6
    label.add(s)

def write_parts(parts):
    # Create the sheet.
    sheet = labels.Sheet(specs, write_part, border=False)
    sheet.add_labels(part for part in parts)
    # Save the file and we are done.
    sheet.save('parts.pdf')
    print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))


from models import Label
def make_labels():
    labels = Label.ojects.all()
    write_parts(labels)
