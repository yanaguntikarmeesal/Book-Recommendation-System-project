# 📚 Book Hub – Book Recommendation System

 Link to open project = https://book-recommendation-system-project-viaoewilj4vuxvtgfa77in.streamlit.app/


> ✨ Discover your next favourite book based on popular reader choices.

A beautiful, interactive **Book Recommendation System** built with **Streamlit**, powered by the **Book-Crossing dataset**. Browse the top 50 trending books, explore ratings, and get personalized book recommendations — all in a sleek, modern UI.

---

## 🌟 Features

- 🏆 **Top 50 Trending Books** — Explore the most popular books from the Book-Crossing dataset
- ⭐ **Star Rating System** — Visual 5-star ratings converted from 10-point scores
- 🎯 **Book Recommendations** — Select any book and get similar recommendations
- 🎨 **Custom Gradient Banner** — Eye-catching animated header with shimmer effect
- 📱 **Responsive Layout** — Multi-column grid layout for book cards
- 🖼️ **Book Cover Images** — High-quality book thumbnails for each title
- 👥 **Rating Counts** — See how many readers have rated each book
- 🚫 **Clean UI** — Hidden Streamlit default header, footer, and menu

---

## 🖼️ Preview

> **Header Banner:** Animated gradient (Indigo → Purple → Pink) with a shimmer effect and the tagline _"📖 EXPLORE • ⭐ RATE • ❤️ DISCOVER"_

| Tab | Description |
|-----|-------------|
| 🏠 **Home** | Displays the top 50 trending books in a 5-column grid with cover, title, author, star rating, and number of ratings |
| 🔍 **Recommend** | Select any book from a dropdown and get 6 recommended books |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web application framework |
| **Pandas** | Data manipulation and analysis |
| **Pickle** | Loading pre-processed data |
| **HTML/CSS** | Custom styling and animations |

---

## 📁 Project Structure

```
book-hub/
│
├── app.py                  # Main Streamlit application
├── popular.pkl             # Pre-processed popular books data
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```

---

## 📊 Dataset

This project uses the **Book-Crossing Dataset** — one of the most popular publicly available book recommendation datasets.

- **Source:** [Book-Crossing Dataset (Kaggle)](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)
- **Contents:** 1.1M+ ratings, 270K+ books, 90K+ users
- **Fields used:** `Book-Title`, `Book-Author`, `Image-URL-M`, `avg_rating`, `num_ratings`

The `popular.pkl` file contains pre-filtered books with:
- Minimum **250 ratings** (to ensure reliability)
- Sorted by **average rating** (descending)
- Top 50 books selected for display

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.8+** installed on your system.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/book-hub.git
cd book-hub
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Or install manually:**

```bash
pip install streamlit pandas
```

### 4️⃣ Add the Data File

Place the `popular.pkl` file in the project root directory.

> 💡 **Don't have `popular.pkl`?** You can generate it using the Book-Crossing dataset with the script below.

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🧪 Generating `popular.pkl`

If you want to recreate the `popular.pkl` file from scratch, use this script:

```python
import pandas as pd
import pickle

# Load datasets
books = pd.read_csv("Books.csv")
ratings = pd.read_csv("Ratings.csv")

# Merge books with ratings
ratings_with_name = ratings.merge(books, on="ISBN")

# Filter: books with at least 250 ratings
num_rating_df = (
    ratings_with_name
    .groupby("Book-Title")
    .count()["Book-Rating"]
    .reset_index()
)
num_rating_df.rename(columns={"Book-Rating": "num_ratings"}, inplace=True)

# Calculate average rating
avg_rating_df = (
    ratings_with_name
    .groupby("Book-Title")
    .mean()["Book-Rating"]
    .reset_index()
)
avg_rating_df.rename(columns={"Book-Rating": "avg_rating"}, inplace=True)

# Combine
popular_df = num_rating_df.merge(avg_rating_df, on="Book-Title")
popular_df = popular_df[popular_df["num_ratings"] >= 250].sort_values(
    "avg_rating", ascending=False
)

# Merge book details
popular_df = popular_df.merge(books, on="Book-Title").drop_duplicates("Book-Title")[
    ["Book-Title", "Book-Author", "Image-URL-M", "num_ratings", "avg_rating"]
]

# Save
with open("popular.pkl", "wb") as f:
    pickle.dump(popular_df, f)

print(f"✅ Saved {len(popular_df)} popular books to popular.pkl")
```

---

## 🎨 Customization

### Change the Banner Colors

Edit the gradient in the `.bookhub-banner` CSS class:

```css
background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #EC4899 100%);
```

### Change Number of Books Displayed

In the Home tab, modify:

```python
total_books = min(50, len(popular_df))  # Change 50 to your desired count
cols_per_row = 5                        # Change grid columns
```

### Change Number of Recommendations

In the Recommend tab, modify:

```python
number_of_results = min(6, len(popular_df))  # Change 6 to your desired count
```

---

## 🔮 Future Enhancements

- [ ] 🤖 **Collaborative Filtering** — Implement user-based and item-based recommendations
- [ ] 🧠 **Content-Based Filtering** — Recommend books by genre, author, and description
- [ ] 🔍 **Search Bar** — Add fuzzy search for book titles
- [ ] 👤 **User Authentication** — Save favourite books per user
- [ ] 📊 **Analytics Dashboard** — Show reading trends and statistics
- [ ] 🌐 **Deploy to Streamlit Cloud** — One-click public deployment
- [ ] ⭐ **Interactive Ratings** — Let users rate books directly in the app

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Yanaguntikar Meesal**

- 📚 Passionate about Data Science & Machine Learning
- 💡 Building real-world projects with Python & Streamlit

---

## 🙏 Acknowledgements

- 📖 [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/) — For providing the dataset
- 🎨 [Streamlit](https://streamlit.io/) — For the amazing web framework
- 🐼 [Pandas](https://pandas.pydata.org/) — For powerful data manipulation

---

## ⭐ Show Your Support

If you found this project helpful, please give it a **⭐ star** on GitHub — it means a lot!

---

<div align="center">

**📚 Book Hub** • Designed & Developed with ❤️ by **Yanaguntikar Meesal**

`Python • Pandas • Streamlit • Book Recommendation System`

</div>
```

---

## 📝 Notes for You

**Replace these placeholders before pushing to GitHub:**

| Placeholder | Replace with |
|-------------|--------------|
| `your-username` | Your actual GitHub username |
| `book-hub` | Your actual repository name |

**Suggested repository name:** `book-hub-recommendation-system` or `book-recommendation-streamlit`

**Add a screenshot** of your app in the `Preview` section for better engagement — you can drag-and-drop an image into the README editor on GitHub and it'll auto-generate the markdown.

**Bonus:** Add a `requirements.txt` file with:
```
streamlit>=1.30.0
pandas>=2.0.0
```

This README is ready to copy-paste into your GitHub repo! 🚀

