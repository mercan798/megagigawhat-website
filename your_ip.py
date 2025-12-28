import streamlit as st
import requests
from static.css.streamlit_style import CUSTOM_CSS
from static.html.footer import get_footer_html

st.set_page_config(
    page_title="IP Information - Mega Giga What?",
    page_icon="🌐",
    layout="wide"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("Your IP Information")
st.markdown('<p class="subtitle">Check your current IP address</p>', unsafe_allow_html=True)


try:
    response = requests.get("https://megagigawhat.com/myapi", timeout=5)
    if response.status_code == 200:
        data = response.json()
        ip_address = data.get("ip", "unavailable")
        message = data.get("message", "")
        
        if ip_address == "unavailable":
            st.markdown(f"""
            <div class="info-card">
                <h3>IP Address Detection</h3>
                <p style="margin-top: 1rem; color: #718096;">
                    {message}
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="info-card">
                <h3>Your IP Address</h3>
                <div class="ip-badge">{ip_address}</div>
                <p style="margin-top: 1rem; color: #718096;">
                    This is your public IP address as detected from your connection.
                </p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Could not retrieve IP information at this time.")
except Exception as e:
    st.warning(f"Unable to connect to IP detection service: {str(e)}")


st.markdown("## API Documentation")

st.markdown("""
<div class="info-card">
    <h4>GET /myapi</h4>
    <p>Returns your current IP address as detected by our server.</p>
    
    <h5 style="margin-top: 1rem;">Response Format:</h5>
    <pre style="background: #2d3748; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow-x: auto;">
{
    "ip": "xxx.xxx.xxx.xxx"
}
    </pre>
    
    <h5 style="margin-top: 1rem;">Example Usage:</h5>
    <pre style="background: #2d3748; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow-x: auto;">
curl https://megagigawhat.com/myapi
    </pre>
</div>
""", unsafe_allow_html=True)

st.markdown("## Privacy Note")
st.info("We do not store or log your IP address. This information is generated in real-time and discarded immediately after the response.")

st.markdown(get_footer_html(), unsafe_allow_html=True)
