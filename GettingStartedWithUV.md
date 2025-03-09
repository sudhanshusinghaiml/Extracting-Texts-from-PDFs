# 🚀 UV - Comprehensive Guide

**UV** provides essential features for Python development — from installing Python and hacking on simple scripts to working on large projects that support multiple Python versions and platforms.

UV's interface can be broken down into sections, which are usable independently or together.

📖 **UV Reference Guide**: [Click here](https://docs.astral.sh/uv/getting-started/features/)

---

## 📌 Python Versions
### **Installing and Managing Python**
- `uv python install` → Install Python versions.
- `uv python list` → View available Python versions.
- `uv python find` → Find an installed Python version.
- `uv python pin` → Pin the current project to use a specific Python version.
- `uv python uninstall` → Uninstall a Python version.

🔹 **See the guide on installing Python to get started.**

---

## 📌 Scripts
### **Executing Standalone Python Scripts**
- `uv run` → Run a script.
- `uv add --script` → Add a dependency to a script.
- `uv remove --script` → Remove a dependency from a script.

🔹 **See the guide on running scripts to get started.**

---

## 📌 Projects
### **Creating and Working on Python Projects**
- `uv init` → Create a new Python project.
- `uv add` → Add a dependency to the project.
- `uv remove` → Remove a dependency from the project.
- `uv sync` → Sync the project's dependencies with the environment.
- `uv lock` → Create a lockfile for the project's dependencies.
- `uv run` → Run a command in the project environment.
- `uv tree` → View the dependency tree for the project.
- `uv build` → Build the project into distribution archives.
- `uv publish` → Publish the project to a package index.

🔹 **See the guide on projects to get started.**

---

## 📌 Tools
### **Running and Installing Tools Published to Python Package Indexes**
- `uvx` / `uv tool run` → Run a tool in a temporary environment.
- `uv tool install` → Install a tool user-wide.
- `uv tool uninstall` → Uninstall a tool.
- `uv tool list` → List installed tools.
- `uv tool update-shell` → Update the shell to include tool executables.

🔹 **See the guide on tools to get started.**

---

## 📌 The Pip Interface
### **Manually Managing Environments and Packages**
#### **Creating Virtual Environments (Replacing venv and virtualenv)**
- `uv venv` → Create a new virtual environment.

🔹 **See the documentation on using environments for details.**

#### **Managing Packages in an Environment (Replacing pip and pipdeptree)**
- `uv pip install` → Install packages into the current environment.
- `uv pip show` → Show details about an installed package.
- `uv pip freeze` → List installed packages and their versions.
- `uv pip check` → Check that the current environment has compatible packages.
- `uv pip list` → List installed packages.
- `uv pip uninstall` → Uninstall packages.
- `uv pip tree` → View the dependency tree for the environment.

🔹 **See the documentation on managing packages for details.**

#### **Locking Packages in an Environment (Replacing pip-tools)**
- `uv pip compile` → Compile requirements into a lockfile.
- `uv pip sync` → Sync an environment with a lockfile.

🔹 **See the documentation on locking environments for details.**

---

## 📌 Utility
### **Managing and Inspecting UV's State**
- `uv cache clean` → Remove cache entries.
- `uv cache prune` → Remove outdated cache entries.
- `uv cache dir` → Show the UV cache directory path.
- `uv tool dir` → Show the UV tool directory path.
- `uv python dir` → Show the UV installed Python versions path.
- `uv self update` → Update UV to the latest version.

---

## 🎯 Conclusion
UV provides a modern, efficient, and feature-rich environment for managing Python projects, scripts, dependencies, and tools.

🚀 Get started with **UV** today and streamline your Python development workflow!

📖 **UV Reference Guide**: [Click here](https://docs.astral.sh/uv/getting-started/features/)

