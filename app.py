# ==============================================================
# 📚 BOOK HUB - BOOK RECOMMENDATION SYSTEM
# ==============================================================

# ==============================================================
# IMPORT LIBRARIES
# ==============================================================

import streamlit as st
import pickle
import pandas as pd


# ==============================================================
# PAGE CONFIGURATION
# ==============================================================

st.set_page_config(
    page_title="Book Hub",
    page_icon="📚",
    layout="wide"
)


# ==============================================================
# LOAD POPULAR BOOK DATA
# ==============================================================

@st.cache_data
def load_data():
    with open("popular.pkl", "rb") as file:
        return pickle.load(file)


popular_df = load_data()


# ==============================================================
# STAR RATING FUNCTION
# ==============================================================

def create_star_rating(rating):

    rating = float(rating)

    # Convert 10-point rating to 5-star rating
    star_rating = rating / 2

    # Round to nearest star
    full_stars = round(star_rating)

    # Keep value between 0 and 5
    full_stars = max(0, min(5, full_stars))

    empty_stars = 5 - full_stars

    stars = (
        "⭐" * full_stars
        + "☆" * empty_stars
    )

    return stars


# ==============================================================
# 🎨 CUSTOM CSS (Header Banner + Hidden HTML Tags)
# ==============================================================

st.markdown(
    """
    <style>

    /* =========================================================
       MAIN PAGE
       ========================================================= */

    .main {
        padding-top: 0rem;
    }

    /* =========================================================
       HIDE STREAMLIT'S DEFAULT HEADER & FOOTER
       ========================================================= */

    header[data-testid="stHeader"] {
        display: none !important;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* =========================================================
       HEADER BANNER
       ========================================================= */

    .bookhub-banner {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #EC4899 100%);
        padding: 45px 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.35);
        position: relative;
        overflow: hidden;
    }

    .bookhub-banner::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 60%);
        animation: shimmer 6s infinite linear;
    }

    @keyframes shimmer {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .bookhub-banner h1 {
        color: #ffffff !important;
        font-size: 44px !important;
        font-weight: 900 !important;
        margin: 0;
        padding: 0;
        letter-spacing: 1px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.25);
        position: relative;
        z-index: 2;
    }

    .bookhub-banner p {
        color: #f0f0ff !important;
        font-size: 17px !important;
        margin-top: 12px;
        margin-bottom: 0;
        font-weight: 500;
        position: relative;
        z-index: 2;
    }

    .bookhub-banner .tagline {
        color: #ffffff !important;
        font-size: 13px !important;
        letter-spacing: 3px;
        margin-top: 15px;
        font-weight: 600;
        opacity: 0.9;
        position: relative;
        z-index: 2;
    }


    /* =========================================================
       BUTTON
       ========================================================= */

    .stButton > button {

        background:
            linear-gradient(
                135deg,
                #4F46E5,
                #7C3AED
            ) !important;

        color: white !important;

        border: none !important;

        border-radius: 14px !important;

        min-height: 50px;

        font-size: 16px !important;

        font-weight: 700 !important;

        box-shadow:
            0 5px 15px
            rgba(79, 70, 229, 0.25);

        transition: 0.3s ease;
    }


    .stButton > button:hover {

        transform: translateY(-3px);

        box-shadow:
            0 8px 20px
            rgba(79, 70, 229, 0.40);
    }


    /* =========================================================
       TABS
       ========================================================= */

    button[data-baseweb="tab"] {

        font-size: 17px !important;

        font-weight: 700 !important;
    }


    /* =========================================================
       SELECT BOX
       ========================================================= */

    div[data-baseweb="select"] > div {

        border-radius: 12px;

        border: 2px solid #E2E8F0;
    }


    /* =========================================================
       IMAGE
       ========================================================= */

    [data-testid="stImage"] img {

        border-radius: 12px;

        object-fit: cover;
    }


    /* =========================================================
       DIVIDER
       ========================================================= */

    hr {

        margin-top: 30px;

        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==============================================================
# 📚 BOOK HUB HEADER BANNER
# ==============================================================
#
# The HTML tags are rendered visually (not displayed as text)
# because we use unsafe_allow_html=True in st.markdown.
#
# ==============================================================

st.markdown(
    """
    <div class="bookhub-banner">
        <h1>📚 BOOK RECOMMENDATION SYSTEM</h1>
        <p>✨ Discover your next favourite book based on popular reader choices.</p>
        <div class="tagline">📖 EXPLORE &nbsp;•&nbsp; ⭐ RATE &nbsp;•&nbsp; ❤️ DISCOVER</div>
    </div>
    """,
    unsafe_allow_html=True
)


# ==============================================================
# TABS
# ==============================================================

tab1, tab2 = st.tabs(
    [
        "🏠 Home",
        "🔍 Recommend"
    ]
)


# ==============================================================
# TAB 1 - HOME
# ==============================================================

with tab1:

    st.header(
        "🏆 Top 50 Trending Books"
    )

    st.caption(
        "Explore the most popular books "
        "from the Book-Crossing dataset."
    )

    total_books = min(
        50,
        len(popular_df)
    )

    cols_per_row = 5

    for start in range(
        0,
        total_books,
        cols_per_row
    ):

        cols = st.columns(
            cols_per_row
        )

        batch = popular_df.iloc[
            start:start + cols_per_row
        ]

        for col, (_, row) in zip(
            cols,
            batch.iterrows()
        ):

            with col:

                with st.container(
                    border=True
                ):

                    # ------------------------------------------------
                    # BOOK IMAGE
                    # ------------------------------------------------

                    image_url = row[
                        "Image-URL-M"
                    ]

                    if pd.notna(image_url):

                        st.image(
                            image_url,
                            use_container_width=True
                        )

                    else:

                        st.write("📕")


                    # ------------------------------------------------
                    # BOOK TITLE
                    # ------------------------------------------------

                    title = str(
                        row["Book-Title"]
                    )

                    if len(title) > 55:

                        title = (
                            title[:55]
                            + "..."
                        )

                    st.markdown(
                        f"**{title}**"
                    )


                    # ------------------------------------------------
                    # AUTHOR
                    # ------------------------------------------------

                    author = str(
                        row["Book-Author"]
                    )

                    st.caption(
                        f"✍️ {author}"
                    )


                    # ------------------------------------------------
                    # RATING
                    # ------------------------------------------------

                    rating = float(
                        row["avg_rating"]
                    )

                    stars = create_star_rating(
                        rating
                    )

                    st.write(
                        stars
                    )

                    st.write(
                        f"⭐ {rating:.2f} / 10"
                    )


                    # ------------------------------------------------
                    # NUMBER OF RATINGS
                    # ------------------------------------------------

                    st.caption(
                        f"👥 {int(row['num_ratings']):,} ratings"
                    )


# ==============================================================
# TAB 2 - RECOMMEND
# ==============================================================

with tab2:

    st.header(
        "🎯 Get Book Recommendations"
    )

    st.caption(
        "Choose a book and discover "
        "more books to read."
    )


    # --------------------------------------------------------------
    # BOOK LIST
    # --------------------------------------------------------------

    book_list = (
        popular_df["Book-Title"]
        .dropna()
        .unique()
        .tolist()
    )


    # --------------------------------------------------------------
    # SELECT BOOK
    # --------------------------------------------------------------

    selected_book = st.selectbox(

        "📖 Search or select a book",

        book_list,

        index=None,

        placeholder="Type or select a book..."
    )


    # --------------------------------------------------------------
    # RECOMMENDATION BUTTON
    # --------------------------------------------------------------

    if st.button(
        "🔮 Get Recommendations",
        use_container_width=True
    ):

        if selected_book:

            st.subheader(
                "📚 Recommended Books"
            )

            st.write(
                f"Books selected for fans of "
                f"**{selected_book}**"
            )


            # ------------------------------------------------------
            # TEMPORARY RECOMMENDATIONS
            # ------------------------------------------------------

            number_of_results = min(
                6,
                len(popular_df)
            )

            sample_results = popular_df.sample(
                number_of_results
            )


            res_cols = st.columns(
                number_of_results
            )


            for col, (_, row) in zip(
                res_cols,
                sample_results.iterrows()
            ):

                with col:

                    with st.container(
                        border=True
                    ):

                        # ------------------------------------------
                        # IMAGE
                        # ------------------------------------------

                        image_url = row[
                            "Image-URL-M"
                        ]

                        if pd.notna(image_url):

                            st.image(
                                image_url,
                                use_container_width=True
                            )

                        else:

                            st.write("📕")


                        # ------------------------------------------
                        # TITLE
                        # ------------------------------------------

                        title = str(
                            row["Book-Title"]
                        )

                        if len(title) > 45:

                            title = (
                                title[:45]
                                + "..."
                            )

                        st.markdown(
                            f"**{title}**"
                        )


                        # ------------------------------------------
                        # AUTHOR
                        # ------------------------------------------

                        st.caption(
                            f"✍️ {row['Book-Author']}"
                        )


                        # ------------------------------------------
                        # RATING
                        # ------------------------------------------

                        rating = float(
                            row["avg_rating"]
                        )

                        stars = create_star_rating(
                            rating
                        )

                        st.write(
                            stars
                        )

                        st.caption(
                            f"⭐ {rating:.2f} / 10"
                        )

        else:

            st.warning(
                "⚠️ Please select a book first!"
            )


# ==============================================================
# FOOTER
# ==============================================================

st.divider()

st.caption(
    "📚 Book Hub • Designed & Developed with ❤️ "
    "by Yanaguntikar Meesal"
)

st.caption(
    "Python • Pandas • Streamlit • "
    "Book Recommendation System"
)