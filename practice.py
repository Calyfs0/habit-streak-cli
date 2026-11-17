habit_count = 0
while True:
    habit = input("Enter your habit? q to quit. ").strip()
    if not habit:
        continue
    elif habit.lower() == "q":
        print(f"You added {habit_count} habits.")
        break

    while True:
        days_done = input("Enter the number of days you did this habit? ").strip()
        if not days_done:
            print("Enter a valid value.")
            continue
        try:
            days_done = int(days_done)
            if days_done < 0:
                print("Days can't be negative!")
                continue
            if days_done >= 7:
                week = days_done // 7
                days = days_done % 7
                if days > 0:
                    print(
                        f"{habit}: {week} week(s) and {days} day(s) done, {days_done + 1} tomorrow."
                    )
                else:
                    print(f"{habit}: {week} week(s) done, {days_done + 1} tomorrow.")
            else:
                print(f"{habit}: {days_done} days done, {days_done + 1} tomorrow.")
            habit_count += 1
            break
        except ValueError:
            print("Please enter a numeric positive input!")
    print(f"Added: {habit}")
