def main():
    birthday = get_date_from_user('Enter your birthday: ')
    now = get_date_from_user('Enter the current date: ')

    age_in_days = (now - birthday).days
    years = age_in_days // 365
    months = (age_in_days % 365) // 30
    days = (age_in_days % 365) % 30
    print(f'You have lived {years} years, {months} months and {days} days')
    print(f'You have lived {years*12 + months} months')
    print(f'You have lived {age_in_days} days')

if __name__ == '__main__':
    from datetime import datetime

    def get_date_from_user(prompt):
        while True:
            try:
                date_str = input(prompt)
                return datetime.strptime(date_str, '%d/%m/%Y')
            except ValueError:
                print('Invalid date format. Please use DD/MM/YYYY')

    main()