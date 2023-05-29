from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_auto_page_break(auto=False, margin=0)
dataFrame = pandas.read_csv("topics.csv", sep=",")

for index, row in dataFrame.iterrows():
    pdf.add_page()  # parent page
    pdf.set_font(family="Times",style="B", size=24)
    pdf.set_text_color(50, 50, 50)
    pdf.line(10, 26, 200, 26)
    pdf.cell(w=0, h=24, txt=row['Topic'], align="L", ln=1)

    pdf.ln(243)  # a break line for fotter
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    pages = row['Pages'] - 1
    for i in range(pages):
        pdf.add_page()
        pdf.ln(266)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=8, align="R", txt=row["Topic"])


pdf.output("output.pdf")