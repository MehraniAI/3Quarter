import streamlit as st
import pandas as pd
import os

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Hackathon Book Course Academy",
    layout="wide",
    page_icon="🤖"
)

# ---------------------------------------------------------
# CUSTOM CSS FOR BETTER DESIGN
# ---------------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #f8f9fa;
}
.nav-title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 10px;
}
.section-title {
    font-size: 30px;
    font-weight: bold;
    margin-top: 35px;
    margin-bottom: 10px;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background: white;
    box-shadow: 0 3px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.footer {
    background: black;
    color: white;
    padding: 15px;
    text-align: center;
    margin-top: 40px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DATA FILE FOR REGISTRATION
# ---------------------------------------------------------
DATA_FILE = "registrations.csv"
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Email", "Course", "Phone", "Experience"])
    df.to_csv(DATA_FILE, index=False)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "About", "Hackathon", "Courses", "Mentors", "Gallery", "Books", "Register", "Admin"]
)

# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------
if page == "Home":
    st.markdown("<div class='nav-title'>🤖 Hackathon Book Course Academy</div>", unsafe_allow_html=True)
    st.write("Where AI meets Robots — and the future gets built by legends like you.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn.pixabay.com/photo/2017/01/31/21/23/robot-2027195_1280.png")

    with col2:
        st.markdown("""
        ### 🌟 Why RoboHack?
        - Next-gen AI + Robotics hub  
        - Real humanoid robot training  
        - International-level hackathons  
        - Hands-on physical AI labs  
        - Learn like you're speedrunning life  
        """)

# ---------------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------------
elif page == "About":
    st.markdown("<div class='section-title'>🏫 About RoboHack Academy</div>", unsafe_allow_html=True)
    st.write("""
    RoboHack Academy is designed for creators, dreamers, and builders.  
    A place where robots, AI, and imagination connect.
    """)

# ---------------------------------------------------------
# HACKATHON PAGE
# ---------------------------------------------------------
elif page == "Hackathon":
    st.markdown("<div class='section-title'>⚡ RoboHack 2024 – Mega Hackathon</div>", unsafe_allow_html=True)

    st.write("""
    A 24-hour battle of brains, bots, and pure caffeine energy.  
    Compete, learn, and dominate with your team.
    """)

    st.subheader("🏆 Competitions")
    st.write("""
    - Best Humanoid Robot  
    - Best AI Agent  
    - Best Autonomous Vehicle  
    - Best Physical AI Project  
    """)

    st.subheader("🎁 Prizes")
    st.write("""
    - Laptops, robots, kits  
    - Cash & trophies  
    - Certificates  
    """)

# ---------------------------------------------------------
# COURSES PAGE
# ---------------------------------------------------------
elif page == "Courses":
    st.markdown("<div class='section-title'>📚 Courses Offered</div>", unsafe_allow_html=True)

    st.markdown("### 🤖 Humanoid Robotics")
    st.write("Motors, actuators, balance control, sensors, AI movement algorithms.")

    st.markdown("### 🧠 Physical AI")
    st.write("Machines that sense, think, move, and react like biological organisms.")

    st.markdown("### 🔌 Sensor Systems")
    st.write("LIDAR, IMU, Computer Vision, ESP32, Raspberry Pi.")

    st.markdown("### 📈 Machine Learning for Robots")
    st.write("YOLO, RL, OpenCV, LLM agents, robotics navigation.")

# ---------------------------------------------------------
# MENTORS PAGE
# ---------------------------------------------------------
elif page == "Mentors":
    st.markdown("<div class='section-title'>👨‍🏫 Meet the Mentors</div>", unsafe_allow_html=True)

    cols = st.columns(3)
    mentors = [
        ("Dr. Arif", "AI Scientist"),
        ("Nida Ali", "Robotics Engineer"),
        ("Rohan Kumar", "Embedded Systems Expert")
    ]

    for i, (name, role) in enumerate(mentors):
        with cols[i]:
            st.markdown(f"""
            <div class='card'>
                <h3>{name}</h3>
                <p>{role}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------------
# GALLERY PAGE
# ---------------------------------------------------------
elif page == "Gallery":
    st.markdown("<div class='section-title'>📸 Event Gallery</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://cdn.pixabay.com/photo/2016/11/19/17/24/robot-1840566_1280.jpg")
    with col2:
        st.image("https://cdn.pixabay.com/photo/2021/03/31/09/38/robot-6141782_1280.jpg")
    with col3:
        st.image("https://cdn.pixabay.com/photo/2017/06/15/20/56/artificial-intelligence-2406357_1280.jpg")

# ---------------------------------------------------------
# BOOKS PAGE
# ---------------------------------------------------------
elif page == "Books":
    st.markdown("<div class='section-title'>📚 AI & Robotics Books</div>", unsafe_allow_html=True)
    st.write("Upgrade your braincells, king 😎📖")

    books = [
    {
        "title": "Humanoid Robotics Fundamentals",
        "image": "https://your_custom_url/cover_humanoid.png",  # custom AI-generated cover
        "desc": "Motors, actuators, sensors & control — full humanoid guide.",
    },
    {
        "title": "Physical AI – Machines That Move",
        "image": "https://your_custom_url/cover_physical_ai.png",
        "desc": "AI + physics + robotics + bio-inspired movement.",
    },
    {
        "title": "Artificial Intelligence: Modern Approach",
        "image": "https://your_custom_url/cover_ai_modern.png",
        "desc": "The world's most popular AI textbook.",
    },
    {
        "title": "Robotics: Sensing & Automation",
        "image": "https://your_custom_url/cover_robotics.png",
        "desc": "Industrial robotics, control systems, and automation.",
    }
]

    cols = st.columns(2)
    for i, book in enumerate(books):
        with cols[i % 2]:
            st.markdown(f"""
            <div class='card'>
                <img src="{book['image']}" width="180" style="border-radius:10px;">
                <h3>{book['title']}</h3>
                <p>{book['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------------
# REGISTRATION PAGE
# ---------------------------------------------------------
elif page == "Register":
    st.markdown("<div class='section-title'>📝 Registration Form</div>", unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")

    course = st.selectbox(
        "Select Program",
        ["Humanoid Robotics", "Physical AI", "Hackathon 2024", "Sensors & AI", "ML for Robots"]
    )

    exp = st.slider("Skill Level (0 = Beginner, 10 = Expert)", 0, 10)

    if st.button("Register Now"):
        if name == "" or email == "" or phone == "":
            st.error("Bruh… fill the required fields 😭")
        else:
            new_entry = pd.DataFrame(
                [[name, email, course, phone, exp]],
                columns=["Name", "Email", "Course", "Phone", "Experience"]
            )

            df = pd.read_csv(DATA_FILE)
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)

            st.success(f"🔥 Registered Successfully! Welcome, {name}.")

# ---------------------------------------------------------
# ADMIN PANEL
# ---------------------------------------------------------
elif page == "Admin":
    st.markdown("<div class='section-title'>🔐 Admin Panel</div>", unsafe_allow_html=True)

    password = st.text_input("Enter admin password:", type="password")

    if password == "admin123":
        st.success("Admin Access Granted ✔")

        df = pd.read_csv(DATA_FILE)
        st.dataframe(df)

        if st.button("Clear All Records"):
            df = pd.DataFrame(columns=["Name", "Email", "Course", "Phone", "Experience"])
            df.to_csv(DATA_FILE, index=False)
            st.warning("All registration records cleared ⚠️")
    else:
        st.info("Enter password to view registrations.")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class='footer'>
© 2024 RoboHack Academy — Building Future Innovators
</div>
""", unsafe_allow_html=True)
