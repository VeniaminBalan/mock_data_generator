import csv
import random
import faker
import sys
import time
from datetime import datetime

def print_progress_bar(iteration, total, rate, length=30, fill='█', prefix='Progress:'):
    """Print a custom progress bar that stays on one line"""
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% ({rate:.0f} rows/s)'.ljust(80), end='')
    if iteration == total:
        print()  # Print a new line on completion

def generate_mock_data(rows=100_000):
    fake = faker.Faker()
    # Generate filename with row count if not provided
    filename = f"mock_data_{rows}_rows.csv"
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Header
        writer.writerow([
            "id", "name", "email", "age", "country", "city", "address", 
            "phone", "company", "job_title", "salary", "registration_date", 
            "last_login", "status", "gender", "birth_date", "credit_card",
            "website", "department", "experience_years"
        ])
        
        # Status options
        status_options = ["active", "inactive", "pending", "suspended"]
        gender_options = ["Male", "Female", "Other", "Prefer not to say"]
        departments = ["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations", "Legal", "Support"]
        
        # Generate rows
        start_time = time.time()
        for i in range(1, rows + 1):
            # Update progress bar every 100 rows or on the last row
            if i % 100 == 0 or i == rows:
                elapsed_time = time.time() - start_time
                if i > 0:
                    rate = i / elapsed_time
                    print_progress_bar(i, rows, rate, prefix='Generating rows:')
            
            registration_date = fake.date_between(start_date="-5y", end_date="today")
            birth_date = fake.date_between(start_date="-80y", end_date="-18y")
            age = (datetime.now().date() - birth_date).days // 365
            
            writer.writerow([
                i,
                fake.name(),
                fake.email(),
                age,
                fake.country(),
                fake.city(),
                fake.address().replace('\n', ', '),
                fake.phone_number(),
                fake.company(),
                fake.job(),
                random.randint(30000, 150000),
                registration_date.strftime("%Y-%m-%d"),
                fake.date_time_between(start_date=registration_date, end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
                random.choice(status_options),
                random.choice(gender_options),
                birth_date.strftime("%Y-%m-%d"),
                fake.credit_card_number(),
                fake.url(),
                random.choice(departments),
                random.randint(0, 40)
            ])
    
    return filename

if __name__ == "__main__":
    # Get number of rows from command line argument or ask user
    if len(sys.argv) > 1:
        try:
            rows = int(sys.argv[1])
            if rows <= 0:
                print("❌ Number of rows must be a positive integer")
                sys.exit(1)
        except ValueError:
            print("❌ Invalid number format. Please provide a valid integer.")
            sys.exit(1)
    else:
        while True:
            try:
                rows = int(input("Enter the number of rows to generate: "))
                if rows <= 0:
                    print("❌ Please enter a positive integer")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid integer")
                continue
    
    print(f"🚀 Starting generation of {rows:,} rows of mock data...")
    filename = generate_mock_data(rows)
    print(f"✅ Mock data CSV with {rows:,} rows generated successfully as '{filename}'!")
