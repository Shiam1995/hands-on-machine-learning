"""

1. How would you define machine learning?

2. Can you name four types of applications where it shines?
3. What is a labeled training set?
4. What are the two most common supervised tasks?
5. Can you name four common unsupervised tasks?
6. What type of algorithm would you use to allow a robot to walk in various
unknown terrains?
7. What type of algorithm would you use to segment your customers into multiple
groups?
8. Would you frame the problem of spam detection as a supervised learning prob‐
lem or an unsupervised learning problem?
9. What is an online learning system?
10. What is out-of-core learning?
11. What type of algorithm relies on a similarity measure to make predictions?
12. What is the difference between a model parameter and a model hyperparameter?
13. What do model-based algorithms search for? What is the most common strategy
they use to succeed? How do they make predictions?
14. Can you name four of the main challenges in machine learning?
15. If your model performs great on the training data but generalizes poorly to new
instances, what is happening? Can you name three possible solutions?
16. What is a test set, and why would you want to use it?
17. What is the purpose of a validation set?
18. What is the train-dev set, when do you need it, and how do you use it?
19. What can go wrong if you tune hyperparameters using the test set?

"""

print("Answers to chapter 1 of hands on machine learning")

"""
1. a program learning from data rather than human finetuning, my favorite answer 
experience = e 
task = t 
improvment = i
measure = m

improvement on measurement of experience of task 

2.
RL - good for agents try and learning things in envrionment - Games and robotics
Supervised - good for putting ideas from human to machine - predict fraud
Semi-supervised - good for labelleing quickly - classification of biologics 
Unsupervised - good for letting a task learn when full data avalibale - spam filet 

3.

a dataset is labelled when most/all of the data has a label

4. common supervised tasks email spam and brain scan classification and regression

5. common unsupervised tasks: brain scans, forecasting future revenue, scanning documents, fraud

6. Id use RL - beacuase its probably an unknown env with too many details 

7.clustering 

8. id say unsupervised i think we have enough cases for it to learn by itself - if it is labelled
or not changes the answer

9. online learning, get constant feed of data at different times its on all the time and can learn   
not done once then left static

10. breaks up a big piece of learing into smaller bits to be learnt 

11. k - clustering nearest neighbors

12. model hyperparameter is done before the model is made it s the recipe 
to make the models results

13. to make a model of things then predict from these models

14. getting good data, balancing training under/over fitting, pick the right models
doing it cost effectively 


15. overfitting: try and hide more of the training set, try and regularise, try and get more data

16. test set , something to test model against , how will you know if you model is any good
if you have nothing to test against

17. validation set is used during training 

18. model is trianed with vaiours hyperparamters because we may not know which is the best one
then tests

19. overfitting, 

"""

# claude gave me 51% some full and partial