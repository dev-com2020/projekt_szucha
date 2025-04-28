import pytest
import csv
import json

def load_csv_data():
    with open("data.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(int(row['num']), int(row['output'])) for row in reader]

def load_json_data():
    with open("data.json") as f:
        data = json.load(f)
        return [(item['num'], item['output']) for item in data]

@pytest.mark.parametrize(
        "num,output",
        [(1,11),(2,22),(5,456),(3,33)],
        ids=["1x11","2x22","5x456","3x33"]
        )
def test_multi_11(num,output):
    assert 11*num == output


@pytest.mark.parametrize("num,output",load_csv_data())
def test_multi_csv(num,output):
    assert 11*num == output

@pytest.mark.parametrize("num,output",load_json_data())
def test_multi_json(num,output):
    assert 11*num == output

