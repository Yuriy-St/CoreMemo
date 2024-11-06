from datetime import datetime, timedelta


def get_upcoming_birthdays(self, days):
    current_date = datetime.today().date()
    upcoming_birthdays = []

    for record in self.data.values():  
        if record.birthday:  
            birthday_this_year = record.birthday.date.replace(year=current_date.year)  

            # Якщо день народження вже пройшов, беремо наступний рік  
            if birthday_this_year < current_date:  
                birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)  

            # Різниця в днях між поточною датою і днем народження  
            difference_days = (birthday_this_year - current_date).days  
            
            # Ініціюємо congratulation_date  
            congratulation_date = None  

            # Якщо день народження на наступному тижні (включаючи сьогодні)  
            if 0 <= difference_days <= days:  
                congratulation_date = birthday_this_year  

                # Якщо день народження випадає на вихідні (субота або неділя)  
                if congratulation_date.weekday() == 5:  # Субота  
                    congratulation_date += timedelta(days=2)  
                elif congratulation_date.weekday() == 6:  # Неділя  
                    congratulation_date += timedelta(days=1)  

                # Додаємо до списку тільки якщо congratulation_date було встановлено   
                upcoming_birthdays.append((record.name.value, congratulation_date.strftime("%d.%m.%Y"))) 
                # print(f'upcoming_birthdays{upcoming_birthdays}')
                
    # print (f"апкаминг{upcoming_birthdays}") 
    return upcoming_birthdays
