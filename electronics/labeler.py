import labels as labels
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

def write_label(label, width, height, data):
    # Measure the width of the name and shrink the font size until it fits.

    for i, (string, size) in enumerate(data.get('left', [])):
        s = shapes.String(3, height-15 * (i+1), string)
        s.fontName = "Helvetica"
        s.fontSize = shrink_font(string, width, size)
        label.add(s)


    for i, (string, size) in enumerate(data.get('right', [])):
        ref_width = stringWidth(string, "Helvetica", size)
        s = shapes.String(width-3-ref_width, height-12*(i+1), string)
        s.fontName = "Helvetica"
        s.fontSize = size
        label.add(s)

def write_labels(labelobjs, partials=[], ):
    # Create the sheet.
    sheet = labels.Sheet(specs, write_label, border=False)
    sheet.partial_page(1, partials)
    sheet.add_labels(label for label in labelobjs)
    # Save the file and we are done.
    sheet.save('/tmp/labels.pdf')
    print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))


