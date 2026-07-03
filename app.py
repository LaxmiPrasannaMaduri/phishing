from flask import Flask, render_template, request
from phishing_url_detector import is_phishing_url
import pickle

app = Flask(__name__)

# Load trained email model and vectorizer
with open("email_model.pkl", "rb") as f:
    email_model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_type = None

    if request.method == "POST":
        input_type = request.form["input_type"]
        user_input = request.form["user_input"]

        if input_type == "url":
            status = is_phishing_url(user_input)
            result = "Safe" if status == "Safe" else "Suspicious"
        elif input_type == "email":
            features = vectorizer.transform([user_input])
            prediction = email_model.predict(features)[0]
            # Map email labels to Safe/Suspicious for display
            if prediction.lower() == "legitimate":
                result = "Safe"
            else:
                result = "Suspicious"

    return render_template("index.html", result=result, input_type=input_type)

if __name__ == "__main__":
    app.run(debug=True)
