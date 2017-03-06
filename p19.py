MONTH_DAY_={9:30,4:30,6:30,11:30,2:28,1:31,3:31,5:31,7:31,8:31,10:31,12:31}



def leap_year(year):
    if (year%100==0):
        if(year%400==0):
            return True
    elif year%4==0:
        return True

    return False

def add_days(date,n):
    year=date[0]
    month=date[1]
    day = date[2] + n

    is_leapyear=(leap_year(year))
    
    if is_leapyear:
            MONTH_DAY={9:30,4:30,6:30,11:30,2:29,1:31,3:31,5:31,7:31,8:31,10:31,12:31}
    else:
            MONTH_DAY={9:30,4:30,6:30,11:30,2:28,1:31,3:31,5:31,7:31,8:31,10:31,12:31}
            
    while day>(MONTH_DAY[month]):
        is_leapyear=(leap_year(year))
        if is_leapyear:
            MONTH_DAY={9:30,4:30,6:30,11:30,2:29,1:31,3:31,5:31,7:31,8:31,10:31,12:31}
        else:
            MONTH_DAY={9:30,4:30,6:30,11:30,2:28,1:31,3:31,5:31,7:31,8:31,10:31,12:31}
            
        day = day-(MONTH_DAY[month])
        month +=1
        if month > 12:
            year += 1
            month=1
    return (year,month,day)

        

def all_sundays(end_date,start_date=(1901,1,6)):
    
    sundays=[(1901,1,6)] #this will only work for the default start_date
    
    while start_date <= end_date:
        start_date=add_days(start_date,7)
        sundays.append(start_date)

    return sundays
def start_month(a_list):
    sunday_month=[]
    for i in a_list:
        if i[2]==1:
            sunday_month.append(i)

    return len(sunday_month)

        
        
        
        
        
    
    
