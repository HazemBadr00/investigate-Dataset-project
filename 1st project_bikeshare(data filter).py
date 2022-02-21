import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']
days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','whole week']
months = ['january', 'february', 'march', 'april', 'may', 'june','all']


def get_filters():
    """
    demand the user to enter a city,day and month to analyze the data of files added as value in CITY_DATA directory
    the code Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('enter the city:').lower()
    while city not in cities:
        print('not valid city')
        city = input('please enter a valid city :').lower()
    print(city)
    # get user input for month (all, january, february, ... , june)
    month = input('enter the month:').lower()

    while month not in months:
        print('not a valid month')
        month = input('please enter valid month :').lower()
    print(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('enter the day:').lower()
    while day not in days:
        print('input is invalid')
        day = input('enter valid days :').lower()
    print(day)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # getting intger from string list by using index of items of list and adding 1
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe and insert it in df
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    month = df['month'].mode()
    print('The most common month is :',month) # display the most common month


    common_day=df['day_of_week'].mode()[0]
    print('the most common day of the week is :',common_day) # display the most common day of week



    df['hour']=df['Start Time'].dt.hour
    print('the most common working hour is:',df['hour'].mode()[0]) # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print('the most commonly start bike station:',common_start)


    # display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print('most commonly used arrived station:',common_end)


    # display most frequent combination of start station and end station trip
    common_trip=(df['Start Station']+df['End Station']).mode()[0]
    print('most common trip is :',common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total travel time taken :',total_travel_time)


    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('average travel time taken:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_type=df['User Type'].value_counts()
    print('city users type:',users_type)


    # Display counts of gender

    try:
        gender_count = df['Gender'].values_counts()
        print("city gender's count:",gender_count)
    except:
        print('no gender column in the file')




    # Display earliest, most recent, and most common year of birth
    early_birth=df['Birth Year'].min()
    recent_birth=df['Birth Year'].max()
    common_birth=df['Birth Year'].mode()
    print('earliest year of birth:',early_birth,)
    print('recent year of birth:',recent_birth)
    print('common year of birth:', common_birth)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    user_input=input('if you want 5 random data from the file type (yes) or (no): ').lower()
    while user_input=='yes':
        random_data=df.sample(5)
        print(random_data)
        user_input = input('if you want 5 random data from the file type (yes) or (no): ').lower()
    return random_data




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()



