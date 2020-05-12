# Automated Essay Grading with Neural Networks
This project is inspired from "The Hewlett Foundation: Automated Essay Scoring" Kaggle competition.
For more details you can visit the site [here](https://www.kaggle.com/c/asap-aes/overview).
The intent of this project is to develop an intelligent system to automate the essay grading process using standard feedforward neural networks and Long Short Term Memory Models(**LSTM**).
The implementation is done using **TensorFlow** and **Keras**.

### Data
We are using the data from the kaggle competition.
The data can be found in the data folder. For more details of what the data contains, you can visit the Kaggle Page for the competition.
The link to the data is [here](https://www.kaggle.com/c/asap-aes/data).

This implementation uses the stanford GloVe vector embeddings which need to be downloaded too.
Go to the [link](https://nlp.stanford.edu/projects/glove/) and go to the `Download pre-trained word vectors` section. Download one of the 300d vector and unzip the file in the same folder in which you create your Jupyter Notebook.

### System requirements
There are certain system requirements for the implentation to work.
  - python 3.6+
  - pip
  - Jupyter Notebook

### Libraries
Upgrade to the latest version of pip. Use the command given below.
```sh
$ pip install --upgrade pip
```
There are certain libraries required for the implementation.
The libraries required are:
- numpy
- scipy
- pandas
- tensorflow
- pyspellchecker
- scikit-learn

There is a requirements.txt file which contains all the necessary libraries mentioned. They can be installed using the below command:
```sh
$ pip install -r requirements.txt
```
The installation part of the project is complete. Yayy !!

### Execution
The project has a Jupyter Notebook (**automated-essay-grader.ipynb**) which is used for the implementation of this project.

The Jupyter notebook has explainations as to what each cell does.
Run each cell and you can observe the output of the commands.
Some commands take longer to execute (they did on our PC atleast), because of the complex calculation and traing being done, so please be patient with it.

### Challenges
The dataset has a total of 8 sets with a total of 13000 samples but because of limited resources, we did our experiments on only 1 set of essays which contained a total of 1783 samples. 

The main challenge we faced was to tune the parameters to give the best accuracy for the models.
It included expermienting with the number of layers, the number of nodes in each layer, optimizer,
epochs, dropout, etc.

### Performance Metric
We used the cohen kappa score to calculate how good our model is. The Cohen's kappa coefficient (κ) is a statistic that is used to measure inter-rater reliability (and also Intra-rater reliability) for qualitative (categorical) items.[[wiki]](https://en.wikipedia.org/wiki/Cohen%27s_kappa)
Our labels can be considered categorical because the scores that a grader can assign is between to 2 to 8 and integer values only.

### Results
We were able to achieve a max cohen kappa score of **~0.79**. The will used will improve with more data being used for training. Our literature review should that by using all the data and tuning the LSTM, we can achieve a cohen kappa score of **0.94**.

Overall it was a fun project to work on which lead to immense learning!

**Note:** More detailed information/report can be found in the [Project Report.pdf](https://github.com/utsav-195/automated_essay_grader/blob/master/Project%20Report.pdf).
