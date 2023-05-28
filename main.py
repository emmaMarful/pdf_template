from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
dataFrame = pandas.read_csv("topics.csv", sep=",")

for index, row in dataFrame.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B", size=24)
    pdf.set_text_color(50, 50, 50)
    pdf.line(10, 26, 200, 26)
    pdf.cell(w=0, h=24, txt=row['Topic'], align="L", ln=1)

    pages = row['Pages'] - 1
    for i in range(pages):
        pdf.add_page()


pdf.output("output.pdf")