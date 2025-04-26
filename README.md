# 🌍 Travel Yari – Personalized Travel Recommendation Web App

A Flask-based web application that helps users discover popular places and recommends a travel destination based on their interests. Users can browse static pages showcasing visiting spots and a gallery, rate their preferences on categories like clubs, museums, and restaurants, and receive a tailored recommendation via a Decision Tree classifier.

## ✨ Features

- 🌏 **Home Page**: Hero banner with featured destinations and navigation menu.
- 🏞️ **Visiting Spots**: Card-based layout showcasing popular places (e.g., Sanghi Temple, Insomnia, Salar Jung Museum).
- 🌐 **Gallery**: A scrollable section displaying destination images.
- 🎓 **Rate Your Interests**: Interactive form where users rate categories (dance clubs, restaurants, museums, resorts, theaters, religious institutions) on a scale of 0–5.
- 🧬 **Personalized Recommendation**: User ratings are saved, analyzed using ML, and a travel location is predicted.

## ⚡ Getting Started

### 📅 Prerequisites

- Python 3.7+
- Flask
- scikit-learn
- pandas
- numpy

### 📚 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd TravelYari
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the dataset**
   - Place your labeled data file as `dataset.txt` in the project root.
   - Ensure it has the header:
     ```csv
     userid,dance_clubs,restaurants,museums,resorts,theaters,religious_institutions,location
     ```

### 💻 Running the App

```bash
export FLASK_ENV=development   # macOS/Linux
set FLASK_ENV=development      # Windows PowerShell
python app.py
```

Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## 📊 Project Structure

```
TravelYari/
├── app.py                 # Flask application entry point
├── Main.py                # ML pipeline (upload, feature selection, decision tree, prediction)
├── dataset.txt            # Training data for model
├── file.txt               # Generated input from user form
├── templates/             # HTML templates
│   ├── home.html
│   ├── index.html         # Rating form
│   └── output.html        # Recommendation results
├── static/                # Static assets (CSS, JS, images)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🔢 Dependencies

```text
Flask>=2.0.0
numpy>=1.18.0
pandas>=1.0.0
scikit-learn>=0.22.0
```

*(You can generate `requirements.txt` using `pip freeze > requirements.txt`.)*

## 🧰 How It Works

1. 🖋️ **User Interaction**
   - User rates each category on a scale from 0 to 5, then clicks **Submit**.
2. 📃 **Data Preparation**
   - Ratings are saved to `file.txt`.
   - `upload()` reads the main dataset `dataset.txt`.
3. 🏋️‍♂️ **Feature Selection**
   - Recursive Feature Elimination (RFE) is performed using a Decision Tree.
4. 📊 **Model Training**
   - The Decision Tree is trained on the dataset.
5. 🔢 **Prediction**
   - The model predicts the user's ideal travel spot and displays the results.

## ⚠️ Troubleshooting

- **ValueError: malformed node or edge data**: Ensure `dataset.txt` matches the expected header and data format.
- **scikit-learn errors**: Verify your `scikit-learn`, `numpy`, and `pandas` versions.

## 📚 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new features, bug fixes, or enhancements.

## 🔒 License

This project is licensed under the MIT License. See `LICENSE` for details.
