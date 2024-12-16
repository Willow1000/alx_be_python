task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case if(priority == 'high' and time_bound == 'yes'):
        print(f"'{task}' is a high priority task that requires immediate attention today!")
    case if(priority == 'low' and time_bound == 'no'):    
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case if(priority == 'medium' and time_bound == 'yes'):
        print(f"'{task}' is a medium priority task that requires immediate attention today!")   
    case if(priority == 'high' and time_bound == 'no'):
        print(f"'{task}' is medium priority task. Consider completing it during your free time.")    
    case if(priority == 'high' and time_bound == 'no'):  
        print(f"'{task}' is a high priority. Consider completing it as soon as you get time.")   
    case if(priority == 'low' and time_bound == 'yes'): 
        print(f"'{task}' is low priority task. Consider completing it after all your urgrnt tasks today!")   