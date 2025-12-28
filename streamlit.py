import streamlit as st
from static.css.streamlit_style import CUSTOM_CSS
from static.html.footer import get_footer_html

st.set_page_config(
    page_title="Mega Giga What?",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


st.title("Mega Giga What?")
st.markdown('<p class="subtitle">Cloud cost & transfer calculators for big data</p>', unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="info-card">
    <h2 style="color: #667eea; margin-bottom: 1rem;">Welcome to Mega Giga What?</h2>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        Your one-stop solution for calculating data transfer times and cloud storage costs. 
        Whether you're planning a massive data migration or estimating your cloud budget, 
        we've got you covered with accurate, easy-to-use calculators.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("## Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>Transfer Time Calculator</h3>
        <p>Calculate how long it takes to transfer large amounts of data over your network connection. 
        Perfect for planning migrations, backups, and data transfers.</p>
        <ul>
            <li>Support for TB-scale calculations</li>
            <li>Accurate bit-level precision</li>
            <li>Real-world network speed conversion</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>Storage Cost Calculator</h3>
        <p>Estimate your cloud storage costs based on AWS S3 pricing. 
        Plan your budget and optimize your storage strategy.</p>
        <ul>
            <li>Based on AWS S3 Standard pricing</li>
            <li>Multi-month cost projections</li>
            <li>Transparent pricing breakdown</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


st.markdown("## Quick Start")
st.info("Use the sidebar navigation to access different calculators and pages. Start with the **Transfer Time** or **Storage Cost** calculators!")

st.markdown("## How It Works")

st.markdown("""
<div class="info-card">
    <h4>Transfer Time Calculation</h4>
    <p>We convert your data amount (TB) to bits and divide by your network bandwidth (Mbit/s) to give you an accurate time estimate in days, hours, minutes, and seconds.</p>
    
    <h4 style="margin-top: 1.5rem;">Storage Cost Calculation</h4>
    <p>Based on current AWS S3 Standard pricing ($0.023 per GB-month), we calculate the total cost for storing your data over your specified duration.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Why Choose Us?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h2 style="color: #667eea; font-size: 2.5rem;">100%</h2>
        <p style="color: #718096;">Free to Use</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h2 style="color: #667eea; font-size: 2.5rem;">Fast</h2>
        <p style="color: #718096;">Instant Results</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h2 style="color: #667eea; font-size: 2.5rem;">Safe</h2>
        <p style="color: #718096;">No Data Stored</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown(get_footer_html(), unsafe_allow_html=True)
