# 📊 Test Coverage Dashboard (Mini SonarQube):

A full-stack Python-based **Test Coverage Analytics Dashboard** built using `pytest`, `coverage.py`, and `Streamlit`.
    It visually analyzes test coverage per file and highlights risky areas in the codebase.
    
## 🚀 Features
- 📁 File-wise test coverage breakdown
- 📊 Interactive bar chart visualization
- 🚨 High / Medium / Low risk classification
- 🔄 One-click test execution from UI
- 📥 Download coverage report (CSV)
- 🔍 Uncovered code insights
- ⚡ Real-time coverage refresh
- 
## 🧰 Tech Stack
- Python 🐍
- pytest
- coverage.py
- Streamlit
- Pandas
- 
## 📸 Preview
```bash
streamlit run dashboard/streamlit_app.py
```

⚙️ Setup Instructions:
```bash
  git clone https://github.com/YOUR_USERNAME/test-coverage-dashboard.git
  cd test-coverage-dashboard

  python -m venv venv
  venv\Scripts\activate

  pip install -r requirements.txt

  coverage run -m pytest
  coverage json -o coverage.json

  streamlit run dashboard/streamlit_app.py
```
## 👨‍💻Author:
  G.Bharath Kumar
