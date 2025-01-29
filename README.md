# COVID-19 Data Analysis Using Web JSON APIs

## Overview
This project analyzes COVID-19 case data for all **50 US states** and **5 US territories** using the publicly available [COVID Tracking Project API](https://covidtracking.com). The program fetches daily case data for each region, processes it, and calculates key statistical insights.

## Features

### Data Collection
- **Real-time API Calls**: Fetches daily COVID-19 data for each US state and territory.
- **JSON Data Storage**: Saves fetched data into individual JSON files (`<state>.json`).

### Data Analysis
- **Average Daily Cases**: Computes the average number of new daily confirmed cases.
- **Peak Case Date**: Identifies the date with the highest number of new cases.
- **Recent No-Case Date**: Finds the most recent date when no new cases were reported.
- **Monthly Case Trends**:
  - Determines the **month with the highest** new COVID cases.
  - Determines the **month with the lowest** new COVID cases.

## API Usage
The program retrieves data using API endpoints structured as follows:
```plaintext
https://api.covidtracking.com/v1/states/{state_code}/daily.json
```
where `{state_code}` represents the two-letter abbreviation of a US state or territory (e.g., `ut` for Utah).

## Program Structure
- **`covid.py`**: Main script that handles data fetching, storage, and analysis.
- **State JSON Files**: Each state’s COVID data is stored in a corresponding JSON file (e.g., `ca.json`, `tx.json`).

## Data Processing Flow
1. **Fetch Data**: Retrieve daily COVID statistics from the API.
2. **Save to JSON**: Store the raw data into JSON files.
3. **Analyze Data**:
   - Extract key statistics for each state.
   - Compute averages and identify key trends.
4. **Output Results**: Print analysis results to the console.

## Example Output
```
NY: {
    "average_daily_cases": 5000.4,
    "max_daily_cases": 15500,
    "max_daily_cases_date": "20210110",
    "recent_no_case_date": "20200415",
    "highest_month": "202012",
    "lowest_month": "202006"
}
TX: {
    "average_daily_cases": 3500.2,
    "max_daily_cases": 12000,
    "max_daily_cases_date": "20200820",
    "recent_no_case_date": "20200410",
    "highest_month": "202007",
    "lowest_month": "202005"
}
```

## Future Enhancements
- **Visualizations**: Generate charts and graphs for better data insights.
- **Automated Data Updates**: Schedule periodic API calls for real-time monitoring.
- **Advanced Analytics**: Include hospitalization and recovery trends.

---

_Developed as an example of web API integrations and data analysis in Python._

