import streamlit as st
from pathlib import Path
import markdown as md
from static.css.streamlit_style import CUSTOM_CSS
from static.html.footer import get_footer_html

st.set_page_config(
    page_title="Contact - Mega Giga What?",
    page_icon="📧",
    layout="wide"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("Contact Us")

contact_file = Path("/opt/mega_giga_what/contact.md")
if contact_file.exists():
    content = contact_file.read_text(encoding="utf-8")
    html_content = md.markdown(content, extensions=["fenced_code", "tables"])
    st.markdown(html_content, unsafe_allow_html=True)
else:
    st.error("Contact file not found")

st.markdown(get_footer_html(), unsafe_allow_html=True)
