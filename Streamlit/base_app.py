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

# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("vectorizer.pkl","rb")
test_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("https://raw.githubusercontent.com/Jana-Liebenberg/2401PTDS_Classification_Project/main/Data/processed/train.csv", encoding="utf-8")

# Load your machine learning models
# Example: Replace 'model1.pkl' and 'model2.pkl' with your actual model file paths
models = {
	"Model 1": joblib.load("best_model.pkl")
}

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
		st.markdown("This app uses machine learning models to classify news articles into predefined categories.")

		
	# Building out the predication page
	if selection == "Prediction":
		st.info("Prediction with ML Models")
		# Creating a text box for user input
		news_text = st.text_area("Enter Text","Type Here")

	if st.button("Classify"):
		if news_text:
			# Transforming user input with vectorizer
			vect_text = test_cv.transform([news_text]).toarray()

			# Get predictions from each model
			predictions = {model_name: model.predict(vect_text)[0] for model_name, model in models.items()}

			# Display predictions
			st.subheader("Model Predictions:")
			for model_name, category in predictions.items():
				st.write(f"**{model_name}:** {category}")
			# Show success message with categorized text
			st.success("Text Categorized as: {}".format(", ".join(predictions.values())))
		else:
			st.warning("Please enter an article for classification.")

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()
