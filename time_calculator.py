def add_time(start, duration, *start_day):
  '''
  The function should add the duration time to the start time and return the result.
 
  Args:
    start(string) start time in the 12-hour clock format (ending in AM or PM)
    duration(string): duration time that indicates the number of hours and minutes
    start_day (string): (optional) a starting day of the week, case insensitive

  Raises:
    None - " Assume that the start times are valid times." -- Program requirements doc

  Returns:
    Formatted time and (optional) day of week
  '''

  #VARIABLES declared and assigned from input
  start_time, start_ampm = start.split()
  start_hour, start_minute = list(map(int, start_time.split(":")))

  dur_hour, dur_minute = list(map(int, duration.split(":")))
  
  start_day_formatted = ""
  days_later_text = ""
  new_time = ""
  days_later = 0
  add_hour_flag = False
  new_day_of_week = ""

  # Format the day of week for use in re-calc and proper output format
  if (start_day):
    start_day_formatted = str(start_day[0]).lower().capitalize()

  print("\nthe input and day of week is: ", start_hour, start_minute, start_ampm, start_day_formatted  )
  print("the duration is: ", dur_hour, dur_minute)

  if (dur_hour>12):
    number_of_12s_in_dur = int(dur_hour/12)
    print("number_of_12s_in_dur" + str(number_of_12s_in_dur))
    days_later = days_later + (number_of_12s_in_dur/2)
    if (number_of_12s_in_dur % 2 != 0):
      if(start_ampm=='PM'): 
        start_ampm="AM" 
      else: 
        start_ampm="PM"
    hours_to_add = dur_hour - (12*number_of_12s_in_dur)
  else:
    hours_to_add = dur_hour
    
  print("the hours_to_add is: ", hours_to_add)

  # get hours, if next day then add to days_later then reset flag for minutes calc
  new_hour, new_amap, next_day_flag = add_hour(start_hour,hours_to_add, start_ampm) 
  if (next_day_flag==True):
    days_later = days_later+1
  next_day_flag = False

  # Minutes caluclate 
  new_min, add_hour_flag = add_minutes(start_minute,dur_minute)
  if (add_hour_flag==True):
    new_hour, new_amap, next_day_flag = add_hour(new_hour,1, new_amap) 

  # If adding minutes results in next day, add day later
  if (next_day_flag==True):
    days_later = days_later+1
    
  # Day of Week placeholder
  new_day_of_week = start_day_formatted

  # Next / n days later string create 
  if (days_later>0):
    if(new_day_of_week != ""):
      new_day_of_week = calc_new_day_of_week(new_day_of_week,int(days_later))
    if (days_later==1):
      days_later_text = " (next day)"
    else:
      days_later_text = " (" + str(int(days_later)) + " days later)"
  
    
  #RETURN statments depending on input
  if (new_day_of_week != ""):
    new_time = str(new_hour) + ":" + f"{new_min:02}" + " " + str(new_amap) + ", " + new_day_of_week + days_later_text 
  #   new_time = str(new_hour) + ":" + f"{new_min:02}" + " " + str(new_amap) + start_day_formatted
  else:
    new_time = str(new_hour) + ":" + f"{new_min:02}" + " " + str(new_amap) + days_later_text 

  print("returning: ",new_time)
  return new_time

def add_hour(start_hour,hours_to_add, start_ampm):
  '''
  Adds hours based on 12 hour clock
  Args: start hour and duration hour to be added together
  Returns hours added together
  '''
  next_day_flag = False
  if (start_hour+hours_to_add>11):
    if(start_ampm=='PM'): 
      new_ampm="AM" 
      next_day_flag=True
    else: 
      new_ampm="PM"
    # Generate new hour on clock accounting for no zero values (instead should be 12)
    if(start_hour+hours_to_add==12):
      new_hours = 12
    else:
      new_hours = (start_hour+hours_to_add)-12
    return new_hours, new_ampm, next_day_flag
  else:
    return start_hour+hours_to_add, start_ampm, next_day_flag

def add_minutes(start_minute,dur_minute):
  if (start_minute+dur_minute<60):
    return start_minute+dur_minute, False
  else:
    return (start_minute+dur_minute)-60, True

def calc_new_day_of_week(day, days_past):
  '''
  Determine and return new day of week 
  Args: stat day of week (int),  number of days passed (int)
  Returns (string): day_of_week_list
  '''
  day_of_week_list = [
    "Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"
  ]

  #find index of day of week
  start_index = day_of_week_list.index(day)
  new_index = int()
  print("start_index: ", start_index, "dayspast: ", days_past )

  days_to_add = int()
  days_to_add = days_past%7
  new_index = days_to_add+start_index
  if(new_index>6):
    new_index = new_index%7
  
  
  return day_of_week_list[new_index] 