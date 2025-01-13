import streamlit as st
import requests
import uuid

# Azure credentials (for translation only)
AZURE_KEY = "9CTd2qVrUkZkvTC9AB44vqrsSYFponfJm8Fi6KCZCxoZuuOK96KBJQQJ99BAACYeBjFXJ3w3AAAEACOGH83l"
ENDPOINT = "https://api.cognitive.microsofttranslator.com"
LOCATION = "eastus"

# Expanded language list with Indian languages
LANGUAGES = {
    'Arabic': 'ar',
    'Bengali': 'bn',
    'Chinese (Simplified)': 'zh-Hans',
    'English': 'en',
    'French': 'fr',
    'German': 'de',
    'Gujarati': 'gu',
    'Hindi': 'hi',
    'Italian': 'it',
    'Japanese': 'ja',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Nepali': 'ne',
    'Odia': 'or',
    'Punjabi': 'pa',
    'Russian': 'ru',
    'Sanskrit': 'sa',
    'Spanish': 'es',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Urdu': 'ur',
    'Vietnamese': 'vi'
}

def translate_text(text, from_lang, to_lang):
    """Translate text using Azure Translator REST API."""
    try:
        path = '/translate'
        constructed_url = ENDPOINT + path

        params = {
            'api-version': '3.0',
            'from': from_lang,
            'to': to_lang
        }

        headers = {
            'Ocp-Apim-Subscription-Key': AZURE_KEY,
            'Ocp-Apim-Subscription-Region': LOCATION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': text
        }]

        response = requests.post(constructed_url, params=params, headers=headers, json=body)
        response.raise_for_status()

        translation = response.json()[0]["translations"][0]["text"]
        return translation

    except Exception as e:
        st.error(f"Translation Error: {str(e)}")
        return ""

# Streamlit UI
st.set_page_config(
    page_title="Universal Translator",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS with animations and modern design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    
    .stApp {
        max-width: 1400px;
        margin: 0 auto;
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg,rgb(150, 0, 0) 0%, #e4e8eb 100%);
    }
    
    .title-container {
        background: linear-gradient(120deg, #2E3192 0%, #1BFFFF 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .language-selector {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
        margin-bottom: 2rem;
        transition: transform 0.3s ease;
    }
    
    .language-selector:hover {
        transform: translateY(-5px);
    }
    
    .stSelectbox > div > div {
        background: #f8f9fa;
        padding: 8px;
        border-radius: 10px;
        border: 2px solid #e9ecef;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #2E3192;
    }
    
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #e9ecef;
        padding: 15px;
        font-size: 16px;
        transition: all 0.3s ease;
        background: white;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        height: 300px !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #2E3192;
        box-shadow: 0 0 15px rgba(46, 49, 146, 0.1);
    }
    
    .stButton > button {
        background: linear-gradient(120deg, #2E3192 0%, #1BFFFF 100%);
        color: white;
        padding: 12px 35px;
        border-radius: 30px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(46, 49, 146, 0.2);
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(46, 49, 146, 0.3);
    }
    
    .translator-box {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        margin-bottom: 2rem;
    }
    
    .subheader {
        color: #2E3192;
        font-weight: 600;
        margin-bottom: 1rem;
        font-size: 1.2rem;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        background: white;
        border-radius: 15px;
        margin-top: 2rem;
        box-shadow: 0 -5px 20px rgba(0, 0, 0, 0.05);
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 1.5rem;
    }
    
    .social-links a {
        color: #2E3192;
        text-decoration: none;
        transition: all 0.3s ease;
        font-size: 1.1rem;
    }
    
    .social-links a:hover {
        color: #1BFFFF;
        transform: translateY(-3px);
    }
    
    /* Loading animation */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .loading {
        animation: pulse 1s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# Enhanced Title Section
st.markdown("""
    <div class="title-container">
        <h1 style="color: white; font-size: 3rem; font-weight: 700; margin-bottom: 1rem;">🌏 Universal Language Translator</h1>
        <p style="color: white; font-size: 1.2rem; opacity: 0.9;">Breaking Language Barriers | Connecting Cultures</p>
    </div>
""", unsafe_allow_html=True)

# Language Selection
st.markdown('<div class="language-selector">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<p class="subheader">Source Language</p>', unsafe_allow_html=True)
    from_lang = st.selectbox("", 
                            list(LANGUAGES.keys()), 
                            index=list(LANGUAGES.keys()).index('English'))

with col2:
    st.markdown('<p class="subheader">Target Language</p>', unsafe_allow_html=True)
    to_lang = st.selectbox("", 
                          list(LANGUAGES.keys()), 
                          index=list(LANGUAGES.keys()).index('Hindi'))
st.markdown('</div>', unsafe_allow_html=True)

# Translation Section with side-by-side layout
st.markdown('<div class="translator-box">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="subheader">📝 Input Text</p>', unsafe_allow_html=True)
    input_text = st.text_area("", height=300, 
                             placeholder="Type or paste your text here...")

with col2:
    st.markdown('<p class="subheader">✨ Translation</p>', unsafe_allow_html=True)
    if 'translated_text' not in st.session_state:
        st.session_state.translated_text = ""
    
    translated_display = st.text_area("", value=st.session_state.translated_text, height=300,
                                    placeholder="Your translation will appear here...")

# Centered Translate Button
col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button("🔄 Translate Now"):
        if input_text:
            with st.spinner("🔄 Magic in progress..."):
                st.session_state.translated_text = translate_text(
                    input_text,
                    LANGUAGES[from_lang],
                    LANGUAGES[to_lang]
                )
                st.rerun()

# Enhanced Footer with Social Media Links
st.markdown("""
    <div class="footer">
        <h3 style="color: #2E3192; margin-bottom: 1rem;">🌟 Features</h3>
        <p style="color: #666; margin-bottom: 0.5rem;">✓ Support for 25+ Global Languages</p>
        <p style="color: #666; margin-bottom: 0.5rem;">✓ Real-time Translation</p>
        <p style="color: #666; margin-bottom: 0.5rem;">✓ Powered by Azure AI Services</p>
        <div class="social-links">
            <a href="https://instagram.com/yourusername" target="_blank">📸 Instagram</a>
            <a href="www.linkedin.com/in/ashwin-dahake-26158b1b5" target="_blank">💼 LinkedIn</a>
            <a href="https://www.instagram.com/ashwin_dahake_?igsh=MTd5dDMzOTIxc2M3ZA==" target="_blank">👨‍💻 GitHub</a>
        </div>
        <p style="color: #666; font-size: 0.8rem; margin-top: 2rem;">Made with ❤️ by Ashwin</p>
    </div>
    """, unsafe_allow_html=True)
