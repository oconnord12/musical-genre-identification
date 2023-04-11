# music-genre-prediction
Dan O'Connor
oconnord6@gmail.com
https://github.com/oconnord12

Music genre prediction - prediciting musical genres based off acoustic features. 

This project I endeavored to predict musical genres from a wide array of pre-extracted acoustic features using various ML classification models. The acoustic features
were extracted from a 30 second clip of over 100,000 songs on Free Music Archieve. The feature extractions were completed by Michaël Defferrard in a paper titled 
'FMA: A Dataset For Music Analysis' (2017) (arXiv link: https://arxiv.org/pdf/1612.01840.pdf, GitHub link:https://github.com/mdeff/fma) This project was inspired by creating more genre specific playlists on 
streaming services, while certainly was not able to accomplish that I learned a substantial amount about feature extraction from audio samples, multi-class classifcation,
and the process of creating and testing models.


Documents included in this project folder:

Data: in included at this google drive link: https://drive.google.com/drive/folders/1-kxpI6UU6_g4QpmqSZ4TjdMH7LcrNN2y?usp=share_link
In the google drive you will find the following:
	-Original Data:
		-features.csv
		-tracks.csv
		-genres.csv
	-Added Data:
		-scores_df(1-4) was updated notebook to notebook, see scores_df4.csv for final success metrics.
		-accuracy_df(1-4) was updated notebook to notebook, see accuracy_df4.csv for model accuracies.
		-filtered_model_df.csv the data used for all modeling
		-features_single_header.csv a modified version of features.csv where the multi-level header is compressed to a single
	-Models: All of the trained optimized models were saved
		-decision_tree_optimized.joblib
		-final_nn_model.h5
		-final_smote_nn_model.h5
		-KNN.joblib
		-logistic_regression_optimized.joblib
		-random_forest.joblib
	-Audio: These are songs from FMA 
		-Bird Names - Referents 
		-Delta Dreambox - Without A Sound
		-Felipe Sarro - Bach, Prelude, BWV 855a, Siloti transcription
		-Nonima - Frenetic (ft. theAudiologist) 
	-Images: Used in notebooks
		-Genre_hierachy
		-feature tree

Jupyter Notebooks: The notebooks are ordered by the number appearing first
	-1_Dan_OConnor_GenreIdentification_Data_Cleaning: Clean and load original data
	-2_Dan_OConnor_GenreIdentification_Feature_Extraction: Demonstrate and explain the feature extraction process
	-3_Dan_OConnor_GenreIdentification_EDA: Basic EDA
	-4_Dan_OConnor_GenreIdentification_Baseline_RandomForest_DecisionTree: Create baseline model, RF, and DT
	-5_Dan_OConnor_GenreIdentifation_LogReg_KNN: Create LR and KNN models
	-6_Dan_OConnor_GenreIdentification_NN: Create neural network
	-7_Dan_OConnor_GenreIdentification_SMOTE_Modeling: Train a neural network with SMOTE training data
	-8_Dan_OConnor_GenreIdentification_Model_Analysis: Analyze accuracy and other success metrics of models
	-9_Dan_OConnor_ConfMatrix_ModelingFun: Inspect the best models confusion matrix and try some unseen samples on models

Python files:
	-myfunction: stores a single function used throughout the notebooks


	
Required Python Libraries:
	-Pandas
	-Tensorflow (NN modeling)
	-Seaborn
	-Librosa (feature extraction)
	-Matplotlib
	-os.path (used to properly load original .csv's)
	-ast (used to properly load original .csv's)
	-numpy
	-IPython.display (play audio files)
	-scipy


