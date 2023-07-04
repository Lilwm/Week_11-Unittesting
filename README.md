## Telecommunication Billing Data Pipeline Unit Tests
This repository contains unit tests for a data pipeline responsible for extracting, transforming, and loading telecommunication billing data. The unit tests are implemented using the unittest framework in Python.

### Usage
To run the unit tests, execute the following command in the project directory:

` python unit_testing.py`
### Test Cases
The unit tests cover the following scenarios and edge cases for each function in the data pipeline:

#### data_extraction
* Check if the returned object is a DataFrame.
* Check if the DataFrame has the expected columns.
* Check if the DataFrame has non-null values in all columns.
* Check if the DataFrame has at least one row.
  
#### data_transformation
* Check if the result of the transformation matches the expected transformed data.

#### data_loading
* Check if the saved data is a DataFrame.
* Check if the saved data has the same columns as the input data.
* Check if the saved data has the same values as the input data.
