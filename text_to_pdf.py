import os
from pdf import PDF

class TextToPDF:
    def __init__(self, font='JetBrainsMono'):
        self.pdf = PDF(font)
        self.errors = []

    def input_from_file(self, path):
        try:
            self.pdf.print_chapter(path)
        except (FileNotFoundError, PermissionError) as ex:
            self.errors.append(f"{path} file does not exist")

    def input_from_files(self, paths):
        for path in paths:
            self.input_from_file(path)

    def input_from_package(self, path, extension=".java"):
        try:
            # files = [path + "/" + file_path for file_path in os.listdir(path) if file_path.endswith(extension)]
            files = [path + "/" + file_path for file_path in os.listdir(path)]
            self.input_from_files(files)
        except FileNotFoundError as ex:
            self.errors.append(f"{path} folder does not exist")

    def output(self, path):
        try:
            self.pdf.output(path, 'F')
        except FileNotFoundError as ex:
            self.errors.append(f"{path} folder does not exist")
