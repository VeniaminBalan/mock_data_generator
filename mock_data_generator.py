import csv
import random
import faker
import sys
import time
from datetime import datetime
from typing import List, Dict, Callable

def print_progress_bar(iteration, total, rate, length=30, fill='█', prefix='Progress:'):
    """Print a custom progress bar that stays on one line"""
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% ({rate:.0f} rows/s)'.ljust(80), end='')
    if iteration == total:
        print()  # Print a new line on completion

def get_column_types():
    """Define all available column types with their generators"""
    fake = faker.Faker()
    
    column_types = {
        "id": {
            "name": "ID (Auto-increment)",
            "generator": lambda i: i,
            "header": "id"
        },
        "name": {
            "name": "Full Name",
            "generator": lambda i: fake.name(),
            "header": "name"
        },
        "first_name": {
            "name": "First Name",
            "generator": lambda i: fake.first_name(),
            "header": "first_name"
        },
        "last_name": {
            "name": "Last Name",
            "generator": lambda i: fake.last_name(),
            "header": "last_name"
        },
        "email": {
            "name": "Email Address",
            "generator": lambda i: fake.email(),
            "header": "email"
        },
        "username": {
            "name": "Username",
            "generator": lambda i: fake.user_name(),
            "header": "username"
        },
        "password": {
            "name": "Password",
            "generator": lambda i: fake.password(),
            "header": "password"
        },
        "age": {
            "name": "Age",
            "generator": lambda i: random.randint(18, 80),
            "header": "age"
        },
        "birth_date": {
            "name": "Birth Date",
            "generator": lambda i: fake.date_between(start_date="-80y", end_date="-18y").strftime("%Y-%m-%d"),
            "header": "birth_date"
        },
        "gender": {
            "name": "Gender",
            "generator": lambda i: random.choice(["Male", "Female", "Other", "Prefer not to say"]),
            "header": "gender"
        },
        "phone": {
            "name": "Phone Number",
            "generator": lambda i: fake.phone_number(),
            "header": "phone"
        },
        "mobile": {
            "name": "Mobile Number",
            "generator": lambda i: fake.phone_number(),
            "header": "mobile"
        },
        "address": {
            "name": "Full Address",
            "generator": lambda i: fake.address().replace('\n', ', '),
            "header": "address"
        },
        "street": {
            "name": "Street Address",
            "generator": lambda i: fake.street_address(),
            "header": "street"
        },
        "city": {
            "name": "City",
            "generator": lambda i: fake.city(),
            "header": "city"
        },
        "state": {
            "name": "State/Province",
            "generator": lambda i: fake.state(),
            "header": "state"
        },
        "country": {
            "name": "Country",
            "generator": lambda i: fake.country(),
            "header": "country"
        },
        "postal_code": {
            "name": "Postal/ZIP Code",
            "generator": lambda i: fake.postcode(),
            "header": "postal_code"
        },
        "company": {
            "name": "Company Name",
            "generator": lambda i: fake.company(),
            "header": "company"
        },
        "job_title": {
            "name": "Job Title",
            "generator": lambda i: fake.job(),
            "header": "job_title"
        },
        "department": {
            "name": "Department",
            "generator": lambda i: random.choice(["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations", "Legal", "Support", "IT", "Research"]),
            "header": "department"
        },
        "salary": {
            "name": "Salary",
            "generator": lambda i: random.randint(30000, 200000),
            "header": "salary"
        },
        "experience_years": {
            "name": "Years of Experience",
            "generator": lambda i: random.randint(0, 40),
            "header": "experience_years"
        },
        "credit_card": {
            "name": "Credit Card Number",
            "generator": lambda i: fake.credit_card_number(),
            "header": "credit_card"
        },
        "iban": {
            "name": "IBAN",
            "generator": lambda i: fake.iban(),
            "header": "iban"
        },
        "website": {
            "name": "Website URL",
            "generator": lambda i: fake.url(),
            "header": "website"
        },
        "ipv4": {
            "name": "IPv4 Address",
            "generator": lambda i: fake.ipv4(),
            "header": "ipv4"
        },
        "ipv6": {
            "name": "IPv6 Address",
            "generator": lambda i: fake.ipv6(),
            "header": "ipv6"
        },
        "mac_address": {
            "name": "MAC Address",
            "generator": lambda i: fake.mac_address(),
            "header": "mac_address"
        },
        "registration_date": {
            "name": "Registration Date",
            "generator": lambda i: fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d"),
            "header": "registration_date"
        },
        "last_login": {
            "name": "Last Login",
            "generator": lambda i: fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
            "header": "last_login"
        },
        "status": {
            "name": "Status",
            "generator": lambda i: random.choice(["active", "inactive", "pending", "suspended", "verified"]),
            "header": "status"
        },
        "priority": {
            "name": "Priority Level",
            "generator": lambda i: random.choice(["low", "medium", "high", "critical"]),
            "header": "priority"
        },
        "score": {
            "name": "Score (0-100)",
            "generator": lambda i: random.randint(0, 100),
            "header": "score"
        },
        "rating": {
            "name": "Rating (1-5)",
            "generator": lambda i: round(random.uniform(1.0, 5.0), 1),
            "header": "rating"
        },
        "price": {
            "name": "Price",
            "generator": lambda i: round(random.uniform(10.0, 1000.0), 2),
            "header": "price"
        },
        "quantity": {
            "name": "Quantity",
            "generator": lambda i: random.randint(1, 1000),
            "header": "quantity"
        },
        "boolean": {
            "name": "Boolean (True/False)",
            "generator": lambda i: random.choice([True, False]),
            "header": "boolean"
        },
        "color": {
            "name": "Color Name",
            "generator": lambda i: fake.color_name(),
            "header": "color"
        },
        "hex_color": {
            "name": "Hex Color Code",
            "generator": lambda i: fake.hex_color(),
            "header": "hex_color"
        },
        "currency": {
            "name": "Currency Code",
            "generator": lambda i: fake.currency_code(),
            "header": "currency"
        },
        "language": {
            "name": "Language",
            "generator": lambda i: fake.language_name(),
            "header": "language"
        },
        "timezone": {
            "name": "Timezone",
            "generator": lambda i: fake.timezone(),
            "header": "timezone"
        }
    }
    
    return column_types

def display_column_menu(column_types: Dict) -> List[str]:
    """Display column selection menu and return selected columns"""
    print("\n" + "="*60)
    print("📋 COLUMN SELECTION MENU")
    print("="*60)
    print("Select columns to include in your dataset:")
    print("Enter column numbers separated by commas (e.g., 1,2,5,8)")
    print("Or type 'all' to select all columns")
    print("Or type 'default' for a standard set of columns")
    print("-"*60)
    
    # Display columns in a nice format
    column_list = list(column_types.keys())
    for i, col_key in enumerate(column_list, 1):
        col_info = column_types[col_key]
        print(f"[{i:2d}] {col_info['name']}")
        if i % 20 == 0 and i < len(column_list):  # Add spacing every 20 items
            print("-"*60)
    
    print("="*60)
    
    while True:
        try:
            selection = input("\nYour selection: ").strip().lower()
            
            if selection == 'all':
                return column_list
            elif selection == 'default':
                return ['id', 'name', 'email', 'age', 'phone', 'city', 'company', 'job_title', 'salary', 'status']
            else:
                # Parse comma-separated numbers
                numbers = [int(x.strip()) for x in selection.split(',')]
                selected_columns = []
                
                for num in numbers:
                    if 1 <= num <= len(column_list):
                        selected_columns.append(column_list[num - 1])
                    else:
                        print(f"❌ Invalid selection: {num}. Please choose numbers between 1 and {len(column_list)}")
                        raise ValueError("Invalid selection")
                
                if not selected_columns:
                    print("❌ No columns selected. Please select at least one column.")
                    continue
                
                # Show selected columns for confirmation
                print(f"\n✅ Selected {len(selected_columns)} columns:")
                for col_key in selected_columns:
                    print(f"   • {column_types[col_key]['name']}")
                
                confirm = input("\nConfirm selection? (y/n): ").strip().lower()
                if confirm in ['y', 'yes']:
                    return selected_columns
                else:
                    print("Selection cancelled. Please choose again.")
                    continue
                    
        except (ValueError, IndexError):
            print("❌ Invalid input. Please enter numbers separated by commas, 'all', or 'default'")
            continue

def generate_mock_data(rows=100_000, selected_columns=None):
    fake = faker.Faker()
    column_types = get_column_types()
    
    # Use default columns if none selected
    if selected_columns is None:
        selected_columns = ['id', 'name', 'email', 'age', 'phone', 'city', 'company', 'job_title', 'salary', 'status']
    
    # Generate filename with row count and column count
    filename = f"mock_data_{rows}_rows_{len(selected_columns)}_cols.csv"
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write header based on selected columns
        headers = [column_types[col]['header'] for col in selected_columns]
        writer.writerow(headers)
        
        # Generate rows
        start_time = time.time()
        for i in range(1, rows + 1):
            # Update progress bar every 100 rows or on the last row
            if i % 100 == 0 or i == rows:
                elapsed_time = time.time() - start_time
                if i > 0:
                    rate = i / elapsed_time
                    print_progress_bar(i, rows, rate, prefix='Generating rows:')
            
            # Generate row data based on selected columns
            row_data = []
            for col_key in selected_columns:
                generator = column_types[col_key]['generator']
                value = generator(i)
                row_data.append(value)
            
            writer.writerow(row_data)
    
    return filename

if __name__ == "__main__":
    print("🎯 MOCK DATA GENERATOR")
    print("="*50)
    
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
    
    # Get column types and let user select
    column_types = get_column_types()
    selected_columns = display_column_menu(column_types)
    
    print(f"\n🚀 Starting generation of {rows:,} rows with {len(selected_columns)} columns...")
    filename = generate_mock_data(rows, selected_columns)
    print(f"✅ Mock data CSV with {rows:,} rows and {len(selected_columns)} columns generated successfully as '{filename}'!")
