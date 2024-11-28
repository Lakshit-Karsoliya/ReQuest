
from LLM_Interface import Interface
from streamlit_tags import st_tags
import streamlit as st
import json
import re 
from HandyFunctions import create_pdf
from datetime import datetime

st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>""", unsafe_allow_html=True)
st.markdown(r"""<style>.stAppDeployButton {visibility: hidden;}</style>""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    div.stButton > button {
        color: #000; /* Set the foreground/text color */
        background-color: #ff9900; /* Optional: button background */
        border: 1px solid #ff9900; /* Optional: border styling */
    }
    div.stButton > button:hover {
        color: #000000; /* Text color on hover */
        background-color: #ffbb00; /* Background color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login_page():
    st.markdown("<h1 style='text-align: center; color:#ff9900'>ReQuest</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>ReQuestr: Turn one question into countless possibilities for smarter practice!</h5>", unsafe_allow_html=True)
    st.write('---')
    st.markdown("<h3 style='text-align: center;'>Disclamer</h3>", unsafe_allow_html=True)
    st.markdown("""
    Language Models (LLMs) are **undeterministic** and can sometimes produce unexpected or inappropriate results. 
    Please be aware that while LLMs strive for accuracy, they may occasionally generate incorrect or biased information. 
    By proceeding, you acknowledge the risks associated with using such models. 
    
    **Please confirm:**
    Are you over 18 years old and aware of these potential risks?
    """)
    if st.button("Yes, I am 18 or older"):
            st.session_state.authenticated = True
            st.rerun()

def main_page():
    st.markdown("<h1 style='text-align: center; color:#ff9900'>ReQuest</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>ReQuestr: Turn one question into countless possibilities for smarter practice!</h5>", unsafe_allow_html=True)
    st.write('---')
   
    user_input = st.text_area("Enter Your Question Here", height=150)

    tags = st_tags(
        label="Enter Tags",
        text="Write a tag name and press enter to add more tags",
        value=['medium level'],
        suggestions=["ml", "dl", "ai"],
        key="tags"
    )

    direction = ','.join(tags)

    slider_value = st.slider("Select Number Of Questions", min_value=1, max_value=5, step=1,value=1)
    interface_object = Interface()
    
    #for runpod 
    interface_object.initiate_runpod_interface()

    with open('prompts.json') as f:
        templates = json.load(f)
    if st.button("Generate Similar Questions"):
        if len(user_input)>0:
            placeholder = st.empty()
            val = ""
            prompt = templates["prompt_for_checking_weather_we_got_a_question_or_not"].format(question=user_input)
           
            runpod_generator = interface_object.generate_runpod_response(prompt)
            
            for token in runpod_generator:
                val += token
            print(f"Model Judgement : {val}")
            if val == '1':
                prompt = templates["prompt_for_generating_similar_question"].format(question=user_input, direction=direction,no_of_question=slider_value)
    
                runpod_generator = interface_object.generate_runpod_response(prompt)
                val=""
                for token in runpod_generator:
                    val += token
                print(f"Model Generated Questions : {val}")
                questions = re.findall(r'<QUESTION>(.*?)</QUESTION>', val, re.DOTALL)
                to_pr=''
                for i in range(len(questions)):
                    question = questions[i]
                    question = question.replace('\n','\n\n')
                    to_pr+=str(i+1)+"."+question+"\n\n\n"
                placeholder.write(to_pr)
                pdf_data = create_pdf(to_pr)
                now = datetime.now()
                formatted_time_date = now.strftime("%H_%M_%S_%d_%b_%Y")
                st.download_button(
                    label="Download PDF",
                    data = pdf_data,
                    file_name=f"Generated_Questions_{formatted_time_date}.pdf",
                    mime="application/pdf"
                )
            else:
                st.warning("Please Enter a Quesion")
        else:
            st.warning("Please Enter Valid Value")


if st.session_state.authenticated:
    main_page()
else:
    login_page()

