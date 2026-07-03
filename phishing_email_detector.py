# phishing_email_detector.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
data = pd.read_csv("data/emails.csv")  # columns: 'content', 'label'
X = data['content']
y = data['label']

# Convert text to features
vectorizer = TfidfVectorizer(stop_words='english')
X_features = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model and vectorizer for later use
with open("email_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Email phishing model trained successfully!")

# Optional: test prediction
sample_email = ["Congratulations! You've won a prize, click here"]
sample_features = vectorizer.transform(sample_email)
print("Prediction:", model.predict(sample_features)[0])
