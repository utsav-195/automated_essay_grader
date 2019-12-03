# Automated Essay Grading with Neural Networks

This project is implemented using python.
The project is inspired from "The Hewlett Foundation: Automated Essay Scoring" Kaggle competition.
For more details you can visit the site [here](https://www.kaggle.com/c/asap-aes/overview).

### Data
We are using the data from the kaggle competition.
It is present in the data folder of the project zip.
The link to the data is [here]().

### System requirements
There are certain system requirements for the implentation to work.

  - python 3.6+
  - pip
  - Jupyter Notebook
##### pip
If you don't have pip installed on your system, you can search online on "How to install pip".
Use the approach to install pip based on your OS (Windows, Linux, MacOS).

Open your terminal/command prompt.
To upgrade to the latest version of pip use the command given below.
```sh
$ pip install --upgrade pip
```

##### Libraries
There are certain libraries required for the implementation.
The libraries required are:
- numpy
 - scipy
- pandas
 - tensorflow
- pyspellchecker
- scikit-learn

To install the libraries. Use the command given below.
```sh
$ pip install numpy scipy pandas tensorflow pickle pyspellchecker scikit-learn
```

##### Jupyter Notebook
If you don't have Jupter Notebook installed on your system, you can search online on "How to install Jupyter Notebook". Launch the Jupyter Notebook and copy paste the extracted zip in the Files tab.
You can also create a new Folder and then paste the files in that folder. 

The installation part of the project is complete. Yayy !!

### File Structure
After you paste the zip in the Jupyter Lab, the whole folder structure should look as follows:

  - data
    - \.\.
    - training_set_rel3.tsv
    - ..  .xls
    - .. .csv
    - ...
  - automated-essay-grader.ipynb
  - glove.840B.300d.txt
  - Project Report.docx
  - Project Presentation.pptx
  - README.md
  - requirements.txt

### Execution
The project has a Jupyter Notebook (**automated-essay-grader.ipynb**) which is used for the implementation of this project.
Open the Notebook by clicking on it. The notebook will open in a new tab.

The Jupyter notebook has explainations as to what each cell does.
Run each cell and you can observe the output of the commands.
Some commands take longer to execute (they did on our PC atleast), so please be patient with it.

### Conclusion
The project has been a great learning experience in NLP and how real world problems can be solved using the concepts learnt in class.