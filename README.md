# TRINIT_Blank_ML01

## About the Project
Our project aims to create a COVID-19 web-based chatbot which replies to COVID-19 related queries and gives the optimum response for the same. As an additional feature we have also included a CNN-based model which takes in the lung x-rays of a user and outputs the probability of the user having the disease.

### Built with -
* TensorFlow / Keras
* Google Colab
* HTML
* CSS
* Flask

<br>

<!-- GETTING STARTED -->
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MistaAsh/TRINIT_Blank_ML01.git
   ```
2. Install TensorFlow libraries and other dependancies
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>
<br>

### Chatbot features
The chatbot uses an NLP-based model which is built upon the <i>Universal Sentence Encoder</i> of the TensorFlow libraries. This model uses a WHO_FAQ dataset to map the user inputted sentence to the nearest sentence within the dataset and provide the most accurate response.

<br>

### Lung X-Ray Classifier
The classification model of Lung X-rays as 'Covid' and 'Non-Covid' is based on a simple Convolutional Neural Network trained on a dataset for 25 epochs.

<br>

## Team Members
1. Ashish Bharath - NITK  
2. Inbasekaran P - NITK
3. Madhav Kumar - NITK
