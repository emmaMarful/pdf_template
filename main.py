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

    # lines. Page One
    lnn = 27
    nextLine = 26
    for i in range(lnn):
        pdf.line(10, nextLine, 200, nextLine)
        nextLine = nextLine + 10

    # a break line for footer. Page One
    pdf.ln(254)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # additional iterated pages
    pages = row['Pages'] - 1
    for i in range(pages):
        pdf.add_page()
        pdf.ln(280)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=8, align="R", txt=row["Topic"])
        pdf.line(10, 15, 200, 15)

        lnn = 250
        nextLine2 = 30
        for l in range(lnn):
            pdf.line(10, nextLine2, 200, nextLine2)
            nextLine2 = nextLine2 + 10




pdf.output("output.pdf")