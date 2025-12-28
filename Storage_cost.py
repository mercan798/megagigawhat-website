import streamlit as st
from static.css.streamlit_style import CUSTOM_CSS
from static.html.footer import get_footer_html

st.set_page_config(
    page_title="Storage Cost Calculator - Mega Giga What?",
    layout="wide"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("Storage Cost Calculator")
st.markdown('<p class="subtitle">Estimate your cloud storage costs</p>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    data_tb_cost = st.number_input(
        "Data Amount (TB)",
        min_value=0.0,
        value=1.0,
        step=0.1,
        format="%.2f",
        key="tb_cost",
        help="Enter the amount of data you want to store in Terabytes"
    )

with col2:
    months = st.number_input(
        "Duration (Months)",
        min_value=0.0,
        value=12.0,
        step=0.1,
        format="%.1f",
        help="Enter the number of months you'll store the data"
    )

if st.button("Calculate Storage Cost", type="primary", use_container_width=True):
    if data_tb_cost <= 0 or months <= 0:
        st.error("Please enter valid positive numbers")
    else:
        TB_TO_GB = 1024
        price_per_gb_month = 0.023
        gb = data_tb_cost * TB_TO_GB
        total_cost = (gb * price_per_gb_month) * months
        
        monthly_cost = total_cost / months if months > 0 else 0
        yearly_cost = monthly_cost * 12
        
        st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #667eea; margin-bottom: 0.75rem;">Storage Cost Result</h3>
            <p>Storing <strong>{data_tb_cost:.2f} TB</strong> for <strong>{months:.2f} months</strong>:</p>
            <p style="font-weight: 700; color: #4c51bf; font-size: 1.4rem; margin-top: 1rem;">
                ${total_cost:,.2f} USD
            </p>
            <hr style="margin: 1rem 0; border-color: #e2e8f0;">
            <p style="font-size: 0.95rem; color: #718096;">
                <strong>Monthly cost:</strong> ${monthly_cost:,.2f} USD<br>
                <strong>Projected yearly cost:</strong> ${yearly_cost:,.2f} USD
            </p>
            <p style="font-size: 0.9rem; margin-top: 1rem; color: #718096;">
                <em>(Based on AWS S3 Standard @ $0.023/GB-month)</em>
            </p>
        </div>
        """, unsafe_allow_html=True)


st.markdown("## Pricing Details")

st.markdown("""
<div class="info-card">
    <h4>AWS S3 Standard Storage Pricing</h4>
    <p>Our calculator uses <strong>$0.023 per GB-month</strong> which is the current AWS S3 Standard storage pricing 
    for the first 50 TB of storage.</p>
    
    <h5 style="margin-top: 1rem;">Pricing Tiers (AWS S3 Standard):</h5>
    <ul>
        <li>First 50 TB: $0.023 per GB-month</li>
        <li>Next 450 TB: $0.022 per GB-month</li>
        <li>Over 500 TB: $0.021 per GB-month</li>
    </ul>
    
    <p style="margin-top: 1rem; color: #718096; font-size: 0.9rem;">
        <em>Note: Prices may vary by region and are subject to change. Always check AWS pricing page for the most current rates.</em>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Cost Optimization Tips")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h4>Save Money</h4>
        <ul>
            <li>Use S3 Glacier for archival data (90% cheaper)</li>
            <li>Enable S3 Intelligent-Tiering for automatic cost optimization</li>
            <li>Delete unnecessary data and old versions</li>
            <li>Compress data before uploading</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h4>Storage Classes</h4>
        <ul>
            <li><strong>S3 Standard:</strong> Frequently accessed data</li>
            <li><strong>S3 IA:</strong> Infrequently accessed (50% cheaper)</li>
            <li><strong>S3 Glacier:</strong> Archive (90% cheaper)</li>
            <li><strong>S3 Deep Archive:</strong> Long-term (95% cheaper)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown(get_footer_html(), unsafe_allow_html=True)
