# megagigawhat-website

# Mega Giga What?

Cloud cost & transfer calculators for big data professionals.

## Overview

Mega Giga What? is a web application that helps you calculate data transfer times and estimate cloud storage costs. Built with Streamlit and FastAPI, it provides accurate calculations for planning migrations, backups, and cloud budgets.

 **Live Demo**: [https://megagigawhat.com](https://megagigawhat.com)

## Features

- **Transfer Time Calculator**: Calculate how long it takes to transfer large amounts of data
- **Storage Cost Calculator**: Estimate cloud storage costs based on AWS S3 pricing
- **IP Detection API**: Get your public IP address via simple API endpoint
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Nature-Themed UI**: Beautiful forest background with glassmorphism effects

## Tech Stack

- **Frontend**: Streamlit 1.52.2
- **Backend**: FastAPI
- **Web Server**: Nginx with SSL (Let's Encrypt)
- **Server**: Uvicorn ASGI
- **Deployment**: systemd services on Ubuntu
- **Python**: 3.10

## Installation

### Prerequisites

- Python 3.10+
- pip
- nginx (for production)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mega-giga-what.git
cd mega-giga-what
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
```bash
# Start FastAPI backend
python app.py

# In another terminal, start Streamlit
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```

4. Access the app:
- Open your browser to `http://localhost:7860`

## Project Structure

```
mega_giga_what/
├── app.py                 # FastAPI backend
├── streamlit_app.py       # Main Streamlit landing page
├── config.py             # Configuration (AdSense, etc.)
├── pages/                # Streamlit multi-page app
│   ├── 1_Your_API.py
│   ├── 2_Transfer_Time.py
│   ├── 3_Storage_Cost.py
│   ├── 4_Privacy_Policy.py
│   ├── 5_Terms.py
│   ├── 6_Contact.py
│   ├── 7_About.py
│   └── 8_Blog.py
├── static/
│   ├── css/
│   │   └── streamlit_style.py
│   └── html/
│       └── footer.py
├── templates/
│   └── page_template.html
├── *.md                  # Markdown content files
└── README.md
```

## API Endpoints

### GET /myapi
Returns your public IP address.

**Response:**
```json
{
  "ip": "xxx.xxx.xxx.xxx"
}
```

**Example:**
```bash
curl https://megagigawhat.com/myapi
```

### GET /contact, /blog, /privacy, /terms
Returns rendered markdown pages.

## Deployment

### Production Setup with systemd

1. Create FastAPI service:
```bash
sudo nano /etc/systemd/system/megagigawhat.service
```

2. Create Streamlit service:
```bash
sudo nano /etc/systemd/system/streamlit.service
```

3. Enable and start services:
```bash
sudo systemctl enable megagigawhat.service
sudo systemctl enable streamlit.service
sudo systemctl start megagigawhat.service
sudo systemctl start streamlit.service
```

### Nginx Configuration

Configure Nginx to reverse proxy to FastAPI (port 7860), which serves an iframe embedding Streamlit (port 8501).

## Configuration

Edit `config.py` to configure:
- Google AdSense credentials
- Other application settings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Developed and maintained by **Mercan Olcek**

- Email: MegaGigaWhat@gmail.com
- Website: [megagigawhat.com](https://megagigawhat.com)

## Acknowledgments

- Background image from [Unsplash](https://unsplash.com)
- Built with [Streamlit](https://streamlit.io)
- Powered by [FastAPI](https://fastapi.tiangolo.com)

---

**Happy calculating!** 🚀
