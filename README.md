# Historical National Population Trends

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-blueviolet.svg)](https://seaborn.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains a time-series analysis pipeline that examines long-term historical national population data to uncover demographic growth trends and annual percentage change over decades[cite: 18].

---

## Project Workflow
1. **Data Loading & Preprocessing**: Reading historical population records (`POPH.csv`), converting date strings to datetime objects, and sorting chronologically[cite: 18].
2. **Exploratory Data Analysis**: Inspecting data types, missing values, and structural summary[cite: 18].
3. **Feature Engineering**: Calculating annual population growth rates (`Population_Growth_Rate`) via percentage change[cite: 18].
4. **Visualization**: Plotting long-term national population growth and growth rates using Seaborn and Matplotlib[cite: 18].
5. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/historical-population-trends.git](https://github.com/YOUR_USERNAME/historical-population-trends.git)
   cd historical-population-trends
