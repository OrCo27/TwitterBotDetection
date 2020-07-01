# Twitter Bot Detection
This code is an implementation of [Learning to Rank Short Text Pairs with Convolutional Deep Neural Networks](http://disi.unitn.eu/moschitti/since2013/2015_SIGIR_Severyn_LearningRankShort.pdf "Learning to Rank Short Text Pairs with Convolutional Deep Neural Network") in Keras, in order to classify bot and human tweets.

## Notes
In **doc** folder you can find the following files:
1. **Help.pdf** - the help system for each component in each window.
2. **Learning to Rank Short Text Pairs with CNN.pdf**- the book for final project.

In **data** folder you can use the **environment.yml** file in order to configure your environment to the versions as mine.

In **screenshots** folder you can see the screenshots for all windows that used on our project.

## Algorithm
![image](https://user-images.githubusercontent.com/34770124/85947286-6586a080-b952-11ea-9898-8592ffadd285.png)

The user inserts a tweet to find whether the tweet was written by a person or by a bot. Then, for this tweet, we perform the preprocessing process and we create a Sentence Matrix that contains its words embedding representation. As part of the training model process, we create a list of bot tweets in their Sentence Matrix representation, and we use them for binding the tweet of the user for each of them. This process allows us to create pairs of bot-user tweets, so we can insert the pairs into the architecture for matching text pairs for checking if this tweet is similar for every bot tweet. 

As the output of the network, we will get the similarity scores list for each of the pairs we created, and then we convert the scores to classes (when zero means the two tweets have a different sentence structure, one means the opposite). 

In order to determine if the tweet written by a bot or human, we calculate the percentage of tweets that are similar, by calculating the ratio of the number of pairs who received the classification 1 to the number of total pairs. If this ratio passes the threshold selected by the user, the model will identify the tweet as bot tweet.

## How to run the project
- In order to set your environment like mine,  please use the yml file that exists on **data** folder, or use the following link of yml file for creating the environment: [environment.yml](https://drive.google.com/file/d/1qTrAOfsqjCyXvklOWgyU3OCGipCiQaxl/view?usp=sharing "environment.yml")

- In the first using, the folder **data** is empty except the yml file. This folder may contain all datasets files and pre-trained word2vec vectors. Please download all these files in the following link: [Data Files](https://drive.google.com/drive/folders/1yE9sHTextcNDBoUNW1PbzUa6pPTukWY3?usp=sharing "Data Files")

- If you want to use with already trained models, please download all files in the following link and copy them to **output** directory:  [Output Files](https://drive.google.com/drive/folders/1-vkuU0QhHxYcrzum4e7dy5QcRj4ZswqV?usp=sharing "Output Files")

- If you want to run the project directly without any IDE, you can download the executable folder in the following link: [Executable Folder](https://drive.google.com/drive/folders/1-yBtgDULyCBwzrHTW6ojf1xpCNDrxXvc?usp=sharing "Executable Folder")

- Video of the program: [Demonstration - Video](https://drive.google.com/file/d/1RCppiogy7_ngH8NTGwe_skc7z8yABdYB/view?usp=sharing "Demonstration - Video")
