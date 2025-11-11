# Separate Interfaces
class Printable:
    def print_document(self, document):
        pass
class Scannable:
    def scan_document(self, document):
        pass
class Faxable:
    def fax_document(self, document):
        pass
class BasicPrinter(Printable):
    def print_document(self, document):
        print(f"Printing: {document}")

class AdvancedPrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        print(f"Printing: {document}")
    def scan_document(self, document):
        print(f"Scanning: {document}")
    def fax_document(self, document):
        print(f"Faxing: {document}")
if __name__ == "__main__":
    basic_printer = BasicPrinter()
    basic_printer.print_document("Doc1.pdf")

    advanced_printer = AdvancedPrinter()
    advanced_printer.print_document("Doc2.pdf")
    advanced_printer.scan_document("Doc2.pdf")
    advanced_printer.fax_document("Doc2.pdf")
