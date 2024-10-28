Project4-FacuaAnalysis
![Portada](https://github.com/user-attachments/assets/c0260f21-3b70-4a12-9072-1be2d53f4852)

Welcome!
📝 What it consists of:
Welcome to a new project! This time we will scrape data from Facua to compare 6 supermarkets: Alcampo, Carrefour, Dia, Eroski, Hipercor, and Mercadona. We will focus on 3 categories: olive oil, sunflower oil, and milk.

Project Objectives:
Data Scraping: Extract detailed information on all products available on the FACUA website for each of the listed supermarkets.
Database Storage: Create a SQL database to store the collected information in a structured manner.
Data Analysis:
Price Comparison between Supermarkets
Price Evolution Analysis
Anomaly Detection
Price Dispersion Analysis
Average Price Comparison
Data Visualization
🗂️ Project Structure
We have created an environment called Webscraping for this project.

bash
Copiar código
        ├── notebooks/           # Jupyter Notebooks for data cleaning and visualization
        ├── src/                 # Processing and modeling scripts
        ├── Data                 # Folder containing the obtained CSV files
        ├── README.md            # Project description
        ├── README_English version.md   # Project description in English
🛠️ Installation and Requirements
This project uses Python 3.12.6. The following libraries have been imported:

BeautifulSoup
requests
pandas
numpy
webdriver
ChromeDriverManager
Keys
Select
WebDriverWait
expected_conditions as EC
NoSuchElementException
re
sys
os
📝 Websites:
Facua: https://super.facua.org/
Results and Conclusions

We analyzed 6 supermarkets and 3 product categories, obtaining a total of 135,869 data points.

The most offered product across all supermarkets is olive oil, with the Carbonel smooth olive oil being the most frequently listed.

Looking at each supermarket, the trend is consistent, showing that sunflower oil has the least offering.

Historically, milk predominates in all 6 supermarkets, surpassing olive oil. However, some supermarkets, like Hipercor, do not follow this pattern and have a historical predominance of olive oil.

Average Prices historically show:

Eroski as the most cost-effective for sunflower oil.
Hipercor as the most cost-effective for milk.
Dia as the most cost-effective for olive oil.
Maximum Prices historically reveal:

Carrefour as the standout for sunflower oil.
Carrefour also as the standout for milk.
Hipercor has almost double the maximum price of other supermarkets for olive oil.
Minimum Prices historically indicate:

Alcampo as the standout for sunflower oil.
Alcampo also as the standout for milk.
Carrefour as the standout for olive oil.
In terms of price evolution, we observe that prices fluctuate constantly, except for Carrefour, which experiences significant spikes.

Interestingly, Alcampo shows a sharp decline in minimum prices, possibly due to the increasing implementation of promotions like "everything for 1 euro."

Anomalies:

As noted, the most significant anomalies are seen with Carrefour, which on 01/09 raised the price of milk by 96%, then lowered it by 49% on 02/08, and increased it again by 228% on 08/08.

For sunflower oil, the most notable anomalies occur at Alcampo and Carrefour, where the maximum increase is 34% at Carrefour on 02/08, and the most significant drop is 25% at Carrefour on 01/09.

Regarding olive oil, anomalies are more constant, with sharp price fluctuations throughout the historical data; we should examine the graphs and tables.

Next Steps
📈 After fully scraping the provided website, the data collection took about 31 minutes, indicating a need to incorporate parallelism and asynchrony for future collections.

Additionally, we will add support functions for graph visualizations, keeping them separate from the Notebook.

Finally, our next step is to clean the brand-volume data for more in-depth analysis by product format, as this column was included in our analysis but has not yet been cleaned.

🏍️ 🌟

![OIP](https://github.com/user-attachments/assets/a3261f22-9193-45df-bf33-14a396dfd988)

