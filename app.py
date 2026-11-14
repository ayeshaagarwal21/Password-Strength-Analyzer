
import streamlit as st

from modules.password_analyzer import analyze_password

from modules.hash_generator import (
    generate_md5,
    generate_sha1,
    generate_bcrypt,
    verify_bcrypt
)

from modules.dictionary_attack import dictionary_attack
from modules.brute_force import brute_force_attack


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🔐",
    layout="wide"
)


# CUSTOM CSS

# CUSTOM CSS

st.markdown("""
<style>

/* Main application */
.stApp {
    background-color: #F4F7FC;
    color: #172B4D;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #EAF0F8;
    border-right: 1px solid #D5DFEC;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #172B4D;
}

/* Headings */
h1, h2, h3 {
    color: #1E3A8A !important;
    font-weight: 700;
}

/* Paragraphs */
p, label {
    color: #334155;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #DCE5F1;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(30, 58, 138, 0.05);
}

/* Buttons */
.stButton > button {
    background-color: #2563EB;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1E40AF;
    color: #FFFFFF;
    border: none;
}

/* Input fields */
.stTextInput input {
    background-color: #FFFFFF;
    color: #172B4D;
    border-radius: 8px;
    border: 1px solid #CBD5E1;
}

/* Select boxes */
.stSelectbox [data-baseweb="select"] {
    background-color: #FFFFFF;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Dividers */
hr {
    border-color: #DCE5F1;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR
st.sidebar.title("🔐 Password Analyzer")
st.sidebar.caption("Cyber Security Lab | CSL-G13")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Password Analyzer",
        "Hash Generator",
        "Dictionary Attack",
        "Brute Force"
    ]
)

st.sidebar.divider()
st.sidebar.caption("SKIT Jaipur | Session 2026-27")


# HOME
if page == "Home":

    st.title("🔐 Password Strength Analyzer")

    st.subheader(
        "Dictionary & Brute Force Attack Simulator"
    )

    st.write("""
    An educational cybersecurity application that
    evaluates password strength and demonstrates
    password-guessing techniques using dummy data.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.info("### Password Analysis")
        st.write("""
        - Entropy calculation
        - Pattern detection
        - Password strength scoring
        """)

    with col2:
        st.info("### Attack Simulation")
        st.write("""
        - MD5, SHA-1 and bcrypt
        - Dictionary attack
        - Bounded brute-force demonstration
        """)

    st.success(
        "Select a module from the sidebar to begin."
    )


# PASSWORD ANALYZER
elif page == "Password Analyzer":

    st.title("Password Strength Analyzer")

    password = st.text_input(
        "Enter a dummy test password",
        type="password"
    )

    if st.button("Analyze Password"):

        if password:

            result = analyze_password(password)

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Strength Score",
                f"{result['score']}/100"
            )

            col2.metric(
                "Strength",
                result["strength"]
            )

            col3.metric(
                "Entropy",
                f"{result['entropy']} bits"
            )

            st.subheader("Password Strength")
            st.progress(result["score"] / 100)

            st.subheader("Detected Patterns")

            if result["patterns"]:
                for pattern in result["patterns"]:
                    st.warning(pattern)
            else:
                st.success("No implemented patterns detected.")

            st.caption(
                "This is an educational scoring model."
            )

        else:
            st.warning("Please enter a test password.")


# HASH GENERATOR
elif page == "Hash Generator":

    st.title("Hash Generator")

    password = st.text_input(
        "Enter a dummy test password",
        type="password",
        key="hash_input"
    )

    algorithm = st.selectbox(
        "Select Algorithm",
        ["MD5", "SHA-1", "bcrypt"]
    )

    if st.button("Generate Hash"):

        if password:

            if algorithm == "MD5":
                hashed = generate_md5(password)

            elif algorithm == "SHA-1":
                hashed = generate_sha1(password)

            else:
                hashed = generate_bcrypt(password)

            st.success(f"{algorithm} hash generated")

            st.code(hashed)

            if algorithm == "bcrypt":

                st.subheader("Password Verification")

                st.write(
                    "Correct password:",
                    verify_bcrypt(password, hashed)
                )

                st.write(
                    "Wrong password:",
                    verify_bcrypt("wrong123", hashed)
                )

        else:
            st.warning("Enter a test password.")


# DICTIONARY ATTACK
elif page == "Dictionary Attack":

    st.title("Dictionary Attack Simulator")

    st.warning(
        "Only use locally generated hashes and dummy passwords."
    )

    password = st.text_input(
        "Enter a dummy target password",
        type="password",
        key="dictionary_password"
    )

    algorithm = st.selectbox(
        "Select Hash Algorithm",
        ["MD5", "SHA-1", "bcrypt"],
        key="dictionary_algorithm"
    )

    if st.button("Run Dictionary Attack"):

        if not password:
            st.warning("Enter a test password.")

        else:

            if algorithm == "MD5":
                target_hash = generate_md5(password)
                algo = "md5"

            elif algorithm == "SHA-1":
                target_hash = generate_sha1(password)
                algo = "sha1"

            else:
                target_hash = generate_bcrypt(password)
                algo = "bcrypt"

            try:

                result = dictionary_attack(
                    target_hash,
                    algo,
                    "dataset/passwords.txt"
                )

                st.subheader("Attack Results")

                col1, col2 = st.columns(2)

                col1.metric(
                    "Attempts",
                    result["attempts"]
                )

                col2.metric(
                    "Execution Time",
                    f"{result['time_taken']} sec"
                )

                if result["found"]:
                    st.success(
                        f"Test password found: {result['password']}"
                    )
                else:
                    st.error(
                        "Password not found in dictionary."
                    )

            except FileNotFoundError as error:
                st.error(str(error))


# BRUTE FORCE
elif page == "Brute Force":

    st.title("Brute Force Demonstration")

    st.warning(
        "This demonstration uses a limited local search space."
    )

    password = st.text_input(
        "Enter a dummy target password",
        type="password",
        key="brute_password"
    )

    algorithm = st.selectbox(
        "Select Hash Algorithm",
        ["MD5", "SHA-1", "bcrypt"],
        key="brute_algorithm"
    )

    charset = st.text_input(
        "Character Set",
        value="ab12"
    )

    max_length = st.slider(
        "Maximum Password Length",
        1, 4, 2
    )

    max_attempts = st.number_input(
        "Maximum Attempts",
        min_value=1,
        max_value=1000,
        value=1000
    )

    if st.button("Run Brute Force"):

        if not password or not charset:
            st.warning("Enter all required values.")

        elif len(set(charset)) != len(charset):
            st.warning("Character set must contain unique characters.")

        else:

            if algorithm == "MD5":
                target_hash = generate_md5(password)
                algo = "md5"

            elif algorithm == "SHA-1":
                target_hash = generate_sha1(password)
                algo = "sha1"

            else:
                target_hash = generate_bcrypt(password)
                algo = "bcrypt"

            try:

                result = brute_force_attack(
                    target_hash,
                    algo,
                    charset,
                    max_length,
                    int(max_attempts)
                )

                st.subheader("Attack Results")

                col1, col2 = st.columns(2)

                col1.metric(
                    "Attempts",
                    result["attempts"]
                )

                col2.metric(
                    "Execution Time",
                    f"{result['time_taken']} sec"
                )

                if result["found"]:
                    st.success(
                        f"Test password found: {result['password']}"
                    )
                else:
                    st.error(
                        "Password not found within the search limit."
                    )

            except Exception as error:
                st.error(str(error))
