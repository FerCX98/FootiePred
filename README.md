*Work in Progress*
The match dataset I am using: https://www.kaggle.com/datasets/hugomathien/soccer (the Match dataset was too large to include here)

This database contains matches from 2008 to 2016. This is over 25000 matches spread across the 8 years that it covers. Football just as the world is changing quickly, and at the time of these matches, in my opinion football was a different game. However just as with most other machine learning tasks, at the heart of this project will be finding correlations between information that can be applied regardless of whether a match took place in 2008, or whether it will take place next week. 
The majority of the features I will be using will be coming from the FIFA video games. For those unfamiliar with it, it is a video game made after real life football. The players in the game are all given ratings from 1 to 100 in regards to attributes that are needed considered to be important to any football player. These are 29 base stats for outfield players, and in the case of goalkeepers they are only given 7. On top of these, every player has an overall rating, as well as a potential rating, which just refers to their maximum expected potential of becoming a better version of themselves in the future. 
For goalkeepers, the attributes are as follows:
Diving – This refers to their ability to ‘dive’, or jump through the air to reach a shot.
Handling – This refers to their ability to catch the ball and hold onto it when making a save, rather than punching it away.
Kicking – This refers to their ability as to how accurately they can pass the ball, this is a lot more important when they are making long passes rather then simple short ones.
Reflexes – This ability refers to how good their reflexes are when it comes to reacting to shots, which is especially important when making saves where the shot is coming from a relatively close range.
Speed – Sprint Speed – This marks the top speed they can achieve while running.
Speed – Acceleration - This refers to how quickly they can reach their top speed when starting to run.
Positioning – This refers to how well they position themselves in any given moment, where a position is considered better if that position has a higher chance of enabling them to stop the ball from going in the net.
For outfield players, the attributes are a little bit more complicated:
Pace – Sprint Speed – This 
Pace – Acceleration – This
Shooting – Positioning – This
Shooting – Finishing – This
Shooting – Shot Power - This
Shooting – Long Shots - This
Shooting – Volleys - This
Shooting – Penalties – This
Passing - Vision - This 
Passing - Crossing - This 
Passing – Free Kick - This 
Passing – Short Passing - This 
Passing – Long Passing - This 
Passing - Curve - This 
Dribbling - Agility- This
Dribbling - Balance - This
Dribbling - Reactions - This
Dribbling – Ball Control - This
Dribbling - Dribbling - This
Dribbling - Composure - This
Defence - Interceptions - This
Defence - Heading - This
Defence – Defensive Awareness - This
Defence – Sliding Tackle - This
Defence – Standing Tackle - This
Physical - Jumping - This
Physical - Stamina - This
Physical - Strength - This
Physical - Aggression - This



  
The database is made up of 7 tables:
Country – This table just encodes the name of the countries as integers, and the players’ nationality later will be represented by country ids defined in this table.
League – This table encodes the name of the 11 football leagues that are present in the database, and later the league in which a match is taking place will be identified by league ids defined in this table.
Match- This table is where all the information about the matches is. It is quite extensive as it contains 115 columns. 
Player – This table contains all the players that take part in the matches of the database. It also assigns a unique player_api_id to every player, which are used to accurately identify the players taking part in a match.
Player_Attributes – This table contains the attributes of the players contained in the Player table. This is highly useful as it makes retrieving the attributes of players in this dataset significantly easier, since it is connected to the Player table with the player_api_id, and this way I am sure to retrieve the attributes of the correct player every time. These attributes data could be acquired from other datasets, however linking them to the previous Player table would be highly problematic. This is because the names of players are not unique, there are players with the name and same nationality, so then I would have to use these data in combination with more data such as their birth dates to be able to uniquely identify them. This would take a longer time and would require more computing power.
Team – This table contain all of the football teams that appear in the Match table. It assigns each team a unique id, as well as contains their abbreviations.
Team Attributes – This table contains the attributes of all the teams that appear in the Team table. Although this also could be acquired from other datasets and it would be easier to link them then to link players as described above, this table still makes my job a lot faster and is still going to be useful.
From this dataset I had to create my own dataset, with the features and classes. First of all, I had to decide what exactly the features will be. The first limitation I had to put on it, is that I can only use data for this project if the data is known before a match starts. 
I chose to add every single available attribute of all the players in a starting line-up, followed by the team attributes after the last player. Then the same with the second team, and lastly of course the class, which is 0 for a draw, 1 for a home win and 2 for an away win. 
For the goalkeepers I chose to only include the goalkeeper specific stats, therefore a row starts with values for the home goalkeeper, followed by the values for the 10 outfield home players which are all the same format, and lastly the values for the home team. This is immediately followed by the away team in the same format. 
The team attributes data section has 12 attributes per team that are categorical data and not numeric data, so I encoded these as integer values 1 and 2 if they are binary, or 1 and 2 and 3 if they are ternary. These features are the team features that has names ending with ‘Class. Here is how I encoded them:
buildUpPlaySpeedClass:
Balanced : 1
Fast : 2
Slow : 3
buildUpPlayDribblingClass:
Little : 1
Normal : 2
Lots : 3
buildUpPlayPassingClass:
Mixed : 1
Short : 2
Long : 3
buildUpPlayPositioningClass:
Organised : 1
FreeForm : 2
chanceCreationPassingClass:
Normal : 1
Risky : 2
Safe : 3
chanceCreationCrossingClass:
Normal : 1
Lots : 2
Little : 3
chanceCreationShootingClass:
Normal : 1
Lots : 2
Little : 3
chanceCreationPositioningClass:
Organised : 1
FreeForm : 2
defencePressureClass:
Medium : 1
Deep : 2
High : 3
defenceAgressionClass:
Press : 1
Double : 2
Contain : 3
defenceTeamWidthClass:
Normal : 1
Wide : 2
Narrow : 3
defenceDefenderLineClass:
Cover : 1
OffsideTrap : 2

As all of the data comes from real life matches, I did not feel comfortable enough with imputing missing values at this stage of the project, and 1807 of the 14478 were missing at least one attribute for a variety of reasons, mainly because there are players that were not in FIFA. This means that roughly 12.5% of the data is missing features. I decided to remove them all for now, which left me with 12671 instances. 
To investigate the suitability of algorithms, I used WEKA explorer and experimenter to see some very initial results. I was using a general 10-fold cross-validation setting for every algorithm.
Initially I thought that the most useful algorithms would be decision trees, as it is very easy to see the most important features in a decision tree model, which I consider important information to see, which attributes of a player in a given position on the pitch had the highest impact at the chances of their team doing better in the game. This does not necessarily mean that I expect them to be the best performing type of algorithm, however they would provide with information that would be very useful for a wide range of purposes. 
Also, In my opinion there will be a need for some feature selection further down the road, because of the fact that the number of features is 696, which is extremely high, and it would be nearly mission impossible to get as much training data to be able to make this scalable. 
Runtime-wise Naïve Bayes took about 10 seconds, while RandomForest took about 2 minutes, J48 3.5 minutes, and iBK took about 5 minutes, so if I was to exponentially increase the size of the dataset, this would be something to consider, however for this project I did not consider the runtime, because in this scope they were all very reasonable. As for the suitability of deep learning networks, I was working with TensorFlow/Keras in combination with pandas and the scikit-learn packages. 
The biggest promise was shown by Naïve Bayes showing an initial 48.05%, Random Forest clocked in at 51.24%, J48 came to 40.63, while iBK also lagged behind with 41.61%.
From these results it made sense to pick the Random Forest algorithm for going forward, however I also wanted to investigate the suitability of neural networks. I chose to do this in code using two python packages, pandas for the data processing and TensorFlow/Keras for the neural networks. WEKA does have an extension called deep4j that allows the use of deep learning in its interface, however for deep learning I felt a lot more comfortable with TensorFlow as it allows for better customization of the entire process including hyper-parameter tuning. 
To begin with, I separated the last attribute which is the class as y, and the rest 696 values are the features. I used Dense layers, the input shape is: (number of rows,696), and the output layer has 3 neurons as it modelled as a ternary classification problem. The final activation function I set to SoftMax, as that is generally the best for non-binary classification problems. For the loss function I experimented with Sparse Categorical Cross entropy as well as Categorical Cross Entropy, there was no notable difference. As for the optimizer I started with the generally the best Adam. 
The initial observation when running this was that around the third epoch it reached 44.97% accuracy and from there on out, it did not learn anymore. The loss was very slightly improving until about 50 epochs, but after this learning completely stopped. 
This usually means that the network is getting overfitted very early and this blocks it from performing better. When looking at how it performed at predicting each of the 3 classes, it did significantly worse at dealing with draws, both predicting draws, and mistaking something as a draw. Because of this the other possibility I considered at this point was to take a second look at the data, and investigate if this could be due to draws being underrepresented, or something along these lines.
To combat overfitting I tried using dropout layers in the network, and treated the dropout rate as a hyperparameter between 0.2 and 0.8, however this resulted in no change.
My other effort for reducing overfitting was that I reduced the learning rate, went down as low as 0.0001, this resulted in a much lower initial accuracy, however this lower accuracy was improving a very small amount.
After that I tried to change the optimizer to the Adadelta optimizer, as the main feature of this optimizer is an adaptive learning rate, and this worked even better. 
However, after running it for 2000 epochs, the learning seems to stop without getting even close to the overfitted accuracy. Running it for an extended amount of time on a supercomputer would be interesting, but in the scope of my project further experiment with the learning rate seems futile. 
As for the distribution of instances of each class in the data, there were 3276 draws, 5825 home team wins, and 3570 away team wins. Even though I was half expecting the draw instances to be underrepresented, in this case actually the home wins are overrepresented. I decided to go on ahead with looking at if it is any help if I prune the home win instances so that they have an equal distribution. So initially it was 25.85% draws, 45.97% home team wins and 28.17% away team wins. I made the count of all three instances equal.
Thus, I decided that the best-looking path to take for this project is to drop neural networks and use a random forest classifier to proceed forward.
When looking at the confusion matrix, I observed that this method also has a high confusion rate for anything that involves a draw. Both classifying a draw as not a draw, and classifying not a draw as a draw. For this reason, I wanted to examine how much better it would fare if I were to join draws with either side. Meaning that even though I train it on ternary classes, for the predictions I look at the probability distribution of each class, and if a draw is predicted, I will change the prediction to the second most probable outcome. The Random Forest classifier has a ‘predict_proba’ method, that gives a list with the probabilities for each class instead of just the most probable class. This way no draws will be predicted. I will also change the meaning of the answers in the model, in a way that if a home win is predicted I will interpret it as either a home win or a draw, and if an away win is predicted then I am interpreting it as either an away win or a draw. So, in a way instead of saying who will win or nobody will win, it will be saying who won’t win.
The only slight problem with this evaluation model, is that very rarely it could occur that both the home and away win have the same probabilities. In this case, it would be possible to come up with a way to make a more educated guess, but because this is 47/ (3*3276*0.2) roughly 2.4% of the cases, I chose to assign them either way at random. I know that this could potentially damage the reproducibility of this project, however when investigation the possibility of doing this, this will not result in a make-or-break situation.
To see how well this works, I implemented a custom accuracy function where every instance which is a draw will be marked as correct.
I also made a chart where every instance is measured by the sum of the chance of a draw and the chance of the more probable team, instances are grouped by every 1 whole percent(1%,2%,3%...100%) and calculated the accuracy for each percent.
This is to see how much confidence it is possible to have in a given prediction depending on how sure the classifier is. The first instance starts at 62% and the last instances are at 97%. The uneducated, purely random guessing here 
0.62 --> 1 / 1 --> 100.0%
0.63 --> 12 / 13 --> 92.3076923076923%
0.64 --> 20 / 30 --> 66.66666666666666%
0.65 --> 22 / 56 --> 39.285714285714285%
0.66 --> 20 / 83 --> 24.096385542168676%
0.67 --> 35 / 135 --> 25.925925925925924%
0.68 --> 17 / 135 --> 12.592592592592592%
0.69 --> 162 / 228 --> 71.05263157894737%
0.7 --> 189 / 268 --> 70.52238805970148%
0.71 --> 194 / 268 --> 72.38805970149254%
0.72 --> 229 / 309 --> 74.11003236245955%
0.73 --> 219 / 307 --> 71.33550488599349%
0.74 --> 224 / 300 --> 74.66666666666667%
0.75 --> 221 / 289 --> 76.47058823529412%
0.76 --> 239 / 307 --> 77.85016286644951%
0.77 --> 213 / 262 --> 81.29770992366412%
0.78 --> 190 / 242 --> 78.51239669421489%
0.79 --> 195 / 252 --> 77.38095238095238%
0.8 --> 153 / 199 --> 76.88442211055276%
0.81 --> 164 / 213 --> 76.99530516431925%
0.82 --> 26 / 187 --> 13.903743315508022%
0.83 --> 41 / 160 --> 25.624999999999996%
0.84 --> 49 / 143 --> 34.26573426573427%
0.85 --> 62 / 124 --> 50.0%
0.86 --> 45 / 106 --> 42.45283018867924%
0.87 --> 42 / 69 --> 60.86956521739131%
0.88 --> 35 / 58 --> 60.3448275862069%
0.89 --> 39 / 71 --> 54.929577464788736%
0.9 --> 16 / 35 --> 45.714285714285715%
0.91 --> 12 / 23 --> 52.17391304347826%
0.92 --> 5 / 16 --> 31.25%
0.93 --> 3 / 10 --> 30.0%
0.94 --> 5 / 5 --> 100.0%
0.95 --> 5 / 5 --> 100.0%
0.96 --> 0 / 0 --> 0.0%
0.97 --> 4 / 4 --> 100.0%

It came to me that I need a new model to better capture the essence of the two-team competing against each other, and that the all the values are not together in this sense. 
For my first try, I came up with the idea of subtracting the attributes of the players and putting this as a feature into the model: So Home player 2 dribbling – away player 2 dribbling will be the player 2 dribbling value. This can be a negative value if the away player is better at this, but that is fine.
a    b    c   <-- classified as
   93 2626 1010 |    a = 0
  131 5613  922 |    b = 1
  111 2125 1847 |    c = 2
As you can see here, home wins are very well classified, draws are terrible once again, and away wins are not looking good. But again, the distribution of the examples is not too good, 3729 draws, 6666 home wins and 4083 away wins, so I have to deal with that. Hopefully the overall will improve once I equalized the instances in the dataset. So, I used the Weka Spreadsubsample supervised instance filter to deal with oversampling. I chose to do this instead of under sampling because I always want to work on 100% real data, most of the times I just don’t like to work with generated data. This reduced the number of each class instances to 3729 as that was the minimum of the draw class instances.
Even though the overall accuracy decreased, the confusion matrix looked a lot better after this:
a    b    c   <-- classified as
  975 1386 1368 |    a = 0
  854 2028  847 |    b = 1
  816  848 2065 |    c = 2
Afterwards I took it onto the whole data, after equalling the samples, there was 5362 of each. 
This resulted in an 86.37% accuracy, which is a whopping almost 8% accuracy over the previous model, and overall, a 19.63% improvement over purely guessing. It clear now to me that this model is the superior model, and that my hunch that the previous did not capture the fact that these teams and players are playing against each other and not playing together was a problem. 
    a    b    c   <-- classified as
 1505 1915 1942 |    a = 0
 1384 2919 1059 |    b = 1
 1323 1134 2905 |    c = 2

Now here is an interesting occurance: initially I was using Random Forst as that was the best, but in overall accuracy without unifying the draws, with this model it was actually outdone by naïve bayes, 46.66-45.45.56. However when looking at their confusion matrixes(naïve bayes is below), bayes only had a 85.59% accuracy while unifies with draws. Therefore with my way treating draws, random forest is still the better choice. However I have to take a note here that should anyone in the future choose not to treat the draws in a unified way as I am at the moment, naïve bayes definitely worths a look.
   a    b    c   <-- classified as
 1334 2017 2011 |    a = 0
 1125 3101 1136 |    b = 1
 1109 1182 3071 |    c = 2
The next thing I have to do is try my new model on neural network, I have high hopes.

