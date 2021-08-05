# COVID-19 API

## About

This COVID-19 API will receive a csv file from a client request, cleanse and aggregate the csv data and returns a JSON response.



## How to run

1. Run `pip install -r requirement.txt` to install the required libraries
2. Click [here](https://data.nsw.gov.au/data/dataset/60616720-3c60-4c52-b499-751f31e3b132/resource/945c6204-272a-4cad-8e33-dde791f5059a/download/pcr_testing_table1_location.csv) to download the csv file to your computer and place it in `./csv/` folder
3. The API endpoint is `localhost:8080/data/api/<file>` where `<file>` is the name of the csv file 
4. Send a POST request to the above endpoint and wait for the JSON response.