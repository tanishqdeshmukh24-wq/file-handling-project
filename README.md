# 🗂️ File Handler Studio

A simple file management tool built with **Python** and **Streamlit**.
It started as a basic command-line script for handling files (create, read,
update, delete) and was turned into a clean, interactive web app.

## ✨ Features

- **Create** — make a new text file with custom content
- **Read** — view the contents of any file
- **Update** — rename a file, append content, or overwrite it entirely
- **Delete** — remove a file (with a confirmation step)
- Sidebar file browser showing all files and their sizes
- Clean error handling with user-friendly messages (no crashes on bad input)
- All files are sandboxed inside a local `user_files/` folder, so the app
  never touches anything else on your system

## 🖼️ Preview

<img width="1280" height="684" alt="Screenshot 2026-07-28 213752" src="https://github.com/user-attachments/assets/8795216d-27aa-4c64-a5c3-fd46b6d720bd" />


## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- `pathlib` for file operations

## 🚀 Getting Started

Clone the repo and run it locally:

```bash
git clone https://github.com/tanishqdeshmukh24-wq/file-handling-project.git
cd file-handling-project
pip install -r requirements.txt
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## 📂 Project Structure

```
file-handler-streamlit/
├── app.py              # Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 💡 What I Learned

- Turning a CLI script into an interactive web app with Streamlit
- Structuring a multi-feature app using tabs and sidebar components
- Handling file I/O safely with proper error handling and validation
- Thinking through UX details like confirmation steps for destructive actions

## 📄 License

This project is open source and available for anyone to use or build on.
