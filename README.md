# Covid-Chatbot

<img src="https://img.shields.io/github/license/MistaAsh/Covid-Chatbot"> <img src="https://img.shields.io/github/languages/top/MistaAsh/Covid-Chatbot"> <img src="https://img.shields.io/github/issues/MistaAsh/Covid-Chatbot"> <img src="https://img.shields.io/github/issues-pr/MistaAsh/Covid-Chatbot"> <img src="https://img.shields.io/github/last-commit/MistaAsh/Covid-Chatbot">

## About the Project
The project aims to create a COVID-19 web-based chatbot which replies to COVID-19 related queries and gives the optimum response for the same. As an additional feature we have also included a CNN-based model which takes in the lung X-rays of a user and outputs the probability of the user having the disease.

<!-- GETTING STARTED -->
### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/MistaAsh/Covid-Chatbot.git
   ```

2. Install TensorFlow libraries and other dependancies

   ```sh
   pip install -r requirements.txt
   ```

<br>

### Chatbot features

The chatbot uses an NLP-based model which is built upon the *Universal Sentence Encoder* of the TensorFlow libraries. This model uses a WHO_FAQ dataset to map the user inputted sentence to the nearest sentence within the dataset and provide the most accurate response.

<br>

### Lung X-Ray Classifier

The classification model of Lung X-rays as 'Covid' and 'Non-Covid' is based on a simple Convolutional Neural Network trained on a dataset for 25 epochs.
