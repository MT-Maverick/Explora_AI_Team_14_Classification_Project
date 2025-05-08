"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: ExploreAI Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/


"""
# Streamlit dependencies
import streamlit as st
import joblib,os
from pathlib import Path
# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("vectorizer.pkl","rb")
test_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("https://raw.githubusercontent.com/Jana-Liebenberg/2401PTDS_Classification_Project/main/Data/processed/train.csv")

# The main function where we will build the actual app
def main():
	"""News Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("News Classifer")
	st.subheader("Analysing news articles")

	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Prediction", "Information"]
	selection = st.sidebar.selectbox("Choose Option", options)

	# Building out the "Information" page
	if selection == "Information":
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		markdown_file = Path('../README.md').read_text()
		st.markdown(markdown_file, unsafe_allow_html=True)

		
	# Building out the predication page
	if selection == "Prediction":
		st.info("Prediction with ML Models")
		# Creating a text box for user input
		news_text = st.text_area("Enter Text","Type Here")

	# List of available models
	model_options = {
		"Logistic Regression": "Logistic_regression.pkl",
		"Random Forest": "Random_forest.pkl",
		"SVM": "Support_Vector_Classifier.pkl",
		"Naive Bayes": "Naive_Bayes.pkl",
	}

	# Streamlit UI - Model selection
	selected_model = st.selectbox("Choose a model:", list(model_options.keys()))

	if st.button("Classify"):
			# Transforming user input with vectorizer
		vect_text = test_cv.transform([news_text]).toarray()

		# Load the selected model
		model_path = model_options[selected_model]

		predictor = joblib.load(open(os.path.join(model_path),"rb"))
		prediction = predictor.predict(vect_text)

		st.success("Text Categorized as: {}".format(prediction))


# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()
