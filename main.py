import streamlit as st

homepage = st.Page(
    page='sections/homepage.py',
    title='Home',
    default=True
)
projects = st.Page(
    page = 'sections/projects.py',
    title = 'Projects'
)

navigator = st.navigation(
    [homepage, projects]
)

if __name__ == '__main__':
    navigator.run()