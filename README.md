# Mock Data Generator

A fast and flexible Python tool for generating realistic mock data in CSV format. Perfect for testing applications, populating databases, and creating sample datasets for development and testing purposes.

## Features

- **High Performance**: Generates large datasets quickly with real-time progress tracking
- **Realistic Data**: Uses the Faker library to create authentic-looking data
- **Comprehensive Fields**: Generates 20 different data fields including personal, professional, and financial information
- **Flexible Output**: Customizable number of rows with automatic filename generation
- **Progress Tracking**: Real-time progress bar with generation rate display
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Generated Data Fields

The tool generates CSV files with the following columns:

| Field | Description |
|-------|-------------|
| `id` | Unique sequential identifier |
| `name` | Full name |
| `email` | Email address |
| `age` | Calculated age based on birth date |
| `country` | Country name |
| `city` | City name |
| `address` | Full address |
| `phone` | Phone number |
| `company` | Company name |
| `job_title` | Job title |
| `salary` | Salary (30,000 - 150,000) |
| `registration_date` | Registration date (last 5 years) |
| `last_login` | Last login timestamp |
| `status` | Account status (active, inactive, pending, suspended) |
| `gender` | Gender identity |
| `birth_date` | Birth date (18-80 years old) |
| `credit_card` | Credit card number |
| `website` | Website URL |
| `department` | Department (Engineering, Marketing, Sales, etc.) |
| `experience_years` | Years of experience (0-40) |

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VeniaminBalan/mock_data_generator.git
   cd mock_data_generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line with Arguments

Generate a specific number of rows:

```bash
python mock_data_generator.py 50000
```

### Interactive Mode

Run without arguments to be prompted for the number of rows:

```bash
python mock_data_generator.py
```

### Examples

```bash
# Generate 1,000 rows
python mock_data_generator.py 1000

# Generate 100,000 rows
python mock_data_generator.py 100000

# Generate 1 million rows
python mock_data_generator.py 1000000
```

## Output

The tool creates CSV files with descriptive names based on the number of rows:

- `mock_data_1000_rows.csv` (for 1,000 rows)
- `mock_data_50000_rows.csv` (for 50,000 rows)
- `mock_data_1000000_rows.csv` (for 1,000,000 rows)

## Use Cases

- **Database Testing**: Populate test databases with realistic data
- **Application Development**: Test applications with large datasets
- **Performance Testing**: Benchmark database queries and application performance
- **Data Analysis**: Practice data analysis techniques on sample datasets
- **Demo Purposes**: Create sample data for presentations and demonstrations
- **Load Testing**: Generate large datasets for stress testing

## Requirements

- Python 3.6+
- faker >= 19.0.0

## Performance

The generator is optimized for speed and includes:

- Real-time progress tracking
- Efficient CSV writing
- Memory-conscious data generation
- Performance metrics (rows/second)

Typical performance on modern hardware:
- **Small datasets** (1K-10K rows): < 1 second
- **Medium datasets** (100K rows): 5-15 seconds
- **Large datasets** (1M+ rows): 1-3 minutes

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Issues and Support

If you encounter any issues or have suggestions for improvements, please:

1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include your Python version and operating system

## Acknowledgments

- Built with [Faker](https://faker.readthedocs.io/) for realistic data generation
- Inspired by the need for quick and easy test data creation

---

**Happy Data Generating!**