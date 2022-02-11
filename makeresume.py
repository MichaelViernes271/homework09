# NOTE: install 'python pip install fpdf2'
import json
from fpdf import FPDF


# json file casting
person = None
with open('person.json') as p:
    person = json.load(p)    

# initialize FPDF library to be used
pdf = FPDF('p', 'cm', 'Letter')
pdf.add_page()
pdf.set_margin(2)
pdf.set_font('times', '', 1)

# my top profile
pdf.set_font('times', 'B', 20)
pdf.cell(0, 2, person['name'], ln=1)
pdf.cell(0, 1, person['role'])
pdf.ln(1)
pdf.cell(20) # padding my image
pdf.image('michael.JPG', 16,2.25,3)

# profile description
pdf.set_font('times', 'B', 14)
pdf.cell(0, 1, 'Description:', ln=1)
pdf.set_font('times', '', 12) # for the desciption
pdf.multi_cell(0,1, person['desc'], ln=1)

# my contacts
pdf.set_font('times', 'B', 14)
pdf.cell(0, 1, 'Contacts:', ln=1)
pdf.set_font('times', '', 12)
pdf.cell(6,1, "Phone: " + person['phone'])
pdf.cell(6,1, "E-mail: " + person['email'], ln=1)
pdf.cell(0,1, "Linkedin: " + person['linkedin'], ln=1)


#my relevant skills
pdf.set_font('times', 'B', 14)
pdf.cell(0, 1, 'Relevant Skils:', ln=1)
pdf.set_font('times', '', 12)
skills = ', '.join(person['relevancy'])
pdf.cell(0, 1, skills, ln=1)


# work exp
pdf.set_font('times', 'B', 14)
pdf.cell(0, 1, 'Experience:', ln=1)
for i in range(0,9,3):
    pdf.set_font('times', '', 12)
    pdf.cell(0, 1, person['workexp'][i] + " | " + person['workexp'][i+1] + " | " + person['workexp'][i+2], ln=1)


# education level      
pdf.set_font('times', 'B', 14)
pdf.cell(0, 1, 'Education:', ln=1)
for i in range(0,6,3):
    pdf.set_font('times', '', 12)
    pdf.cell(0, 1, person['workexp'][i] + " | " + person['workexp'][i+1] + " | "  + person['workexp'][i+2], ln=1)

# referral
pdf.set_font('times', 'B', 14)
pdf.cell(0, 1, 'Reference:', ln=1)
pdf.set_font('times', '', 12)
pdf.cell(0, 1, person['reference'])

# make resume
pdf.output('VIERNES_MICHAEL.pdf')