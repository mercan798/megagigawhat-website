import streamlit as st
from static.css.streamlit_style import CUSTOM_CSS
from static.html.footer import get_footer_html

st.set_page_config(
    page_title="Transfer Time Calculator - Mega Giga What?",
    page_icon="⏱",
    layout="wide"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("Transfer Time Calculator")
st.markdown('<p class="subtitle">Calculate how long your data transfer will take</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    data_tb = st.number_input(
        "Data Amount (TB)",
        min_value=0.0,
        value=1.0,
        step=0.1,
        format="%.2f",
        help="Enter the total amount of data you want to transfer in Terabytes"
    )

with col2:
    link_mbit = st.number_input(
        "Link Speed (Mbit/s)",
        min_value=1.0,
        value=100.0,
        step=1.0,
        format="%.0f",
        help="Enter your network connection speed in Megabits per second"
    )

if st.button("Calculate Transfer Time", type="primary", use_container_width=True):
    if data_tb <= 0 or link_mbit <= 0:
        st.error("Please enter valid positive numbers")
    else:
      
        bit_cal = data_tb * (8 * 1024**4)
        band_width = link_mbit * 1_000_000
        sec = bit_cal / band_width
        real_sec = int(sec)
        
        day = real_sec // 86400
        rem = real_sec % 86400
        hour = rem // 3600
        rem %= 3600
        minute = rem // 60
        seconds = rem % 60
        
        st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #667eea; margin-bottom: 0.75rem;">Transfer Time Result</h3>
            <p>Transferring <strong>{data_tb:.2f} TB</strong> at <strong>{link_mbit:.0f} Mbit/s</strong> will take:</p>
            <p style="font-weight: 700; color: #4c51bf; font-size: 1.4rem; margin-top: 1rem;">
                {day} days, {hour} hours, {minute} minutes, {seconds} seconds
            </p>
        </div>
        """, unsafe_allow_html=True)


st.markdown("## How It Works")

st.markdown("""
<div class="info-card">
    <h4>Calculation Formula</h4>
    <p>We use the following formula to calculate transfer time:</p>
    <ol>
        <li>Convert TB to bits: <code>bits = TB × 8 × 1024⁴</code></li>
        <li>Convert Mbit/s to bits/s: <code>bandwidth = Mbit/s × 1,000,000</code></li>
        <li>Calculate time: <code>seconds = bits ÷ bandwidth</code></li>
        <li>Convert to days, hours, minutes, and seconds</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("## Tips")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h4>Real-World Factors</h4>
        <ul>
            <li>Network overhead typically reduces effective speed by 5-10%</li>
            <li>Protocol overhead (TCP/IP) adds additional time</li>
            <li>Distance and routing can affect transfer speeds</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h4>Common Speeds</h4>
        <ul>
            <li>Fast Ethernet: 100 Mbit/s</li>
            <li>Gigabit Ethernet: 1000 Mbit/s</li>
            <li>10G Ethernet: 10000 Mbit/s</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown(get_footer_html(), unsafe_allow_html=True)
