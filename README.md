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

You may open "app" folder to run overall application

---


# Structure and Clarity Report

## 1.0 Introduction to Problem
_“ Our vision is put into action through program to discover depression; to create a space where they feel comfortable and wanted”_


There are various forms of depression, each with its own set of symptoms, causes, and time frames.Depression is invisible, unobservable, and impossible to predict. Depression is a mental condition that many people are unaware of. It is critical that we assist our friends and family members in detecting depression before it worsens and becomes more serious.People tend to feel melancholy in a world without boundaries, and this issue is clearly influencing our generation negatively without us recognising it. In general, certain efforts were made to identify depression among humans, such as through questionnaires. It does not, however, always work. As a result, we must come up with a novel solution to the problem. Early signs of depression may go unnoticed, and without the help of a health professional, when depression becomes extreme, it can lead to suicide. Furthermore, it will increase the number of suicide cases in our country.To address this issue, we developed an application that users may use as a virtual journal. Once a day, a diary is normally written. As a result, users may utilize our programme to write about how they are feeling on any given day. Our application will allow the user to write anything in the diary about how they feel about the day, and once submitted, the database will accept the response, and we will utilise NLP (Natural Language Processing) to evaluate the response that he or she wrote that day. With the implementation of NLP, we could recognize the level of depression facing by him/her such as - Mild, Moderate, Severe. We also implement Facial Expression Recognition to know the facial expression of the writer when they are writing in their diary.

## 2.0 Hypothesis made for the problem
-	View depression as a classification problem.
-	Target users are university students .
-	Target users are uncomfortable with consulting other people in real life.
-	The more negative the semantics detected by the model, the higher the possibility of being depressed.


## 3.0 Project Objectives
1. To create a depression indicator that helps to identify the level of depression an individual is facing.
2. To spread awareness of depression among university students to avoid further complications.
3. To identify the majority of depressed students based on their course, gender and age. 
4. To provide minor solutions to those who are identified with depression using our Diary. 
5. To implement Deep Learning in our diary to help expand our knowledge in Machine Learning.

## 4.0	Methodology
To create a depression indicator we decided to take an approach in building a program which can help classify the level of depression an individual has based on the words used to write in their daily journal and also their facial expression.   We decided to implement Deep Learning to study facial expressions that are made by an individual. Furthermore, classified learning is used. We have collected data of different facial expressions that can help the program identify the expressions that will be done in real time by the individuals that use our system. Moreover, we have implemented classified learning. We have given our program a file of training sets that contains all the expressions. Therefore, the program studied each set or file thoroughly before implementing it in real time. Support Vector Machine algorithm is used for text recognition. This algorithm is used to help in text recognition by using the Natural Language Processing (NLP)  to help to identify words that are frequently used by depressed individuals. We used Graphic User Interface (GUI) to build the diary. Moreover the GUI also helps in making the diary more attractive and interesting. Therefore, our targeted users can be encouraged to share their insights on their life so we can help provide the solution needed. Facial Expression Recognition Each expressions like angry face, sad face, surprised face, happy face, and etc are taken from the Internet to help the program to study each expression in detail such that each features eyebrows, nose and eye. Text Recognition dataset for words that are identified as sad, happy, angry and etc is given to the program to learn and then classify the words that will be used by an individual in real time for each classification level of depression. 

## 5.0	Elaboration on Data & Features Used
Diary feature-University students can use the virtual diary as the space to tell stories and express their emotions and feelings on a particular day. This diary works to detect some words related to depression and sadness and facial detection for determine the emotion that person is currently having. For this program we have two different dataset to train two different models.

### 5.1 NLP data
For NLP, we use a dataset from a google drive provided by a youtube channel that taught us how to implement NLP for our project. The dataset originally has text intention which categorizes whether the text is depressed(0) or not(1), time and the text for the training. But For our model we only needed the text intention and the text itself which render the other element as irrelevant. Thus we make a new panda dataframe which only contains those two items, text intention and text, that we can now fit it to our model. After creating the new data frame, now we must clean the text as it fills with unnecessary symbols like number, comma, full stop etc. Then we split the data into two parts, train for training the model and test for validating the model, with the ratio of 70-30%. After splitting, we tokenize the train set, convert a text into a sequence of words and then we index the token which gets each different word its own index number.

![Figure 5.1.1 - Head of the unclean dataset](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%205.1.1.jfif)
![Figure 5.1.2 - Head of the unclean dataset](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%205.1.2.jfif)

**_Figure 5.1 Head of the clean dataset_**

### 5.2 Classification Data
The classification data used to build and train the Facial Expression Recognition program is taken from Keggle.com. This website contains ready made training sets that can help Machine Learning and Data Science students. According to the training set that we have downloaded, it contains the most common facial expressions that are made by humans on a daily basis like happy, sad, angry, surprised and disgusted. The training set is then inserted in our Facial Expression Recognition code to be implemented. Once the data was trained, when the program ran we got to see the results based on the web camera that a device has and it also displays the expression shown by the person in real time. Therefore the data set that was downloaded was used to train our program to make use of it in real time.

## 6.0	Results and discussions
### 6.1 Results
When we train the data, one of the main concerns that it would happen is overfitting. Overfitting is when your model fits the training data well, but it isn’t able to generalize and make accurate predictions for data it hasn’t seen before. Hence, to find out if the model is overfitting or not, we use a technique called cross-validation. We split the data into two parts - training set and validation set. The training set is used to train the model and validation set is only used to evaluate the model’s performance. In the training set, it lets you see how your model is progressing in terms of its training. For a validation set, it lets you measure the quality of your model. It measures how well it’s able to make new predictions based on the data that it hasn’t seen before from the dataset.

![Figure 3.0 - Loss](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%203.0.jfif)

**_Figure 6.0_**

![Figure 3.1 - Accuracy](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%203.1.jfif)

**_Figure 6.1_**

![Figure 3.2 - Epoch](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Figure%203.2.jfif)

**_Figure 6.2_**

For Natural Language Processing, we measure the loss and accuracy on both training and validation sets. As we can see from figure 6.0 the loss (training set) decreases meanwhile the validation loss (validation set) is also decreasing but almost constant which is not bad for our validation loss. Next, as we can see from figure 6.1 the accuracy (training set) is increasing meanwhile the validation accuracy (validation set) is also increasing but almost constant which is also not bad for our model. As we can see in figure 6.2, The accuracy of the training set is at approximately 83% meanwhile the validation set is at approximately 82%. This means that you can expect your model to perform with approximately 82% accuracy on new data.

### 6.2 	Discussion
#### <ins>Depression among University Students in Malaysia</ins>
According to the 2019 National Health and Morbidity Survey, about half a million Malaysians suffer from depression symptoms (NHMS 2019). Tan Sri Lee Lam Thye, the patron of The Befrienders Kuala Lumpur, stated that NHMS 2019 revealed many people have experienced emotional anguish as a result of the Covid-19 epidemic and the Movement Control Order (MCO). The commonness of this depression problem is rising over the past decade, especially among university students.

University students in Malaysia are a high-risk group for developing psychiatric disorders during adulthood. Social difficulties are on the rise among university students today. This rise is attributed to a variety of issues, including despair among students. Many factors previously contributed to depression, including familial issues, stressful life events, and low self-esteem can lead to self-harming behaviors and suicide.

As a result, this study and the development of this emotional typewriter application was carried out to determine the levels of depression among university students in Malaysia  as it is not visible on a daily basis so that early action can be taken. Students will be given suggestions of solutions to help them cope with their depression.

#### <ins>Journaling and Depression</ins>
Journaling is one of the ways that university students used to cope with depression. Many students like to express their problems and feelings on their private social media like Twitter. According to Danielle Roeske, PsyD, a psychologist and the vice president of Residential Services at Newport Healthcare, journaling can make emotions feel manageable. That is the reason why university students like to express their emotions by journaling. Most of them will feel calmer and relaxed after expressing all their negative thoughts in their private journal.

Moreover, most people are uncomfortable with consulting other people in real life. Many factors that make them uncomfortable are social anxiety, not having time, and so on. Journaling can be done 24 hours without any time restriction and they do not have to meet anyone. So, they will prefer to show their feelings with text and journals on private social media accounts.

So, here is where we got an idea to develop an application that can detect the level of depression from text in a diary by the frequency of the word that they are using in a particular diary. The more negative the semantics detected by the model, the higher the possibility of being depressed. This application can act as the platform for them to express all their feelings, thoughts, problems, and stressful events that make them depressed.

#### <ins>Facial Expressions Recognition Feature</ins>
At first, the limitation that our depression application faced is that we must assume that everyone will express their honest and real feelings in the form of text. Sometimes, text can be deceiving as people will act differently when typing in the text compared to speaking verbally. They might act like a different person, a so-called “alter ego” when typing in text. This is most likely because people love to showcase their best side to others.

After some discussion among groupmates about this problem, we add another feature to recognize facial expression. This feature is an additional feature to determine their feeling by the time they submit their journal on the add diary space . This feature is implemented to assume their emotions only but do not affect the depression rate because facial emotion can be varied to their feelings and emotion.


## 7.0	Suggestion for future works
1. 	Collaborate with hospitals and clinics
One of our future goals is to collaborate with national or international hospitals and clinics with our application. This is due to the fact that our programme may notify doctors to someone who is currently depressed. They can also tell if a person's depression is serious or not. If the situation is critical, the hospital should be able to contact them or go to them without having to wait for the user to contact them first. As the authorities are notified to what's going on with the individual who uses our app, this can automatically minimise suicide.

2. 	Improve the accuracy of the application
As we know accuracy for this project is 81% only. It is beyond our expectation but if this application is used in the future, the accuracy needs to be improved. The fact that it is really hard to get 100% but at least more than 98% if there is enough time. This is because people will be more confident with the result given by this application if the accuracy is near to 100%. By improving the accuracy, the performance of the application also increases.

3. 	Use theme that suits for depression people
For now, this application uses a soft color theme as we believe with all these colors chosen, it can make depressed people feel a little bit calm. However, a detailed research needs to be done, so that the theme chosen by this application is suitable for depressed people. For example, dark color can make someone feel more depressed and dull. Thus, this theme selection must get more attention in the future so the user can be  a little calmer than before.


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

### 1.4	Implementing
We created an application that uses SVM learning to detect words related to depression or suicidal thoughts in their diary to determine whether or not they have depression symptoms, and if they do, it specifies its severity , and provides suggestions on how to treat their depression based on its severity. We created classification learning as an additional feature to categorize emotions such as sad, furious, startled, and glad.

### 1.5	Testing
The process of executing a programme or system with the goal of identifying flaws is known as software testing. Examining the code as well as executing it in various contexts and situations are frequently included in the scope of testing. The project's testing steps are shown below, and the system was tested at each level.

Component or unit testing : Individual components are put to the test on their own. Functions, objects, or cohesive collections of these components can all be considered components.
System testing : The system as a whole is being tested. Emergent property testing is extremely significant.

Acceptance testing : Testing with data from university students to ensure that the system fits the needs of the users.

We had solved several issues in our codes during the testing and debugging process and discussed it with among us. Although our scripts and application implementation are not as perfect as we would want it to be, we recognised that this is due to time constraint, particularly in achieving our program's initial aim and strategy. We noticed many problems during our first testing, and we had some difficulty correcting them owing to our lack of grasp of the Python language. However, with the help of Internet resources and guidance from our seniors and friends, we were able to rectify certain flaws and address our difficulties in our codes.

## 2.0 Background Theory
### 2.1	Natural Language Processing (NLP)
Natural language processing (NLP) is a discipline of computer science, and more precisely, a field of artificial intelligence (AI), a text analysis technique that allows robots to interpret human speech. Automatic text summarization, sentiment analysis, topic extraction, named entity recognition, parts-of-speech tagging, connection extraction, stemming, and other real-world applications are made possible by this human-computer interaction. Text mining, machine translation, and automated question answering are all examples of how NLP is employed. NLP integrates statistical, machine learning, and deep learning models with computational linguistics regulation modeling of human language. These technologies, when used together, allow computers to interpret human language in the form of text or speech data and 'understand' its full meaning, including the speaker's or writer's purpose and mood.

### 2.2	Classification Algorithm
On the basis of training data, the Classification algorithm is a Supervised Learning technique that is used to categorize future observations. In classification, a software makes use of the dataset or observations that are provided to learn how to categorize fresh observations into various classes or groups. For instance, cat or dog, yes or no, 0 or 1, spam or not spam, etc. Targets, labels, and categories are all terms for classes.Classification requires a training dataset with many examples of inputs and outputs from which to learn.The output variable of Classification is a category, not a value, such as "Green or Blue" and "fruit or animal". Classification method uses labeled input data since it is a supervised learning approach, therefore it comprises input and output information.

In terms of modeling, classification necessitates a training dataset with a large number of instances of inputs and outputs from which to learn.The training dataset will be used to find the optimum way to map samples of input data to specified class labels. As a result, the training dataset has to be sufficiently representative of the issue and contain a large number of samples of each class label.

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
![Commented 01](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%201.jfif)
![Commented 02](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%202.jfif)
![Commented 03](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%203.jfif)
![Commented 04](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%204.jfif)
![Commented 05](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%205.jfif)
![Commented 06](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%206.jfif)
![Commented 07](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%207.jfif)
![Commented 08](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%208.jfif)
![Commented 09](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%209.jfif)
![Commented 10](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%2010.jfif)
![Commented 11](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%2011.jfif)
![Commented 12](https://github.com/AfdaPrime/DepressionDetection/blob/main/Media/Commented%2012.jfif)
