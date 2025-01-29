import requests
import json
from statistics import mean
from collections import defaultdict
from datetime import datetime

# List of US state and territory codes to be analyzed.
state_codes = [
    "al",
    "ar",
    "as",
    "az",
    "ca",
    "co",
    "ct",
    "dc",
    "de",
    "fl",
    "ga",
    "gu",
    "hi",
    "ia",
    "id",
    "il",
    "in",
    "ks",
    "ky",
    "la",
    "ma",
    "md",
    "me",
    "mi",
    "mn",
    "mo",
    "mp",
    "ms",
    "mt",
    "nc",
    "nd",
    "ne",
    "nh",
    "nj",
    "nm",
    "nv",
    "ny",
    "oh",
    "ok",
    "or",
    "pa",
    "pr",
    "ri",
    "sc",
    "sd",
    "tn",
    "tx",
    "ut",
    "va",
    "vi",
    "vt",
    "wa",
    "wi",
    "wv",
    "wy",
]

# Base URL for fetching COVID data from the tracking API.
base_url = "https://api.covidtracking.com/v1/states"


def fetch_and_save_state_data(state_code):
    """
    Fetches COVID data for a given state code and saves it as a JSON file.

    Args:
        state_code (str): The state code to fetch data for.

    Returns:
        list: A list of dictionaries containing daily COVID data for the state.
    """
    # Construct the URL to fetch daily data for the specified state.
    url = f"{base_url}/{state_code}/daily.json"
    response = requests.get(url)
    data = response.json()

    # Save the fetched data to a JSON file named after the state code.
    with open(f"{state_code}.json", "w") as f:
        json.dump(data, f)

    return data


def analyze_data(data):
    """
    Analyzes the fetched COVID data for key statistics.

    Args:
        data (list): The COVID data to analyze.

    Returns:
        dict: A dictionary containing various calculated statistics.
    """
    # Extract positive case increases and calculate average and max values.
    positive_increases = [
        day["positiveIncrease"] for day in data if day["positiveIncrease"] is not None
    ]
    average_daily_cases = mean(positive_increases) if positive_increases else 0
    max_daily_cases = max(positive_increases) if positive_increases else 0
    max_daily_cases_date = (
        data[positive_increases.index(max_daily_cases)]["date"]
        if positive_increases
        else None
    )
    recent_no_case_date = next(
        (day["date"] for day in data if day["positiveIncrease"] == 0), None
    )

    # Aggregate cases by month to identify the month with highest and lowest cases.
    monthly_cases = defaultdict(int)
    for day in data:
        if day["positiveIncrease"] is not None:
            month = str(day["date"])[:6]
            monthly_cases[month] += day["positiveIncrease"]

    highest_month = max(monthly_cases, key=monthly_cases.get) if monthly_cases else None
    lowest_month = min(monthly_cases, key=monthly_cases.get) if monthly_cases else None

    # Return a dictionary of the analyzed results.
    return {
        "average_daily_cases": average_daily_cases,
        "max_daily_cases": max_daily_cases,
        "max_daily_cases_date": max_daily_cases_date,
        "recent_no_case_date": recent_no_case_date,
        "highest_month": highest_month,
        "lowest_month": lowest_month,
    }


# Loop through each state code, fetch its data, analyze it, and print the results.
for state_code in state_codes:
    data = fetch_and_save_state_data(state_code)
    analysis = analyze_data(data)
    print(f"{state_code.upper()}: {analysis}")
