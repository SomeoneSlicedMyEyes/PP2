from datetime import datetime, timedelta

current_date = datetime.now()
subsctracted = current_date - timedelta(days=5)

print("Current:", current_date.strftime("%Y-%m-%d"))
print("Substracted:", subsctracted.strftime("%Y-%m-%d"))
