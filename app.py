from arg_parser import ArgParser
try:
    from text_to_pdf import TextToPDF
except ModuleNotFoundError:
    print("pip install fpdf")
    exit()

def main():
    pdf = TextToPDF()
    arg = ArgParser()
    argv = arg.start_parse()
    if argv.method == "file":
        pdf.input_from_file(argv.input[0])
    elif argv.method == "files":
        pdf.input_from_files(argv.input)
    elif argv.method == "folder":
        pdf.input_from_package(argv.input[0])
    pdf.output(argv.output)
    if pdf.errors:
        for error in pdf.errors:
            print(error)
    else:
        print("Success")

if __name__ == "__main__":
    main()
