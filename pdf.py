import os
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, font):
        super().__init__()
        self.add_page()
        self.font = font
        self.set_fonts()

    def chapter_title(self, path):
        self.set_font(self.font, 'B', 12)
        file_name = os.path.basename(path)
        self.cell(0, 5, file_name, align='C')
        self.ln()

    def chapter_body(self, path):
        with open(path, 'rb') as fh:
            txt = fh.read().decode('utf-8')
        self.set_font(self.font, '', 9)
        self.multi_cell(0, 5, txt)
        self.ln()

    def print_chapter(self, path):
        self.chapter_title(path)
        self.chapter_body(path)

    def set_fonts(self):
        self.add_font('JetBrainsMono', '', 'data/JetBrainsMono-Regular.ttf', uni=True)
        self.add_font('JetBrainsMono', 'B', 'data/JetBrainsMono-Bold.ttf', uni=True)
        self.add_font('DejaVu', '', 'data/DejaVuSansCondensed.ttf', uni=True)
        self.add_font('DejaVu', 'B', 'data/DejaVuSansCondensed-Bold.ttf', uni=True)




