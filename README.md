# COVID-19 API

## About

This COVID-19 API will receive a csv file from a client request, cleanse and aggregate the csv data and returns a JSON response.



## How to run

1. Run `pip install -r requirement.txt` to install the required libraries
2. Click [here](https://data.nsw.gov.au/data/dataset/60616720-3c60-4c52-b499-751f31e3b132/resource/945c6204-272a-4cad-8e33-dde791f5059a/download/pcr_testing_table1_location.csv) to download the csv file to your computer
3. Run `py app.py` to start the server
4. Go to the host link on the Flask terminal
5. Upload the csv file that you just downloaded **OR** place the csv file in `/csv/` folder
6. Go to path `localhost:8080/data/api/?file=pcr_testing_table1_location.csv` to get the JSON response



## Testing

A test file is located in `/csv/testfile.csv` folder. 

If you get the test JSON response (`localhost:8080/data/api/?file=testfile.csv`), you should expect to see:

- Inner West (A) as lga with highest total test count, day with most tests on 2020-02-01 with 5 counts, day with least tests on 2020-01-01 with 2 counts
- Ku-ring gai (A) and Strathfield (A) as lga(s) with second highest test count
- All records with null value in lga_code19, lga_name19 are not included

