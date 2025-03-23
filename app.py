from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

# Load disease data
with open("templates/static/disease_data.json") as file:
    disease_data = json.load(file)

def detect_disease(symptoms):
    for disease, info in disease_data.items():
        if any(symptom.lower() in info["symptoms"] for symptom in symptoms):
            return disease, info
    return "Unknown Disease", {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symptoms = request.form.get("symptoms").split(", ")
        disease, details = detect_disease(symptoms)
        return render_template("result.html", disease=disease, details=details)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
