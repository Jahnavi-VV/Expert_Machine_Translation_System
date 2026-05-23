# Expert_Machine_Translation_System

### Offline Transformer-Based Multilingual Translator

An intelligent **Machine Translation System** built using **Streamlit, HuggingFace Transformers, and PyTorch** that translates English text into **Telugu, Hindi, and French** using Meta’s **NLLB-200 Transformer Encoder–Decoder model**. The application supports both direct text input and uploaded **TXT/PDF files**, and also generates **audio output** from translated text.

---

# 📌 Project Overview

This project demonstrates a **real-world Natural Language Processing (NLP)** application that performs multilingual translation completely through **local Transformer inference** without relying on cloud translation APIs.

The system accepts English text or uploaded documents, processes the content, translates it into the selected language, and converts the translated output into speech for playback and download.

---

# 🎯 Objectives

* Build an **offline multilingual translation system**
* Eliminate dependency on cloud translation APIs
* Preserve translation accuracy and context
* Support document translation through PDF/TXT uploads
* Generate translated speech output

---

# ✨ Features

* English → Telugu Translation
* English → Hindi Translation
* English → French Translation
* PDF Upload Support
* TXT File Upload Support
* Audio Generation (Text-to-Speech)
* Interactive Streamlit UI
* Local Transformer Inference
* Download Generated Audio (.mp3)

---

# 🏗️ System Architecture

```plaintext
User Input
(Text / PDF / TXT)
        │
        ▼
Text Extraction
(PyPDF2 / UTF-8)
        │
        ▼
Tokenization
(HuggingFace Tokenizer)
        │
        ▼
Transformer Model
(NLLB-200 Encoder–Decoder)
        │
        ▼
Translation Output
        │
        ▼
Text-to-Speech
(gTTS)
        │
        ▼
Audio Playback & Download
```

---

# ⚙️ Workflow

## Step 1: User Input

Users can:

* Enter English text manually
* Upload TXT files
* Upload PDF documents

---

## Step 2: File Processing

### TXT Processing

* Reads uploaded text
* Converts UTF-8 content

### PDF Processing

* Extracts document text
* Combines multiple pages

---

## Step 3: Transformer Translation

The system loads:

```plaintext
facebook/nllb-200-distilled-600M
```

Translation Pipeline:

```plaintext
Input Text
↓
Tokenizer
↓
Encoder
↓
Decoder
↓
Translated Text
```

Language Mapping:

```plaintext
Telugu → tel_Telu
Hindi → hin_Deva
French → fra_Latn
```

---

## Step 4: Text-to-Speech

The translated output is converted into speech using:

```plaintext
gTTS
```

Users can:

* Listen to audio
* Download MP3 output

---

# 🧠 Model Details

## Model Used

**facebook/nllb-200-distilled-600M**

### Architecture

Transformer Encoder–Decoder

### Framework

HuggingFace Transformers

### Training

Supports 200+ languages

### Key Components

### Encoder

Extracts meaning and context.

### Decoder

Generates target language text.

### forced_bos_token_id

Forces translation into selected language.

### Tokenizer

Converts text into model-understandable tokens.

---

# 🛠️ Tech Stack

## Programming Language

* Python

## Frontend

* Streamlit

## Backend

* Python Backend
* File Handling

## AI/ML

* Machine Learning
* Natural Language Processing
* Machine Translation
* Transformer Models
* HuggingFace
* PyTorch

## Libraries

```plaintext
transformers
torch
streamlit
gtts
PyPDF2
python-dotenv
```

---

# 📂 Project Structure

```plaintext
Expert-Machine-Translation/
│
├── app.py
├── requirements.txt
├── README.md
├── assets/
├── sample_files/
└── screenshots/
```

---

# 📸 Output

### Translation Output

* Multilingual translated text
  <img width="1600" height="900" alt="O1" src="https://github.com/user-attachments/assets/3b1c0cf0-ff96-43da-b796-761bd89bb7a3" />


### Audio Output

* MP3 playback
* Download support
  <img width="1600" height="900" alt="O2" src="https://github.com/user-attachments/assets/ef5e2f7b-7967-443e-8fef-67ed2c8ebbd5" />


---

# 🔥 Key Learnings

* Transformer Encoder–Decoder Architecture
* HuggingFace Model Integration
* Streamlit Application Development
* NLP Workflow Design
* File Processing and Audio Generation
* Local AI Model Deployment

---

# ⚠️ Limitations

* Initial model download (~2.5GB)
* Long documents truncated at 512 tokens
* gTTS requires internet
* GPU recommended for better performance

---

# 📌 Conclusion

This project demonstrates how **Transformer-based multilingual translation** can be implemented efficiently without cloud dependency. By integrating **HuggingFace NLLB-200, Streamlit, PyTorch, PyPDF2, and gTTS**, the system provides a scalable and practical solution for offline AI-powered language translation.

