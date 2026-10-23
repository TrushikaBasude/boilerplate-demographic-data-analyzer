
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read the data
    df = pd.read_csv('adult.data.csv')

    # How many people of each race?
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage with a Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # People with advanced education
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    # People without advanced education
    lower_education = ~higher_education

    # Percentage of advanced education earners making >50K
    higher_education_rich = round(
        (df.loc[higher_education, 'salary'] == '>50K').mean() * 100, 1
    )

    # Percentage of non-advanced education earners making >50K
    lower_education_rich = round(
        (df.loc[lower_education, 'salary'] == '>50K').mean() * 100, 1
    )

    # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # People who work the minimum number of hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # Percentage of minimum-hours workers earning >50K
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # Country with the highest percentage earning >50K
    country_earning = (
        df[df['salary'] == '>50K']['native-country'].value_counts()
        / df['native-country'].value_counts()
        * 100
    )

    highest_earning_country = country_earning.idxmax()
    highest_earning_country_percentage = round(country_earning.max(), 1)

    # Most popular occupation among people in India earning >50K
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degree:", percentage_bachelors)
        print("Higher education earning >50K:", higher_education_rich)
        print("Lower education earning >50K:", lower_education_rich)
        print("Minimum work hours:", min_work_hours)
        print("Rich percentage among minimum-hours workers:", rich_percentage)
        print("Country with highest earners:", highest_earning_country)
        print("Percentage of high earners in that country:",
              highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

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
