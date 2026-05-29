class Fileexport:
    def export(self,data):
        pass
class PDFExport(Fileexport):
    def export(self,data):
        print(f"export pdf data:{data}")

class ExcelExporter(Fileexport):
    def export(self,data):
        print(f"export the excel data:{data}")

class CSVEExporter(Fileexport):
    def export(self,data):
        print(f"expoert the csve:{data}")    


def process_export(Fileexport,data):
    Fileexport.export(data) 


pdf=PDFExport()
excel=ExcelExporter()
csve=CSVEExporter()

process_export(pdf,"okay")
process_export(excel,"andi")
process_export(csve,"vara")

