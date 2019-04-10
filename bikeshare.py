import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some interesting US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            states = {'chicago': 'Illinois', 'new york city':'New York', 'washington':'District of Columbia'}
            city = input('Which city are you interested in? Choose between chicago, new york city, and washington: ')
            print('OK, let\'s explore a city in {}!'.format(states[city]))
            break
        except:
            print('Ups, you may choose only between three cities. Type in a valid one.')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month_num = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
            month = input('Which month are you interested in? Type in a month name (january / february / march / april / may / june) or "all" if you want to see the data for all months: ')
            if month == 'all':
                print('OK, let\'s look at the data for all months!')
                break
            else:
                print('Ok, let\'s see what happened in the month number {}!'.format(month_num[month]))
            break
        except:
            print('Ups, seems you entered an invalid month name. Type in a valid one.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            weekdays = {'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':7}
            day = input('Which day of week are you interested in? Type in a weekday name (monday / tuesday / wednesday / thursday / friday / saturday / sunday) or "all" if you want to see the data for all weekdays: ')
            if day == 'all':
                print('OK, let\'s look at the data for all days!')
                break
            else:
                print('Ok, let\'s see what happened in the day number {}!'.format(weekdays[day]))
                break
        except:
            print('Ups, seems you entered an invalid weekday name. Type in a valid one.')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    # Display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    
    print('Most Frequent Month:', popular_month)
    print('Most Frequent Day of Week:', popular_day_of_week)
    print('Most Frequent Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('Most Frequent Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds:', total_travel_time)

    #Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time in seconds:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types: ", user_types)

    #Display counts of gender
    
    try:
        gender_types = df['Gender'].value_counts()
        print("Genders: ", gender_types)
    except:
        print("There is no data on Genders.")

    #Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("The earliest birth year was {}, the most recent was {} and the most common - {}.".format(earliest_birth_year, recent_birth_year, common_birth_year))
            
    except:
        print("There is no data on Birth Year.")
            
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
		if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
