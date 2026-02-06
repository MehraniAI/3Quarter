# hackathon_app.py
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Hackathon Project 2026",
    page_icon="🚀",
    layout="wide"
)

# --- HEADER ---
st.markdown(
    """
    <div style="text-align:center; padding:50px; background: linear-gradient(135deg, #ffb703, #fb8500); border-radius:12px;">
        <h1 style="color:#000;">Hackathon Project 2026</h1>
        <p style="color:#000; max-width:700px; margin:auto;">
        A professional multi-phase hackathon project focused on problem solving,
        reusable intelligence, and real-world software development.
        </p>
    </div>
    """, unsafe_allow_html=True
)

# --- ABOUT ---
st.subheader("About the Hackathon")
st.markdown(
    """
    This hackathon is designed to simulate real-world industry challenges.
    Participants work through multiple phases including ideation, design,
    implementation, testing, and final presentation.

    The goal is not just to complete a task, but to build scalable, reusable,
    and intelligent solutions that can be used in future projects and hackathons.
    """
)

# --- OBJECTIVES & SKILLS ---
st.subheader("Objectives & Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Objectives")
    st.markdown(
        """
        - Solve real-world problems  
        - Build structured solutions  
        - Develop reusable components  
        - Improve logical thinking
        """
    )

with col2:
    st.markdown("### 🛠 Skills Used")
    st.markdown(
        """
        - HTML & CSS  
        - JavaScript (optional)  
        - Problem solving  
        - Presentation & documentation
        """
    )

# --- HACKATHON PHASES ---
st.subheader("Hackathon Phases")
st.markdown(
    """
    1. **Phase 1:** Idea & planning  
    2. **Phase 2:** UI / system design  
    3. **Phase 3:** Implementation  
    4. **Phase 4:** Testing & improvements  
    5. **Phase 5:** Final submission & presentation
    """
)

# --- LIVE DEMO ---
st.subheader("Live Demo")

st.markdown("Click the button below to see an interactive feature:")

if st.button("Show Demo"):
    st.success("🚀 Demo Activated! Your project is running live here.")

# --- PRESENTATION ---
st.subheader("Presentation to NAD / Jury")
st.markdown(
    """
    This project will be presented in a professional manner including:
    - Clear explanation of the problem
    - Live demo of the solution
    - Code walkthrough
    - Future scope and improvements

    Focus is on clarity, structure, and how the solution can scale in real-world applications.
    """
)

# --- FUTURE SCOPE ---
st.subheader("Future Scope")
st.markdown(
    """
    - Add backend integration  
    - Improve UI/UX  
    - Make the system fully dynamic  
    - Deploy as a live web application  
    - Integrate APIs for real-time data
    """
)

# --- TEAM & RESOURCES ---
st.subheader("Team & Resources")
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 👥 Team Members")
    st.markdown(
        """
        - Devan Das – Project Lead  
        - Member 2 – UI Designer  
        - Member 3 – Backend Developer
        """
    )

with col4:
    st.markdown("### 📂 Resources")
    st.markdown(
        """
        - [Project GitHub Repository](#)  
        - [Download Project Files](#)  
        - [Documentation PDF](#)
        """
    )

# --- CONTACT ---
st.subheader("Contact Information")
st.markdown(
    """
    - Email: [ddmehraifd@gmail.com](mailto:ddmehraifd@gmail.com)  
    - Phone: 0332-2694215  
    © 2026 Hackathon Project
    """
)
