# 🤖 Local AI Chatbot: Phi-3 Mini Powered Assistant

This repository hosts a simple yet powerful local AI chatbot application built with Streamlit and `llama-cpp-python`, leveraging the efficient Microsoft Phi-3 Mini Large Language Model (LLM). Developed as a university project for **Burgas State University "Prof. Dr. Asen Zlatarov"**, this project demonstrates the capabilities of running modern LLMs directly on your local machine, offering a private and accessible AI assistant without reliance on cloud services.

## ✨ Features

*   **Local LLM Inference:** Runs entirely on your machine, ensuring data privacy and no internet dependency after the initial model download.
*   **Streamlit User Interface:** Provides an intuitive and easy-to-use web-based chat interface.
*   **Chat History:** Maintains conversation state within the session.
*   **GPU Acceleration:** Configurable `n_gpu_layers` to offload layers to your GPU for faster inference (requires a compatible GPU and `llama-cpp-python` built with GPU support).
*   **Lightweight Model:** Utilizes the Phi-3 Mini model, optimized for local deployment while delivering strong performance for its size.

## 🧠 About the Model: Microsoft Phi-3 Mini

The core of this chatbot is the **Microsoft Phi-3 Mini** model.

*   **Type:** A small, yet highly capable Large Language Model (LLM) developed by Microsoft. It's part of the Phi-3 family, known for punchy performance relative to their size.
*   **Version Used:** Specifically, `Phi-3-mini-4k-instruct-q4.gguf` is configured in the script.
    *   `4k`: Indicates a context window of 4,000 tokens, allowing for moderately long conversations.
    *   `instruct`: Means it's fine-tuned for instruction-following, making it good for chat and question-answering.
    *   `q4.gguf`: This specifies a **quantized** version of the model in the GGUF format. Quantization reduces the model's size and memory footprint, making it more efficient to run on consumer hardware, often with minimal impact on performance. GGUF is a common format for running models with `llama.cpp` and its Python bindings.
*   **Why Phi-3 Mini?** It's an excellent choice for local AI applications due to its balance of size, performance, and accessibility, making it suitable for educational projects and personal use cases where larger models might be too resource-intensive.

## 🚀 Installation

Follow these steps to get your local AI chatbot up and running:

### 1. Prerequisites

*   **Python 3.8+:** Ensure you have a recent version of Python installed.
*   **Git:** For cloning the repository.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name # Replace 'your-repo-name' with the actual folder name
```

### 3. Create a Virtual Environment (Recommended)

It's good practice to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

*   **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **On macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```

### 5. Install Dependencies

First, create a `requirements.txt` file in your project's root directory with the following content:

```
streamlit
llama-cpp-python
```

Then, install the dependencies:

```bash
pip install -r requirements.txt
```
**Note for `llama-cpp-python`:** If you have an NVIDIA GPU, you might want to install `llama-cpp-python` with CUDA support for better performance. Refer to the official `llama-cpp-python` documentation for advanced installation instructions: [https://github.com/abetlen/llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

### 6. Download the LLM Model

The model file (`Phi-3-mini-4k-instruct-q4.gguf`) needs to be downloaded and placed in the **same directory** as your `main.py` script.

*   **Download Link:** [https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/blob/main/Phi-3-mini-4k-instruct-q4.gguf](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/blob/main/Phi-3-mini-4k-instruct-q4.gguf)
*   **Direct Download (using `wget` or `curl` if available on your system):**
    ```bash
    # For Windows, you might need to install wget or use PowerShell's Invoke-WebRequest
    # PowerShell:
    # Invoke-WebRequest -Uri "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf" -OutFile "Phi-3-mini-4k-instruct-q4.gguf"

    # For Linux/macOS or if you have wget installed:
    wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf
    ```
    Make sure the downloaded file is named exactly `Phi-3-mini-4k-instruct-q4.gguf`.

## ⚙️ Usage

Once the model is downloaded and dependencies are installed, you can run the application:

```bash
streamlit run main.py
```

*(Assuming your Streamlit script is named `main.py`)*

This command will start a local web server, and your default web browser should automatically open to the chatbot interface (usually `http://localhost:8501`). You can then type your messages in the input box and interact with the AI assistant.

## 📂 Project Structure

```
.
├── .gitignore               # Specifies files and directories to be ignored by Git
├── main.py                  # The main Streamlit application script
├── requirements.txt         # Lists Python dependencies
└── Phi-3-mini-4k-instruct-q4.gguf  # The downloaded LLM model (should be placed here)
```

## 🤝 Acknowledgements

*   **Burgas State University "Prof. Dr. Asen Zlatarov"**: For providing the academic framework for this project.
*   **Microsoft**: For developing and open-sourcing the Phi-3 Mini models.
*   **Hugging Face**: For hosting the model and providing easy access.
*   **`llama.cpp` & `llama-cpp-python`**: For the incredible work on efficient LLM inference on consumer hardware.
*   **Streamlit**: For making it incredibly easy to build interactive web applications with Python.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
