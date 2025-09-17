# =========================
# Analyzing Data with Pandas and Visualizing Results with Matplotlib
# Dataset: Student Performance
# =========================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Task 1: Load and Explore the Dataset
# =========================

try:
    # Load dataset (update path if needed)
    df = pd.read_csv("student_performance.csv")

    # Display first few rows
    print("First five rows of the dataset:")
    print(df.head())

    # Check structure of dataset
    print("\nData types and missing values:")
    print(df.info())
    print("\nMissing values count:")
    print(df.isnull().sum())

    # Clean dataset (drop or fill missing values)
    df = df.dropna()

except FileNotFoundError:
    print("Error: Dataset file not found. Please check the file path.")
except Exception as e:
    print("An error occurred:", e)


# =========================
# Task 2: Basic Data Analysis
# =========================

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Example: Group by gender (or another categorical column if available)
if "gender" in df.columns:
    grouped = df.groupby("gender").mean(numeric_only=True)
    print("\nMean of numerical columns per gender:")
    print(grouped)

# Observations (customize based on dataset content)
print("\nObservations:")
print("- Differences in average scores by gender (if gender column exists).")
print("- Look for subjects where students tend to score higher/lower on average.")


# =========================
# Task 3: Data Visualization
# =========================

sns.set_style("whitegrid")  # optional, for prettier plots

# 1. Line chart - show trends over index (or time if there's a date column)
plt.figure(figsize=(8,5))
if "math_score" in df.columns:
    plt.plot(df.index, df["math_score"], label="Math Score")
if "reading_score" in df.columns:
    plt.plot(df.index, df["reading_score"], label="Reading Score")
plt.title("Line Chart: Student Scores over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Score")
plt.legend()
plt.show()

# 2. Bar chart - average score per category (e.g., gender)
if "gender" in df.columns and "math_score" in df.columns:
    plt.figure(figsize=(6,4))
    sns.barplot(x="gender", y="math_score", data=df, ci=None)
    plt.title("Bar Chart: Average Math Score per Gender")
    plt.xlabel("Gender")
    plt.ylabel("Math Score")
    plt.show()

# 3. Histogram - distribution of math scores
if "math_score" in df.columns:
    plt.figure(figsize=(6,4))
    plt.hist(df["math_score"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Histogram: Distribution of Math Scores")
    plt.xlabel("Math Score")
    plt.ylabel("Frequency")
    plt.show()

# 4. Scatter plot - relationship between math and reading scores
if "math_score" in df.columns and "reading_score" in df.columns:
    plt.figure(figsize=(6,4))
    plt.scatter(df["math_score"], df["reading_score"], alpha=0.7)
    plt.title("Scatter Plot: Math Score vs Reading Score")
    plt.xlabel("Math Score")
    plt.ylabel("Reading Score")
    plt.show()
