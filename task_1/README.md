# Task 1: Data Cleaning - Netflix Dataset

## Dataset:
Netflix Movies and TV Shows - [Kaggle Link](https://www.kaggle.com/datasets/shivamb/netflix-shows)

## Tools Used:
- Python
- Pandas
- VS Code

## Data Cleaning Steps:
- Handled missing values:
  - Filled `rating` with "Not Rated"
  - Filled `country` with "unknown"
  - Dropped rows with missing `director`
- Removed duplicate records
- Standardized `country` column (lowercase, trimmed)
- Converted `date_added` to `datetime`
- Renamed all columns to lowercase with underscores
- Exported cleaned dataset to `netflix_cleaned.csv`

## Output:
- Cleaned CSV file: `netflix_cleaned.csv`
