# Simple Writepad

A lightweight, responsive rich-text editor built using Python and Tkinter. This application goes beyond standard text editing by implementing advanced event binding mechanisms, dynamic tag layering, and real-time custom font styling behaviors similar to commercial word processors.

---

## 🚀 Key Features

* **Advanced Keyboard Shortcuts:** Global keyboard listeners for critical file system operations (`Ctrl+N`, `Ctrl+O`, `Ctrl+S`) and standard text formatting.
* **Context-Aware Formatting:** Fully integrated overrides preventing native system shortcut collisions (such as intercepting the deep-level Unix text widget `Ctrl+I` deletion/tab swap bug).
* **Granular Text Selection Engine:** Implements micro-tag management allowing users to highlight precise characters, lines, or blocks of text to apply individual font families, font sizing scales, and styling options independently without altering global document layouts.
* **Dynamic Tag Compounding:** Generates custom Tkinter style configurations on-the-fly (`Font_Size_Style` matrices) to handle multi-layered formatting blending seamlessly.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.x
* **GUI Framework:** Tkinter
* **Component Architecture:** Structured into an immutable state tuple registry, a centralized mutable Tkinter wrapper framework (`StringVar`/`IntVar`), and isolated runtime callback pipelines.

---

## 📦 Getting Started

### Prerequisites
Make sure you have Python installed on your local machine. Tkinter comes bundled automatically with standard Python distributions on Windows and macOS.

### Installation & Execution
1. Clone the repository to your desktop machine:
   ```bash
   git clone [https://github.com/Ratul-Chatterjee2006/Text-Editor.git](https://github.com/Ratul-Chatterjee2006/Text-Editor.git)
