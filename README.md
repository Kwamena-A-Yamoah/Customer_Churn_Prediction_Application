# Customer Churn Prediction Application

This **Customer Churn Prediction Application** is built using **Streamlit** to provide tools for analyzing and predicting telecom customer churn. It includes three main pages: **Home**, **Dashboard**, and **Predict**, each designed to facilitate exploratory data analysis, data visualization, and predictive modeling.

---

## Features

### 1. **Home Page**
- Overview of the application.
- Introduces its purpose (analyzing and predicting customer churn).
- Guides users on navigation.

---

### 2. **Dashboard Page**
- **Dataset Overview**: Displays a snapshot (first 5 rows) and descriptive statistics of the dataset.
- **Churn Distribution**: Pie chart to show churned and non-churned customers' proportions.
- **Bar Chart Comparisons**: Dynamic bar charts comparing relationships between features.
- **Feature Distribution**: Histograms for visualizing selected features.
- **Correlation Heatmap**: Heatmap showing feature correlations.
- **Advanced Analysis**:
  - Scatterplots for numerical feature relationships.
  - Bivariate analysis (bar charts for categorical features, boxplots for numerical features).

---

### 3. **Predict Page**
- **Model Selection**: Choose between `Linear Regression` or `Support Vector Classifier (SVC)`.
- **Customer Details Form**: Input key attributes like gender, tenure, contract type, etc.
- **Prediction Results**: Displays churn prediction and probabilities.
- **Prediction History**: Saves prediction results to a CSV file (`history.csv`).

---

## Installation

### Prerequisites
- Python 3.10+
- Required libraries: `Streamlit`, `pandas`, `plotly`, `joblib`

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
2. Launch the app:
   ```bash
   streamlit run 1_home.py

   
