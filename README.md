# Virtual-Reality-EEG-analysis
We will process the data collected in a mindfulness intervention with virtual reality (VR) experiment, prepare the data for analyzing the effect of mindfulness intervention and use different machine learning models to classify data collected in different brain activities. 


Pre-intervention activity (pre.mat):
Each volunteer plays the BrainGymmer game. The time taken in this step depends on how much time the volunteer uses to finish the game.

Meditation (med.mat):
Each volunteer plays the VR TRIPP meditation game.  The TRIPP demo is used to guide the meditation. The entire process take about 10 minutes.

Post-intervention activities (post.mat):
Each volunteer plays the same BrainGymmer game as in the pre-intervention phase. The time taken in this step depends on how much time the volunteer uses to finish the game.


EEG data were recorded in all the above three phases using Compumedics Grael LT 34 channel recorder. Dataset is saved in a MAT LAB file. We will use package “pyEEG” to compute power spectrum intensity (PSI) to be used in modeling from https://github.com/forrestbao/pyeeg.

