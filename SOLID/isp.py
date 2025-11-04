class Printer:
    def print_document(self, document):
        pass
    def scan_document(self, document):
        pass
    def fax_document(self, document):
        pass
class BasicPrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")
    def scan_document(self, document):
        raise NotImplementedError("This printer cannot scan.")
    def fax_document(self, document):
        raise NotImplementedError("This printer cannot fax.")
if __name__ == '__main__':
    basic_printer = BasicPrinter()
    basic_printer.print_document("Document2.pdf")
    basic_printer.scan_document("Document2.pdf")  
    basic_printer.fax_document("Document2.pdf")   
