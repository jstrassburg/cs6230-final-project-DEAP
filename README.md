# cs6230-final-project-DEAP

* This project evaluates the python library [DEAP - Distributed Evolutionary Algorithms in Python](https://deap.readthedocs.io/en/master/) 
* We're using DEAP to optimize an answer to the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
* The [GeoPy](https://geopy.readthedocs.io/en/stable/#) library is used for geographical distance calculations.

## Installation Notes

* The installation package for DEAP uses `2to3` in its build.
* Support for this was removed in [setuptools v58.0.0](https://setuptools.pypa.io/en/latest/history.html#v58-0-0).
* Because of this, we create a virtual environment without `setuptools` and then install the last version before version 58.

```shell
virtualenv --no-setuptools .env
source .env/bin/activate # or for Windows, .\.env\Scripts\activate
pip install setuptools<58
pip install -r requirements.txt
```