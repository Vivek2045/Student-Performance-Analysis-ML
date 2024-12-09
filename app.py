from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Function to classify average score into groups
def classify_group(avg_score):
    if avg_score < 35:
        return "E"
    elif 35 <= avg_score <= 55:
        return "D"
    elif 55 < avg_score <= 75:
        return "C"
    elif 75 < avg_score <= 85:
        return "B"
    else:
        return "A"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve input values from the form
        math_score = float(request.form['math_score'])
        reading_score = float(request.form['reading_score'])
        writing_score = float(request.form['writing_score'])

        # Calculate average score
        avg_score = (math_score + reading_score + writing_score) / 3

        # Determine the group
        group = classify_group(avg_score)

        return render_template('index.html', prediction=f"Predicted Group: {group} (Average Score: {avg_score:.2f})")

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

