import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # Count of each race
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df["education"].value_counts().get("Bachelors", 0) / len(df)) * 100, 1)

    # Filtering higher and lower education
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # Percentage earning >50K based on education level
    higher_education_rich = round((higher_education[higher_education["salary"] == ">50K"].shape[0] / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round((lower_education[lower_education["salary"] == ">50K"].shape[0] / lower_education.shape[0]) * 100, 1)

    # Minimum work hours per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of rich among those who work the minimum hours
    num_min_worker = df[df["hours-per-week"] == min_work_hours].shape[0]
    num_min_workers_above_50k = df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0]
    rich_percentage = round((num_min_workers_above_50k / num_min_worker) * 100, 1) if num_min_worker > 0 else 0

    # Country with the highest percentage of people earning >50K
    country_salary_counts = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_counts = df["native-country"].value_counts()
    country_rich_percentage = round((country_salary_counts / country_counts) * 100, 1)
    
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = country_rich_percentage.max()

    # Most popular occupation in India among rich people
    top_IN_occupation = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].mode()[0]

    # Print the results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Run the function
calculate_demographic_data()
