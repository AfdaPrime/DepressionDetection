# WIA1006 Machine Learning Assignment Project - Emotional Typewriter Application

**Group Name : Day N Night**

**Group Members :**
|         **Name**          | **Matric Number** |
|---------------------------|-------------------|
|  Muhammad Idzhans Khairi  |      U2000735     |
|  Afiq Danish bin Affindi  |      U2001419     |
| Magdalena Maya Anak David |      U2102800     |
|   Tessa Shalini Pradeep   |      U2102825     |
|  Amirul Aiman bin Mohsin  |      U2000595     |


---


# Structure and Clarity Report

## 1.0 Introduction to Problem
_“ Our vision is put into action through program to discover depression; to create a space where they feel comfortable and wanted”_


There are various forms of depression, each with its own set of symptoms, causes, and time frames.Depression is invisible, unobservable, and impossible to predict. Depression is a mental condition that many people are unaware of. It is critical that we assist our friends and family members in detecting depression before it worsens and becomes more serious.People tend to feel melancholy in a world without boundaries, and this issue is clearly influencing our generation negatively without us recognising it. In general, certain efforts were made to identify depression among humans, such as through questionnaires. It does not, however, always work. As a result, we must come up with a novel solution to the problem. Early signs of depression may go unnoticed, and without the help of a health professional, when depression becomes extreme, it can lead to suicide. Furthermore, it will increase the number of suicide cases in our country.To address this issue, we developed an application that users may use as a virtual journal. Once a day, a diary is normally written. As a result, users may utilize our programme to write about how they are feeling on any given day. Our application will allow the user to write anything in the diary about how they feel about the day, and once submitted, the database will accept the response, and we will utilise NLP (Natural Language Processing) to evaluate the response that he or she wrote that day. With the implementation of NLP, we could recognize the level of depression facing by him/her such as - Mild, Moderate, Severe. We also implement Facial Expression Recognition to know the facial expression of the writer when they are writing in their diary.

## 2.0 Hypothesis made for the problem
- View depression as a classification problem.
- Target users are English speaking users.
- Target users are uncomfortable with consulting other people in real life.
- The more negative the semantics detected by the model, the higher the possibility of being depressed.

## 3.0 Project Objectives
1. To create a depression indicator that helps to identify the level of depression an individual is facing.
2. To spread awareness of depression among university students to avoid further complications.
3. To identify the majority of depressed students based on their course, gender and age. 
4. To provide minor solutions to those who are identified with depression using our Diary. 
5. To implement Deep Learning in our diary to help expand our knowledge in Machine Learning.

## 4.0	Methodology

## 5.0	Elaboration on Data & Features Used

## 6.0	Results and discussions

## 7.0	Suggestion for future works


---


# Technical Content Report

## 1.0 Process Involved to Solve The Problem

### 1.1 Formation of Team Members
We consist of a group of first year students from the Faculty of Computer Science and Information Technology, University Of Malaya from occurrence 7 and 8.

### 1.2	Planning
We assess the work assigned to us by lecturers as soon as we obtain it, which is to develop a depression indicator using machine learning. We performed a great deal of research on depression in the first place because we were told not to make assumptions about depression symptoms and treatments based on their severity. We had read papers about depression, depression treatments, depression types, and depression symptoms. Following our research on depression, we devised numerous possibilities for implementing a depression indicator. After evaluating several aspects of the entire process of building a comprehensive and functional GUI of depression indicator, team members have presented numerous early proposals. We assigned assignments to each other in a fair and detailed manner. A comprehensive timetable was arranged very carefully in order to manage tasks easily. 

### 1.3	Designing
Our first aim was to create an app that would connect people to the company's Twitter account. It will turn on the camera when the user is using twitter (desktop) to look at the user's facial expression while using twitter. Aside from that, the programme will employ Natural Language Processing (NLP) to analyze the user's Twitter actions.

Due to time restrictions, we had to make a few changes to our original plan. For our users to express their views and relate their tales, we designed a diary place. We added an additional function called emotion recognition, which requires users to open their webcam and identify their face expression. We had sketched many interfaces to help us visualize our concepts in a real-world setting.

![1.3.1	Mainpage design using HTML](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Screenshot%20(91).png)

**_1.3.1 Mainpage Design Using HTML_**

![1.3.2	Journal history designs using HTML](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Screenshot%20(92).png)

![1.3.2	Journal history designs using HTML](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Screenshot%20(93).png)

**_1.3.2 Journal History Design Using HTML_**

![1.3.3 	Writing space design using HTML](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Screenshot%20(94).png)

**_1.3.3 Writing Space Design Using HTML_**

## 2.0 Background Theory


## 3.0 Experimental Protocol

### <ins>1. Purpose</ins>
The purpose of us creating a diary type of application  as a depression indicator is because the majority of university students are always comfortable with their own thoughts and are frequently judged for feeling sad or depressed. Not all of the students have a best friend or close friend for them to listen to about their problems. These kinds of students are always complaining or expressing their feelings through a platform where they can complain without anybody else noticing such as in their own private Twitter account. From here, we choose a diary method for our application to become a depression indicator as the student can express their feelings by typing into the diary without the limitation number of characters or words as Twitter. Then, we will implement Natural Language Processing (NLP) to detect their level of depression. With the suitable dataset, we will be able to detect the level of depression of the user by the frequency of the word that they are using in a particular diary. Other than that, the application also implements Facial Recognition to look at the user's facial expression while writing the diary.

### <ins>2. Materials</ins>
For our implementation of Machine Learning (NLP and Facial Recognition) in this diary application, we would use some dataset online to train the data for both NLP and Facial Recognition. For Facial Recognition, we will use a dataset called ‘Facial Expression Recognition Dataset’ from Kaggle. We can find the dataset for Facial Recognition in this link [here](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset). Next, for NLP, we will use the dataset of a .csv file from a google drive provided by a [youtube video](https://www.youtube.com/watch?v=pkPR8jYUN_8&list=WL&index=127) that taught us how to implement NLP in our project. The dataset can be obtained in this link [here](https://drive.google.com/drive/folders/1EwuMypz4kpQjfYvoABAU9SBuUabzT1DR). These datasets are important for us to train and create a model to be used by our application and users. Other materials that we would use is an IDE that can be used to run Python such as VS Code and PyCharm and also some youtube videos for us to learn how to implement these machine learning algorithms. We will also implement GUI for our application.

### 3. <ins>Methods</ins>
To set up this experiment, first and foremost we will find the suitable dataset used for our Machine Learning model for both NLP and Facial Expression Recognition. The dataset for NLP was obtained from [here](https://drive.google.com/drive/folders/1EwuMypz4kpQjfYvoABAU9SBuUabzT1DR) and the dataset for Facial Expression Recognition was obtained from [here](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset). However, the data need to be cleaned first so that there will be uniformity in our dataset. Next, we will train the data that we obtained by using the TensorFlow model for both Facial Expression Recognition (FER) and Natural Language Processing (NLP). However, we need some extra model for FER which is OpenCV to use the device’s camera and also to detect the user’s face through the camera.  After some coding to train the data, we test the trained data using Support Vector Machine (SVM) method by inserting some sentences and see if the sentence is determining if the user is having depression or not. After successfully training the data, we will save the trained data as a model for future use especially in our project. This also works the same for FER as we need to do some coding to train the data using the Deep Learning method based on the datasets of pictures that we obtained in the first place. After that we need to turn it into a model so that we can use it in the future, especially in our project. With both of these models created, all we need to do is create a GUI that acts as a diary application.

### 4. <ins>Controls</ins>
In conducting the experiment for this project, the manipulated variable will be the entry from the user into their diary and also their facial expression to the user’s device camera. Next, for the responding variable, it will be the result or percentage of depression of the users (NLP) and also the feelings or facial expression of the user’s at the moment they are typing in the diary (Facial Recognition). Lastly, the control variable will be the model that we trained for both NLP and Facial Recognition with their own datasets respectively. This will become the control variable because, if we manipulate any of the data inside both of the datasets, it will change the accuracy and also we need to train the data once again which will take time. Other than that, we are using these models to help us to determine the depression level and also facial expression of the users while they are using this application.

### 5. <ins>Data Interpretation</ins>
When we train the data, one of the main concerns that it would happen is overfitting. Overfitting is when your model fits the training data well, but it isn’t able to generalize and make accurate predictions for data it hasn’t seen before. Hence, to find out if the model is overfitting or not, we use a technique called cross-validation. We split the data into two parts - training set and validation set. The training set is used to train the model and validation set is only used to evaluate the model’s performance. In the training set, it lets you see how your model is progressing in terms of its training. For a validation set, it lets you measure the quality of your model. It measures how well it’s able to make new predictions based on the data that it hasn’t seen before from the dataset.

![Figure 3.0 - Loss](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%203.0.jfif)

**_Figure 3.0_**

![Figure 3.1 - Accuracy](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%203.1.jfif)

**_Figure 3.1_**

![Figure 3.2 - Epoch](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%203.2.jfif)

**_Figure 3.2_**

For Natural Language Processing, we measure the loss and accuracy on both training and validation sets. As we can see from figure 3.0 the loss (training set) decreases meanwhile the validation loss (validation set) is also decreasing but almost constant which is not bad for our validation loss. Next, as we can see from figure 3.1 the accuracy (training set) is increasing meanwhile the validation accuracy (validation set) is also increasing but almost constant which is also not bad for our model. As we can see in figure 3.2, The accuracy of the training set is at approximately 83% meanwhile the validation set is at approximately 82%. This means that you can expect your model to perform with approximately 82% accuracy on new data.

### 6. <ins>References</ins>
- Singh, S. [codepiep]. (2020, May 15). Twitter sentiment analysis using lstm tensorflow | NLP tutorial for beginners [Video]. Youtube. https://youtu.be/pkPR8jYUN_8
- What is the difference between the terms accuracy and validation accuracy. (2018, July). Stack Overflow. Retrieved 15 June 2022, from https://stackoverflow.com/questions/51344839/what-is-the-difference-between-the-terms-accuracy-and-validation-accuracy#:~:text=The%20training%20set%20is%20used,to%20evaluate%20the%20model’s%20performance.
- Starmer, J. [StatQuest with Josh Starmer]. (2019, October 1). Support Vector Machines Part 1 (of 3): Main Ideas!!! [Video]. Youtube. https://youtu.be/efR1C6CvhmE
- Simplilearn. (2021, March 17). Natural Language Processing In 5 Minutes | What Is NLP And How Does It Work? | Simplilearn [Video]. Youtube. https://youtu.be/CMrHM8a3hqw
- Jones, B. (2016, July 1). How to write an experiment protocol. Bridger Jones. Retrieved 15 June 2022, from https://bridger-jones.com/how-to-write-an-experiment-protocol/

## 4.0 Commented Source Code









