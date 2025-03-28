# MalCare - AI-Powered Health & Fitness Assistant

Welcome to **MalCare**, an intelligent non-invasive malaria treatment  health application powered by AI. Designed to assist users in maintaining a healthy lifestyle, MalCare leverages **GPT-4o, Chat Avatars, and GitHub Copilot** to offer personalized fitness and nutrition recommendations.

[Try now](https://jerryblessed.pythonanywhere.com/fitness/)

## Features

- **AI-Powered Health Insights**: Get personalized health advice based on user data, powered by **GPT-4o**.
- **Chat Avatars for Interaction**: Engage with an AI-driven assistant that provides fitness coaching and dietary suggestions.
- **Activity and Diet Tracker**: Monitor daily activities, workouts, calorie intake, and nutritional values.
- **Automated Goal Setting**: AI analyzes progress and suggests fitness goals.
- **Secure User Authentication**: Ensuring user data privacy with secure login and authentication mechanisms.
- **Code Assistance with GitHub Copilot**: Streamlined development process with AI-generated code suggestions for optimized performance.

## Technologies Used

- **Backend**: Django (Python) for secure and scalable architecture.
- **Frontend**: HTML, CSS, JavaScript for a responsive interface.
- **Database**: Azure PostgreSQL- flexible server for efficient data storage and retrieval.
- **AI & Cloud Services**:
  - **Azure GPT-4o** for AI-driven insights.
  - **Azure Chat Avatars** for interactive guidance.
  - **GitHub Copilot** for automated coding assistance.

## Getting Started

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/jerryblessed/malcare.git
   ```

2. **Set Up a Virtual Environment**:

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use env\Scripts\activate
   ```

3. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**:

   ```sh
   python manage.py runserver
   ```
5. **Deployment of Azure**:

   ```sh
   deploy on azure after replacement of settings.py with azure_settings.txt then configure the .env file
   ```
## Contribution

This project utilizes **GitHub Copilot** for optimized coding practices. Contributions are welcome to enhance security, AI features, and user experience. Note that ```.env``` file was left in main directory for testing purposes thank you. 

## License

This project is licensed under the MIT License.

---

Stay fit and secure with **MalCare!** 🚀

