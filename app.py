
import streamlit as st
from PIL import Image
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="truVox | Crime Investigation",
    page_icon="🔴",
    layout="wide"
)

# Dark red and black theme
st.markdown("""
<style>
.stApp {
    background-color: #080808;
    color: white;
}
h1, h2, h3 {
    color: #e50914;
}
p, label {
    color: #dddddd;
}
.stButton > button {
    background-color: #a00000;
    color: white;
    border: 1px solid #ff2020;
    border-radius: 8px;
}
.stButton > button:hover {
    background-color: #e50914;
    color: white;
}
section[data-testid="stSidebar"] {
    background-color: #130808;
}
div[data-testid="stFileUploader"] {
    background-color: #151515;
    border: 1px solid #8b0000;
    border-radius: 10px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

# Header
# Official truVox Logo
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "truvox_logo.png")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(LOGO_PATH, width=400)

# Sidebar
st.sidebar.title("🔎 INVESTIGATION")
page = st.sidebar.radio(
    "Select Investigation",
    ["Dashboard", "Image Investigation", "Text Investigation"]
)

# Dashboard
if page == "Dashboard":
    st.title("Investigation Dashboard")
    st.write("Welcome to the truVox Crime Investigation System.")

    col1, col2, col3 = st.columns(3)

    col1.metric("SYSTEM", "ONLINE")
    col2.metric("MODULES", "03")
    col3.metric("STATUS", "READY")

    st.subheader("Investigation Center")
    st.write("Select an investigation module from the left sidebar.")

    st.info("Upload evidence to begin your investigation.")

# Image Investigation
elif page == "Image Investigation":
    st.title("🖼️ Image Investigation")
    st.write("Upload an image as digital evidence.")

    image_file = st.file_uploader(
        "Upload Evidence Image",
        type=["png", "jpg", "jpeg"]
    )

    if image_file:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Evidence", width=500)
        st.success("Image uploaded successfully.")

# Text Investigation
elif page == "Text Investigation":
    st.title("📄 Text Investigation")
    st.write("Upload a text file or enter evidence manually.")

    text_file = st.file_uploader(
        "Upload Text Evidence",
        type=["txt"]
    )

    evidence_text = st.text_area(
        "Enter Investigation Text",
        height=200,
        placeholder="Enter the evidence text here..."
    )

    if text_file:
        evidence_text = text_file.getvalue().decode(
            "utf-8", errors="replace"
        )
        st.text_area(
            "Uploaded Evidence Content",
            value=evidence_text,
            height=200
        )

    if st.button("SUBMIT EVIDENCE"):
        if evidence_text.strip():
            st.success("Evidence received successfully!")
        else:
            st.warning("Please enter or upload evidence.")

st.divider()

st.markdown(
    "<p style='text-align:center;color:#777;'>truVox © 2026 | DIGITAL INVESTIGATION SYSTEM</p>",
    unsafe_allow_html=True
)
