import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini with the secure API key
genai.configure(api_key=api_key)

models = list(genai.list_models())
for model in models:
    print(model)

def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input, generation_config=genai.types.GenerationConfig(temperature=0))
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Streamlit app
st.title("CAREER CONNECTOR")
st.markdown(
    """
    <style>
    .title {
        font-size: 24px;
        color: #A52A2A;
    }
    .text-area {
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
    }
    .file-uploader {
        margin-bottom: 20px;
    }
    .submit-button {
        background-color: #007bff;
        color: #0000ff;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .submit-button:hover {
        background-color: #1338BE;
    }
    img .image{
    height:100px;
    }
     </style>
    """,
    unsafe_allow_html=True
)

st.header("Welcome to Career Connector!")
st.write("Career Connector is your go-to tool for optimizing your resume to match job descriptions effectively. Upload your resume and paste the job description to get detailed feedback on how well your resume aligns with the job requirements.")
st.image("https://assets-global.website-files.com/627c8700df0be67c4b1d533c/65319680bcee14a021a3dc7f_Show_Me_Checker-p-800.png")
st.write("Our advanced AI technology evaluates your resume against the job description, highlighting areas of improvement, missing keywords, grammar and spelling errors, and much more.")

st.header("How it helps")
st.write("With Career Connector, you can:")
st.write("- Optimize your resume to increase its chances of getting noticed by recruiters.")
st.write("- Ensure that your resume highlights relevant skills and experiences demanded by the job.")
st.image("https://img.freepik.com/premium-vector/recruitment-job-search-isometric-concept-use-presentation-social-media-cards-web-banner-illustration_106788-1272.jpg")
st.write("- Receive real-time feedback on grammar, spelling, and formatting to present a polished resume.")
st.write("- Save time and effort by automating the resume optimization process.")

st.header("Analyze your resume ")
st.write("Get real-time feedback and expert tips with our resume checker. ")
st.markdown('<div class="title">Improve Your Resume</div>', unsafe_allow_html=True)
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        input_prompt = f"""
Hey Act Like a skilled or very experienced ATS(Application Tracking System), with extensive experience in evaluating resumes against job descriptions. Be a strict checker. Let's dive into the evaluation process based on the provided job description:

1. Get Resume Text: Extract the full resume text enclosed in triple backticks (```).
2. Evaluate Resume: Thoroughly analyze the entire resume text, considering the competitive job market.
3. Assign Percentage Based on JD Matching: Determine the percentage of match between the job description (JD) enclosed in triple quotes (''') and the resume text. This percentage indicates the likelihood of the candidate's resume being shortlisted for the job based on the matched text from the JD. If there is an exact match assign percentage greater than 95. If there is a good match assign % greater than 75. If the match is moderate assign % greater than 60 and if the match is not that good assign percentage around 10.
4. Identify Missing Keywords: List the missing keywords representing skills, technologies, or tools knowledge from the job description. These keywords should ideally be present in the resume. Separate the missing keywords with commas in a different section for easy identification and consideration.
5. Check Grammar and Spelling: Review the resume for grammar and spelling errors since human errors are common.
6. Highlight Grammar and Spelling Mistakes: Identify lines or words with incorrect grammar or spelling for correction.
8. Assess Work Experience: Examine the work experience section and provide suggestions for improvement in the format of old text -> suggested new text. Only suggest the lines where major improvement is required not all.
9. Find Opportunities for Quantifiable Figures: Identify areas in the resume where quantifiable figures (e.g., percentages, numbers) can be added, excluding lines already containing figures or percentages. Limit suggestions to lines where you are 100% confident in the format of old text -> suggested new text.
10. Maintain Consistency: Ensure a consistent output format for each section, regardless of the provided job description and resume.

resume: ```{text}```
description: '''{jd}'''

Below is the desired output structure for each section:

JD Match in %
Missing Keywords in an enclosed list comma-separated
Grammar and Spelling Errors
Experience Updates in the format of old text -> suggested new text
Lines where I can add quantifiable figures mostly in '%' or in numbers in the format of old text -> suggested new text"""
        response = get_gemini_repsonse(input_prompt)
        st.subheader("Career Connector Results:")
        st.write(response)

st.markdown('<div class="scroll-down"></div>', unsafe_allow_html=True)
st.write("Thank you for choosing Career Connector!")