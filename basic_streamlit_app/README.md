# 🎮 Video Game Sales Explorer

<p align="center">
  <img src="data/dawit-Fwr4wTBX9RU-unsplash.jpg" alt="Close-up of a video game controller" width="600">
</p>

## ⚡ At a glance

| 🎮 Game records | 📋 Data columns | 🌍 Sales regions |
| :---: | :---: | :---: |
| **16,598** | **11** | **5** |

I made this app to explore video game sales without scrolling through thousands of rows. Home narrows the table to one platform; Console Wars asks which platform leads in a selected year and region. Try changing just one choice at a time—the answer might change too.

## ▶️ Run the app

Open the repository in VS Code, then run this command in the VS Code terminal:

```bash
streamlit run basic_streamlit_app/main.py
```

## 🕹️ Choose your view

| 🔎 Home | 🏆 Console Wars |
| --- | --- |
| Browse the full game table, then filter it to one platform. Watch the game count update. | Pick a year and region. See the top ten platforms in a bar chart and ranking table, plus the leader for your selection. |

## 🎯 Try a match-up

1. **Start wide:** Open **Home** with **All Platforms** selected.
2. **Zoom in:** Choose a platform and see which games remain.
3. **Open Console Wars:** Pick a year, then switch the region without changing the year.

## 🏆 What “winner” means

Sales are recorded in millions of units. Console Wars adds game sales by platform for the selected year and region, then shows the ten largest totals. Here, “winner” means the leader in that view, not the best console ever, and not hardware sales.

<details>
<summary>📚 Curious about the data? Open the notes</summary>

- Each row represents a game. The columns include platform, release year, genre, publisher, and sales by region.
- Regions: **Global**, **North America**, **Europe**, **Japan**, and **Other Regions**.
- Some records have no year, so they cannot appear in a year-based comparison.
- Source: [Video Game Sales on Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales).

</details>

## 🚀 Next levels

- [x] Filter game records by platform.
- [x] Compare platform sales by year and region.
- [ ] Add a clearer genre comparison.
- [ ] Show regions side by side.

---

*Built with Python, Streamlit, and pandas as part of my data science portfolio.*
