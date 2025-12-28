import streamlit as st
from pathlib import Path
import markdown as md
from static.css.streamlit_style import CUSTOM_CSS
from static.html.footer import get_footer_html

st.set_page_config(
    page_title="Terms of Service - Mega Giga What?",
    page_icon="📜",
    layout="wide"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("Terms of Service")


terms_file = Path("/opt/mega_giga_what/terms_of_service.md")
if terms_file.exists():
    content = terms_file.read_text(encoding="utf-8")
    html_content = md.markdown(content, extensions=["fenced_code", "tables"])
    st.markdown(html_content, unsafe_allow_html=True)
else:
    st.error("Terms of service file not found")

st.markdown(get_footer_html(), unsafe_allow_html=True)
