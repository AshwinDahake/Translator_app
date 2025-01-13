🌏 Universal Language Translator
Breaking Language Barriers | Connecting Cultures

Overview
Universal Language Translator is a web application built using Streamlit and powered by Microsoft Azure Cognitive Services. It allows real-time text translation between 25+ global languages, including Indian languages, with a user-friendly interface and visually appealing design.

Features
🌐 Support for 25+ Global Languages: Translate text between popular languages, including Hindi, Marathi, Tamil, Kannada, Chinese, Arabic, and more.
⏱️ Real-time Translation: Instantly translate text with the power of Azure Translator API.
🎨 Modern UI/UX: Sleek design with smooth animations for an enhanced user experience.
🛠️ Customizable: Easily expandable to support additional languages or features.
🔒 Secure: Built with Azure API keys for safe and secure communication.
Tech Stack
Streamlit: For building the user interface.
Microsoft Azure Cognitive Services: For translation capabilities.
Python: The backbone of the application.
Languages Supported
The app supports the following languages:

Arabic, Bengali, Chinese (Simplified), English, French, German, Gujarati, Hindi, Italian, Japanese, Kannada, Korean, Malayalam, Marathi, Nepali, Odia, Punjabi, Russian, Sanskrit, Spanish, Tamil, Telugu, Thai, Urdu, Vietnamese.
Prerequisites
Before running this project, ensure you have:

Python 3.7 or higher installed.
A Microsoft Azure subscription with Translator API access.
Azure Translator API credentials: AZURE_KEY, ENDPOINT, and LOCATION.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/universal-language-translator.git
cd universal-language-translator
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set Azure credentials: Replace the placeholders in the AZURE_KEY, ENDPOINT, and LOCATION variables in the script with your Azure Translator API details.

Run the application:

bash
Copy code
streamlit run app.py
Open the app in your browser at http://localhost:8501.

How to Use
Select the Source Language and Target Language from the dropdown menus.
Enter the text you want to translate in the Input Text area.
Click the Translate Now button.
View the translated text in the Translation box.
	
Input and Translation Area	
Customization
To add more languages, update the LANGUAGES dictionary in the script with the new language name and its ISO code.
Modify the UI styles in the Custom CSS section for a personalized look.
Contributing
We welcome contributions to make this project even better! 🎉

Fork the repository.
Create a new branch for your feature/bugfix.
Submit a pull request with detailed information.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any queries, feedback, or collaboration opportunities:

Instagram: yourusername
LinkedIn: Ashwin Dahake
GitHub: Ashwin Dahake
