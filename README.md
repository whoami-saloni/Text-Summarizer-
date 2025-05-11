Text Summarizer

A Python-based text summarization pipeline utilizing Hugging Face Transformers and PyTorch Lightning. This project implements an abstractive summarization model using the Pegasus architecture fine-tuned on the SAMSum dataset. It includes a modular training pipeline, configuration management, and a Streamlit-based web interface for interactive summarization.
GitHub

🚀 Features
Abstractive summarization using the Pegasus model.

Modular pipeline with stages for data ingestion, transformation, model training, and evaluation.

Configuration management using YAML files.

Streamlit web application for real-time text summarization.



📁 Project Structure


Text-Summarizer-/
├── .github/workflows/         # GitHub Actions workflows
├── config/                    # Configuration files
├── pegasus-samsum/            # Model checkpoints and runs
├── research/                  # Research notebooks and experiments
├── src/textSummarizer/        # Source code for the summarizer
├── templates/                 # HTML templates for the web app
├── .gitignore
├── Dockerfile                 # Docker configuration
├── LICENSE
├── README.md
├── app.py                     # Streamlit web application
├── main.py                    # Entry point for the training pipeline
├── params.yaml                # Hyperparameter configurations
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── template.py                # Template configurations
⚙️ Installation


Clone the repository:
git clone https://github.com/whoami-saloni/Text-Summarizer-.git
cd Text-Summarizer-

Create a virtual environment and activate it:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install the dependencies:

pip install -r requirements.txt
🧪 Usage
Training the Model
To train the model using the predefined pipeline:


python main.py

This script will execute the training pipeline as defined in main.py, utilizing configurations from params.yaml.
GitHub

Running the Web Application
To launch the Streamlit web application for interactive summarization:
GitHub


streamlit run app.py
Access the application in your browser at http://localhost:8501.

🛠️ Configuration
Hyperparameters and other configurations are managed through the params.yaml file. Adjust the parameters as needed to customize the training and evaluation processes.
GitHub


📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
This project leverages the following technologies and datasets:
Medevel

Hugging Face Transformers

PyTorch

Streamlit

SAMSum Dataset

For more details and updates, please refer to the GitHub repository.



