
# 📝 Blog Generator using OpenAI (GPT-3.5 Turbo)

Welcome to my AI project! 🚀  
This Python app generates blog-style paragraphs based on topics you choose – powered by **OpenAI's GPT-3.5 Turbo**.

Perfect for anyone curious about AI, Python, or content generation. 🤖✍️

---

## 💡 What does it do?

- You enter a topic (e.g. "The future of AI")
- The app sends it to OpenAI's GPT-3.5 model
- It returns a well-written paragraph about your topic
- You can keep adding as many paragraphs as you like!

---

## 📦 Requirements

To run this project, you need:

- ✅ Python 3.10 or higher
- ✅ An [OpenAI API Key](https://platform.openai.com/account/api-keys)
- ✅ Python packages: `openai`, `python-dotenv`

---

## 🔧 Setup Instructions

1. **Clone or download** this project to your computer  
2. **Create a `.env` file** in the root directory and add your API key:

```

OPENAI\_API\_KEY=your\_openai\_api\_key\_here

````

⚠️ **Never share this key** or upload your `.env` file!

3. **Install the required packages**:

```bash
pip install openai python-dotenv
````

4. **Run the app**:

```bash
python blog_generator.py
```

---

## 🖥️ Example

```text
Write a paragraph? (Y = yes, anything else = no): Y
What should this paragraph talk about? The future of AI

→ The model will generate a full paragraph about that topic.
```

---

## 📁 Project Structure

```bash
blog-generator/
│
├── blog_generator.py     # Main script
├── .gitignore            # Tells Git to ignore .env
├── .env                  # Your API key (NOT uploaded to GitHub)
└── README.md             # This file
```

---

## 🔐 Security Notice

The `.env` file contains your private API key and **must never be uploaded to GitHub**.
That's why it's listed in `.gitignore`.

If your key was accidentally committed once, remove it from your history or regenerate it from OpenAI's dashboard.

---

## 👩‍💻 Created by

**Shirin Sharifi**
AI Beginner | #100DaysOfAI | Exploring the world of machine learning
🌐 [GitHub](https://github.com/shirinxbyte)

---

## 🚀 Future Ideas

* Generate full blog posts with multiple paragraphs
* Add blog outlines or headlines
* Turn this into a web app using `streamlit`
* Add image generation using DALL·E

---

> ⭐️ If you like this project, consider giving it a star on GitHub!


Let me know if you'd like me to:

- Help you create a GitHub project banner
- Turn this into a one-click web app with `streamlit`
- Add more features like blog post export or image generation

You're doing amazing, Shirin – keep going! 🌟
```
