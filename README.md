# 


# 🚀 Extracting-Texts-from-PDFs: UV-Based Dependency Management

This module vastly covers the concepts about extracting data from PDFs using Langchain Framework using **UV(Ultra Violet)** a fast and lightweight Python runtime environment. This guide provides step-by-step instructions to install **UV**, set up the project, and get started.

---

## 📌 Prerequisites
Before installing UV, ensure you have the following:
- **Python** (version 3.10 or higher)
- **Git** installed
- **Basic knowledge of Python and API development**

---

## 📥 Installation Guide
Follow these steps to install **UV** and set up the project.

### 🔹 Step 1: Install UV
First, install **UV** using `pip`:
```bash
pip install uv
```

To verify that UV is installed, run:
```bash
uv --version
```

---

### 🔹 Step 2: Set Up the Project
Clone the repository:
```bash
git clone https://github.com/sudhanshusinghaiml/Extracting-Texts-from-PDFs.git
cd Extracting-Texts-from-PDFs
```

---

### 🔹 Step 3: Create and Manage a Virtual Environment
UV provides a **faster alternative to venv and virtualenv**.

Create a new UV environment:
```bash
uv venv .venv
```

Activate the environment:
- **Mac/Linux:**
  ```bash
  source .venv/bin/activate
  ```
- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

---

### 🔹 Step 4: Install Dependencies
Once the virtual environment is active, install dependencies:
```bash
uv pip install -r requirements.txt
```

If `requirements.txt` is not present, install dependencies manually:
```bash
uv pip install langchain==0.3.19 
```

```bash
uv add langchain==0.3.19
```

```bash
uv add langchain-community==0.3.18"
```

---

## 🛠 Additional Commands


### 🔄 Freeze Dependencies
To create a `requirements.txt` file:
```bash
uv pip freeze > requirements.txt
```

### 🛑 Deactivate Environment
To exit the virtual environment:
```bash
deactivate
```

---

## 📜 Project Structure
```
Extracting-Texts-from-PDFs/
├── main.py  # Main entry point
│── .venv/   # Virtual environment (created by UV)
│── data/    # Directory to save documents or datapoints  
│── .env     # env file to store environment variables
│── requirements.txt/ pyproject.toml # Dependencies
│── README.md  # Documentation
|── .gitignore
```

---



## 🚀 Working with Python Projects Using UV

### Creating and Managing Python Projects

- `uv init` → Create a new Python project.
- `uv add <package>` → Add a dependency to the project.
- `uv remove <package>` → Remove a dependency from the project.
- `uv sync` → Sync the project's dependencies with the environment.
- `uv lock` → Create a lockfile for the project's dependencies.
- `uv run <command>` → Run a command in the project environment.
- `uv tree` → View the dependency tree for the project.
- `uv build` → Build the project into distribution archives.
- `uv publish` → Publish the project to a package index.

---

## 🎯 Conclusion
By using **UV**, the project benefits from:
✅ **Faster dependency management**
✅ **Optimized virtual environments**
✅ **Better package resolution**

🚀 Now you're ready to start developing your UV-based project! Happy coding! 🎉
