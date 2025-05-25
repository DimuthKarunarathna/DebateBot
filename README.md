# 🧠 DebateBot

DebateBot is a Streamlit application that allows users to engage in debates on various topics. You can either debate against an AI or watch two AIs debate each other.

## 🚀 Features

* **🗣️ 1v1 Mode:** Engage in a debate with an AI. Choose your stance (For/Against) and the number of rounds.
* **🤖 AI vs AI Mode:** Watch two AI agents debate a topic for a specified number of rounds.
* **📜 Debate Transcript:** View the full transcript of the debate as it unfolds.
* **⚙️ Customizable Rounds:** Set the number of rounds for each debate.

## 🛠️ Tech Stack

* **Python:** The core programming language.
* **Streamlit:** For creating the interactive web application.
* **[Mention any other key libraries from your `backend.debate_manager` if relevant, e.g., LLM libraries]**

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Make sure you have a `requirements.txt` file. If not, you can create one using `pip freeze > requirements.txt` after installing necessary packages locally.
    ```bash
    pip install -r requirements.txt
    ```
    *Ensure `streamlit` and any libraries used by `backend.debate_manager` are listed in `requirements.txt`.*

## ▶️ Running the Application

1.  Navigate to the directory containing `app.py`.
2.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
3.  Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).

## 📝 How to Use

1.  **Select Debate Mode:**
    * Choose "🗣️ 1v1 Mode" to debate against the AI.
    * Choose "🤖 AI vs AI" to watch two AIs debate.
2.  **Enter the Debate Topic:** Type the topic you want to debate.
3.  **Number of Rounds:** Use the slider to select the number of rounds for the debate.
4.  **If in 1v1 Mode:**
    * **Choose your stance:** Select "For" or "Against" the topic. The AI will take the opposing stance.
5.  **Start Debate:** Click the "Start Debate" button.
6.  The debate transcript will be displayed below.

## 📁 Project Structure (Simplified)


.
├── app.py                  # Main Streamlit application file
├── backend/
│   └── debate_manager.py   # Handles the debate logic (assumption)
├── requirements.txt        # Project dependencies
└── README.md               # This file


## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the [Your Chosen License, e.g., MIT] License. See `LICENSE` file for more information (if you add one).

---

*This README was generated based on the provided `app.py`.*
*Remember to replace placeholders like `<your-repository-url>`, `<your-repository-name>`, and specify your license.*
