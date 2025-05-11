# 📝 Text Summarizer

A Python-based text summarization pipeline built using **Hugging Face Transformers** and **PyTorch Lightning**.  
This project implements an **abstractive summarization model** using the **Pegasus** architecture fine-tuned on the **SAMSum dataset**.  
It features a modular pipeline for data processing, training, evaluation, and a **Streamlit-based web interface** for real-time summarization.

---

## 🚀 Features

- 🤖 **Abstractive Summarization** using the Pegasus model.
- ⚙️ **Modular Pipeline**: Includes stages for data ingestion, preprocessing, training, and evaluation.
- 📁 **YAML-Based Configuration** for easy parameter tuning.
- 🌐 **Streamlit Web App** for interactive summarization.
- 🐳 **Docker Support** for containerized deployment.

---

## 📁 Project Structure

Text-Summarizer-/

├── .github/workflows/        # GitHub Actions workflows    
├── config/ # Configuration files  
├── pegasus-samsum/ # Model checkpoints and outputs  
├── research/ # Research notebooks and experiments  
├── src/textSummarizer/ # Source code for the summarizer  
├── templates/ # HTML templates for Streamlit  
├── .gitignore  
├── Dockerfile # Docker configuration  
├── LICENSE  
├── README.md  
├── app.py # Streamlit web app  
├── main.py # Training pipeline entry point  
├── params.yaml # Hyperparameter configs  
├── requirements.txt # Dependencies  
├── setup.py # Package setup  
├── template.py # Template config  



---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/whoami-saloni/Text-Summarizer-.git
   cd Text-Summarizer-


2. **Create a virtual environment and activate it::**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate

3. **Install The Dependencies:**

   ```bash
   pip install -r requirements.txt


## 🧪 Usage

1. **✅Train The Model:**

   ```bash
   python main.py

 This will run the pipeline as defined in main.py, using configurations from params.yaml

2. **🌐 Launch the Web App:**
  To run the Streamlit-based web application
   ```bash
   streamlit run app.py
   
Then open your browser and go to: http://localhost:8501

## 🛠️ Configuration
All hyperparameters and paths are managed via the params.yaml file.
Update this file to:

- Change batch sizes, learning rate, and epochs

- Set custom model checkpoints

- Modify dataset paths

## 📄 License
This project is licensed under the MIT License.

## 🙌 Acknowledgements

This project uses the following tools and datasets:

- 🤗 [Hugging Face Transformers](https://huggingface.co/transformers/)
- 🔦 [PyTorch](https://pytorch.org/)
- 🧼 [Streamlit](https://streamlit.io/)
- 🗣️ [SAMSum Dataset](https://huggingface.co/datasets/samsum)


  


