import streamlit as st

col1, col2 = st.columns(2, gap='small', vertical_alignment='bottom')

col1.image('assets/foto_perfil.png', width=250)
col2.header("Welcome to Samuel Rangel's Website")
col2.write('Data Analyst | Data Scientist | Data Engineer')

st.subheader('🙋‍♂️ About me:',divider='red')

st.write(''' 

I am a professional with a Bachelor’s degree in Chemistry, with experience as a Data Analyst, applying the scientific method in the extraction and analysis of information, combining my knowledge in Chemistry, and Science in general, with programming and data management skills. I have experience in Python and tools such as NumPy, Pandas, Matplotlib, Seaborn, FastAPI, Power BI and Streamlit, as well as version control with Git and GitHub.


Not only that, but I also manage databases such as MySQL and BigQuery, along with data visualization skills and effective communication, developed through my experience as a teacher and tutor. My main motivation is the continuous learning and the optimization of data-driven processes.

🛠 __Technical skills:__
         
Languages: Python
        
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit.
        
Visualization tools: Power BI, Tableau, Looker Studio.
        
Data: MySQL, BigQuery.

Version Control: Git, GitHub.
         
🎓 __Background:__
         
I have a Data-Science certificate 👨‍💻 from Soy Henry

I have a Bachelor of Science in Chemistry 👨‍🔬 from Universidad Central de Venezuela

📫 __How to reach me:__
         
LinkedIn: https://www.linkedin.com/in/samuel-antonio-rangel-sar021/
          
Email: samuel.rangel.021@gmail.com
''')
st.subheader('My Resume:',divider='red')

language = st.radio('Language',['English','Spanish'], horizontal=True, label_visibility='collapsed')

if language == 'Spanish':
    with open('assets/Samuel Antonio Rangel- CV - Analista de Datos.pdf', "rb") as file:
        btn = st.download_button(
            label="Download Spanish CV",
            data=file,
            file_name="Samuel Antonio Rangel- CV - Analista de Datos.pdf",
            )

if language == 'English':
    with open('assets/Samuel Antonio Rangel- CV - Data Analyst.pdf', 'rb') as file:
        btn = st.download_button(
            label="Download English CV",
            data=file,
            file_name="Samuel Antonio Rangel- CV - Data Analyst.pdf",
        )