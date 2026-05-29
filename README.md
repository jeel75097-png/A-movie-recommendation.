# 🎬 Movie Recommendation System using Machine Learning

A Content-Based Movie Recommendation System that suggests movies similar to a user's favorite movie using Natural Language Processing (NLP) and Cosine Similarity.

---

## 📌 Project Overview

Finding movies to watch can be difficult when thousands of options are available.

This project recommends movies based on a movie that the user likes. The recommendation engine analyzes movie features such as:

- Genres
- Keywords
- Taglines
- Cast
- Director

and finds movies with similar characteristics.

---

## 🎯 Objectives

- Recommend similar movies to users
- Build a content-based recommendation engine
- Apply Natural Language Processing (NLP)
- Calculate similarity between movies
- Provide personalized movie suggestions

---

## 📂 Dataset

Dataset: **movies.csv**

The dataset contains information about thousands of movies.

### Features Used

| Feature | Description |
|----------|------------|
| genres | Movie genres |
| keywords | Important movie keywords |
| tagline | Movie tagline |
| cast | Actors in the movie |
| director | Movie director |

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- NLP (TF-IDF Vectorization)

---

## 🤖 Recommendation Technique

### Content-Based Filtering

The system recommends movies by comparing movie content instead of user ratings.

It analyzes:

- Story themes
- Genres
- Actors
- Directors
- Keywords

to identify similar movies.

---

## 🚀 Project Workflow

### 1️⃣ Load Dataset

Load movie dataset using Pandas.

### 2️⃣ Select Important Features

The following columns are used:

```python
genres
keywords
tagline
cast
director
```

### 3️⃣ Handle Missing Values

Replace empty values with blank strings.

### 4️⃣ Combine Features

Merge selected features into a single text column.

### 5️⃣ Text Vectorization

Convert text data into numerical vectors using:

```python
TfidfVectorizer()
```

### 6️⃣ Similarity Calculation

Calculate similarity between movies using:

```python
cosine_similarity()
```

### 7️⃣ User Input

User enters a favorite movie name.

Example:

```text
Avatar
```

### 8️⃣ Find Closest Match

Use:

```python
difflib.get_close_matches()
```

to handle spelling mistakes.

### 9️⃣ Generate Recommendations

Display the Top 20 most similar movies.

---

## 📊 Machine Learning Concepts Used

### TF-IDF Vectorization

TF-IDF converts movie text information into numerical vectors.

Benefits:

- Removes importance of common words
- Highlights unique movie characteristics
- Improves recommendation quality

### Cosine Similarity

Measures similarity between two movie vectors.

Value Range:

```text
0 → Completely Different
1 → Identical
```

---

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── movies.csv
├── movie.py
├── README.md
├── requirements.txt
│
└── screenshots/
```

---

## 📦 Installation

Install required libraries:

```bash
pip install numpy pandas scikit-learn
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
```

Move into the project directory:

```bash
cd movie-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python movie.py
```

---

## 💻 Example

### Input

```text
Enter your favourite movie name:
Avatar
```

### Output

```text
Movies Suggested For You:

1. Avatar: The Way of Water
2. Guardians of the Galaxy
3. Star Trek
4. John Carter
5. The Fifth Element
...
```

---

## 🔮 Future Improvements

- Web Application using Streamlit
- Movie Posters Integration
- TMDB API Integration
- User Rating System
- Hybrid Recommendation System
- Deep Learning Recommendations

---

## 📈 Applications

- Netflix-like recommendation systems
- OTT Platforms
- Entertainment Websites
- Personalized Content Recommendations

---

## 👨‍💻 Author

Developed as a Machine Learning project for movie recommendation and content personalization.

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.
