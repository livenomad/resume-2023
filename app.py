from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "MTR.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | MacklinThomas"
PAGE_ICON = ":wave:"
NAME = "Macklin Thomas"
DESCRIPTION = """
Junior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "Macklinthomas5@gmail.com"
SOCIAL_MEDIA = {
#    "YouTube": "https://youtube.com/c/codingisfun"
    "LinkedIn": "https://www.linkedin.com/in/macklin-thomas-500571133?trk=people-guest_people_search-card",
    "GitHub": "https://github.com/livenomad",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 Digital Resume": "https://livenomad-resume-2023-app-zvlsta.streamlit.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years experience extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displays strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | ConocoPhillips**")
st.write("09/2017 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding automation initiatives, and supplied recommendations to reduce work-hours by 30%.
- ► Lead a team of 4 analysts to brainstorm potential RPA improvements, and implemented A/B tests to generate 15% increase in productivity.
- ► Compiled, studied, and inferred large amounts of data, modeling oil well information to drive asset management.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Python Developer | Shell Energy**")
st.write("02/2018 - 08/2018")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful eﬀorts.
- ► Redesigned data models through iterations that improved predictions by 30%.
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive sales efforts.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | MP2 Energy**")
st.write("05/2017 - 01/2018")
st.write(
    """
- ► Devised KPIs using Excel and SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic sales.
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customer satisifaction.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
