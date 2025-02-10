import streamlit as st

homepage = st.Page(
    page='homepage.py',
    title='Home',
    default=True
)
projects = st.Page(
    page = 'projects.py',
    title = 'Projects'
)

navigator = st.navigation(
    [homepage, projects]
)

if __name__ == '__main__':
    navigator.run()