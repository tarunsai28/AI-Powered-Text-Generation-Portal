
# AI-Powered Text Generation Portal

An interactive AI-powered text generation application built using Python, Flask, and nanoGPT. The portal uses a custom-trained language model to generate Twitter-style text through a modern web interface.

## Project Overview

This project demonstrates the end-to-end process of preparing text data, training a language model, and integrating it into a web application.

The nanoGPT model was trained on a preprocessed Twitter conversation dataset and connected to a Flask backend for text generation.

Users can generate new text through a responsive web interface.

## Features

- AI-powered Twitter-style text generation
- Custom-trained nanoGPT language model
- Flask REST API integration
- Interactive Generate Text button
- Modern, responsive dark-themed interface
- Loading animation during generation
- Word counter for generated text
- Copy generated text functionality
- Clean output without unnecessary model logs

## Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Backend | Flask |
| Language Model | nanoGPT |
| Deep Learning Framework | PyTorch |
| Frontend | HTML, CSS, JavaScript |
| API Communication | Fetch API |
| Dataset | Preprocessed Twitter conversations |
| Version Control | Git and GitHub |

## Project Structure

```text
AI-Powered-Text-Generation-Portal/
|
|-- workshop-07/
|   |-- myNanoGPT/
|       |-- app.py
|       |-- index.html
|       |-- sample.py
|       |-- model.py
|       |-- train.py
|       |-- config.py
|       |-- data/
|           |-- twitter/
|               |-- input.txt
|               |-- prepare.py
|
|-- README.md
```

## Dataset Preparation

The project uses Twitter conversation data processed through a text preprocessing pipeline.

The preprocessing workflow includes:

1. Loading raw Twitter conversation data.
2. Cleaning and normalizing text.
3. Preparing the text for language model training.
4. Encoding text into tokens.
5. Creating training and validation datasets.

The processed text is used to train the nanoGPT language model.

## Model Training

The nanoGPT model was trained on the prepared Twitter dataset using PyTorch.

Training configuration:

- Model architecture: GPT-style Transformer
- Training iterations: 10,000
- Approximate model parameters: 0.84 million
- Training framework: PyTorch

The trained model checkpoint is loaded during text generation.

Model checkpoint files are excluded from Git tracking because of their size.

## Flask Backend

The Flask application connects the trained nanoGPT model to the frontend.

### Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Displays the web interface |
| `/generate` | GET | Generates text using nanoGPT |

The `/generate` endpoint runs `sample.py` and returns the generated text in JSON format.

Example response:

```json
{
  "generated_text": "Example AI-generated text."
}
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tarunsai28/AI-Powered-Text-Generation-Portal.git
```

### 2. Navigate to the Project

```bash
cd AI-Powered-Text-Generation-Portal/workshop-07/myNanoGPT
```

### 3. Run the Flask Application

Install `uv` and ensure a compatible Python environment is available.

```bash
uv run --no-project --with flask --with torch --with numpy --with tiktoken python app.py
```

The application starts at:

http://127.0.0.1:5000

**Note:** A compatible trained model checkpoint must be available in the configured `out_twitter` directory. Checkpoint files are not included in the Git repository.

## How to Use

1. Start the Flask server.
2. Open http://127.0.0.1:5000 in your browser.
3. Click **Generate New Text**.
4. Wait for the nanoGPT model to generate text.
5. View the generated output.
6. Check the word count or copy the generated text.
7. Click again to generate another sample.

## Application Workflow

```text
User
  |
  v
HTML / CSS / JavaScript Frontend
  |
  | GET /generate
  v
Flask Backend (app.py)
  |
  v
nanoGPT Sampling (sample.py)
  |
  v
Trained Model Checkpoint
  |
  v
Generated Text
  |
  v
JSON Response
  |
  v
Frontend Output Display
```

## Testing

The application was tested locally.

- Flask server started successfully.
- Homepage returned HTTP 200.
- Text generation endpoint returned HTTP 200.
- Generated text was displayed in the frontend.
- Multiple generation requests were tested.

## Future Improvements

- Support multiple trained datasets.
- Add user-controlled generation parameters.
- Add text generation history.
- Deploy the Flask application to a cloud platform.
- Improve model quality with additional training data.

## Author

Tarun Sai Tirumala

## Project

AI-Powered Text Generation Portal — Build Fellowship
