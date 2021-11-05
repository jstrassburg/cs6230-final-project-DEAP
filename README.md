# cs6230-final-project-DEAP

* This project evaluates the python library [DEAP - Distributed Evolutionary Algorithms in Python](https://deap.readthedocs.io/en/master/) 
* We're using DEAP to optimize an answer to the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
* The [GeoPy](https://geopy.readthedocs.io/en/stable/#) library is used for geographical distance calculations.
  * The distance calculations are used in the fitness function.

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

## Famous Addresses Used

The example contained herein uses famous address in the United States as points in the _Travaling Salesman Problem_.

* The White House - 1600 Pennsylvania Avenue, Washington DC  20006
* Wall Street - 11 Wall Street New York, NY  10005
* Empire State Building - 350 Fifth Avenue New York, NY 10118
* The Hollywood Sign - 4059 Mt Lee Dr. Hollywood, CA 90068
* The Gateway Arch - The Gateway Arch, St. Louis, MO
* The Golden Gate Bridge - Golden Gate Bridge, San Francisco, CA
* The Space Needle - Space Needle, Broad Street, Seattle, WA
* MSOE - 1025 N Broadway, Milwaukee, WI 53202