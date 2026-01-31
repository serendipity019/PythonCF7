# Constants
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_A_HOUR = 3600
SECONDS_IN_A_DAY = 86400

# PROMPT
total_seconds = int(input("Enter the number of seconds: "))

# Calculations
days = total_seconds // SECONDS_IN_A_DAY
print(f"Days calculated: {days}")
days_wrong = total_seconds / SECONDS_IN_A_DAY
print(f"Days (wrong calculation using /): {days_wrong}")
seconds_remaining = total_seconds % SECONDS_IN_A_DAY
print(f"Seconds remaining after extracting days: {seconds_remaining}")
hours = seconds_remaining // SECONDS_IN_A_HOUR
seconds_remaining %= SECONDS_IN_A_HOUR

minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds = seconds_remaining % SECONDS_IN_A_MINUTE

# Output
print(f"{total_seconds} seconds is equivalent to: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")