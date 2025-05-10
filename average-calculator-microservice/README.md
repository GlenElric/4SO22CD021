# Average Calculator Microservice

This microservice provides an API for calculating the average of unique numbers based on specified criteria. It supports fetching numbers that are prime, Fibonacci, even, or random, and maintains a configurable window size for the calculations.

## Project Structure

```
average-calculator-microservice
├── src
│   ├── app.py                # Entry point of the microservice
│   ├── services
│   │   ├── number_fetcher.py # Fetches unique numbers from a third-party server
│   │   └── calculator.py      # Calculates the average of stored numbers
│   ├── routes
│   │   └── numbers.py        # Defines the REST API endpoint
│   └── utils
│       └── helpers.py        # Utility functions for validation and formatting
├── requirements.txt          # Project dependencies
├── config.py                 # Configuration settings
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd average-calculator-microservice
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the microservice settings in `config.py` as needed.

4. Run the microservice:
   ```
   python src/app.py
   ```

## API Usage

### Endpoint

- `GET /numbers/{numberid}`

### Parameters

- `numberid`: The ID of the number type to fetch:
  - `p`: Prime numbers
  - `f`: Fibonacci numbers
  - `e`: Even numbers
  - `r`: Random numbers

### Response

The response will include:
- The current average of the numbers fetched.
- The previous state of stored numbers.
- The current state of stored numbers.

### Example Request

```
GET /numbers/p
```

### Example Response

```json
{
  "previous_state": [2, 3, 5],
  "current_state": [2, 3, 5, 7],
  "average": 4.25
}
```

## Notes

- The microservice is designed to respond within 500 milliseconds.
- Ensure that the third-party server for fetching numbers is accessible and properly configured in the `number_fetcher.py` service.