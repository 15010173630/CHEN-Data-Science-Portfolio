import streamlit as st
import pandas as pd

# Load the Video Game Sales dataset from data folder.
df = pd.read_csv("data/vgsales.csv")

# Create sidebar navigation for the app.
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "Console Wars"])
                                            #"Global Gaming Tastes", "隐藏游戏发现"

if page == "Home":
    # Welcome section for the Home page.
    st.title("🎮 Video Game Sales Explorer")
    st.write("Welcome! This interactive app explores video game sales across different platforms, genres, publishers, and regions.")


    # Show a quick overview of the dataset.
    st.subheader("Dataset at a glance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Game Records", value=f"{len(df)}")
    col2.metric(label="Platforms", value=df["Platform"].nunique())
    col3.metric(label="Genres", value=df["Genre"].nunique())
    col4.metric(label="Publishers", value=df["Publisher"].nunique())

    st.caption("The dataset contains video game releases and their sales in North America, Europe, Japan, other regions, and worldwide.")
    st.markdown("***")
    st.image("data/dawit-Fwr4wTBX9RU-unsplash.jpg")
    st.markdown("***")

    # Interactive dataset section.
    st.subheader("Explore the Dataset")
    st.write("Select a platform to view its video game sales records.")

    # Let the user view every platform or select one platform.
    platforms = ["All Platforms"] + df["Platform"].unique().tolist()
    selected_platform = st.selectbox("Select a platform:", platforms)

    # Filter the DataFrame according to the user's selection.
    if selected_platform == "All Platforms":
        filtered_df = df
    else:
        filtered_df = df[df["Platform"] == selected_platform]

    # Create an interactive DataFrame.
    st.subheader("Filtered Results")
    st.write(f"Number of games found: {len(filtered_df)}")
    st.dataframe(filtered_df)

elif page == "Console Wars":
    st.title("🎮 Console Wars")
    st.write("Compare video game platforms by sales region and year.")

    # Give names for each sales region in the dataset.
    regions = {
        "Global": "Global_Sales",
        "North America": "NA_Sales",
        "Europe": "EU_Sales",
        "Japan": "JP_Sales",
        "Other Regions": "Other_Sales",
    }

    # Let the user choose a sales region.
    selected_region = st.selectbox("Select a sales region:", regions.keys())

    sales_column = regions[selected_region]

    # Let the user select one year to compare.
    selected_year = st.slider("Select a year:", min_value=1980, max_value=2020)

    # Keep only games released during the selected year.
    console_data = df[df["Year"] == selected_year]

    # Find the ten platforms with the highest sales.
    platform_sales = console_data.groupby("Platform")[sales_column].sum()
    platform_sales = platform_sales[platform_sales > 0]
    platform_sales = platform_sales.sort_values(ascending=False)
    platform_sales = platform_sales.head(10)

    if len(platform_sales) > 0:
        winning_platform = platform_sales.index[0]
        winning_sales = platform_sales.iloc[0]

        st.subheader("🏆 Console War Winner")
        st.success(f"{winning_platform} wins in {selected_region} at {selected_year}!")

        winner_column, sales_column_display = st.columns(2)
        winner_column.metric(label="Winning Platform", value=winning_platform)
        sales_column_display.metric(label="Total Sales", value=f"{winning_sales:.2f} million")

        st.subheader(f"Top 10 Platforms in {selected_region}")
        st.bar_chart(platform_sales)

        st.subheader("Platform Sales Ranking")
        st.dataframe(platform_sales)
    else:
        st.write("No sales data is available for this region and year.")

#elif page == "Global Gaming Tastes":
    #st.title("Global Gaming Tastes")

# elif page == "隐藏游戏发现":
    #st.title("隐藏游戏发现")
