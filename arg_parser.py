from argparse import ArgumentParser

class ArgParser:
    def __init__(self):
        self.root = ArgumentParser(description='Program for translating the test to PDF')
        self.add_arguments()

    def add_arguments(self):
        self.root.add_argument("-m", "--method", choices=["files", "file", "folder"], type=str, help="How to read text", required=True)
        self.root.add_argument("-i", "--input", nargs='+', type=str, help="File/files/folder path", required=True)
        self.root.add_argument("-o", "--output", type=str, help="File path", required=True)

    def start_parse(self):
        return self.root.parse_args()
