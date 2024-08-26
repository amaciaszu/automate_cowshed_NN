# automate_cowshed_NN
automated farm to manage weight and milk production on farms

# The database should be located in the path data_base/automated_cowshed.db
# It has not been possible to upload the file with all the loaded data because it exceeds the maximum size. You can still run it and it will create a new database with the same structure but without records.

#########################
#automate_cowshed
#########################

Endpoints to manage the input and output of data to manage a cowshed where daily measurements are made of the weight and liters of milk from cows.
Several reports are available that can be run on demand for data mining and decision making.

#########################
#Installation:
#########################

git clone https://github.com/amaciaszu/automate_cowshed_NN.git
cd proyecto

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

#########################
#Start services:
#########################

uvicorn modules.main:app --reload

#########################
#Execute reports:
#########################

python scripts/report_milk_production_cows_per_day.py
python scripts/report_cow_could_be_sick.py
python scripts/report_cow_weight.py

#########################
#Execute load data from parquet files:
#########################

python scripts/simulate_data_sensors_from_parquet.py

#########################
#Execute Unite test:
#########################

python -m unittest tests/unit_test.py
