## Unit Testing Assignment

by Bill Gates.


## Test Cases for unique


| Test case              |  Expected Result    |
|------------------------|---------------------|
| Empty List             |  Empty List         |
| Single Item            |  List with 1 Item   |
| One Item, Many Times   |  List with 1 Item   |
| 2 Items, Many Times, Many Orders | 2 item list, items in same order  |
| >2 Items, Many Times, Many Orders | >2 item list, items in same order  |
| Non-List               |  TypeError          |


## Test Cases for Fraction
**Test Cases for `__init__`**

| Test case                                     |  Expected Result |
|-----------------------------------------------|------------------|
| non-zero-int Numerator and non-zero-int Denominator |  Fraction(`numerator`, `denominator`) |
| Numerator and Denominator equal to Zero (0/0) |  ValueError      |
| Non-int Numerator or Denominator              |  TypeError       |


**Test Cases for `__str__`**

| Test case                                     |  Expected Result |
|-----------------------------------------------|------------------|
| int Numerator and int Denominator(not 0 or 1) |  `numerator`/`denominator` in Proper Fraction Form |
| Numerator Only or Denominator = 1             |  `numerator`     |
| Numerator = 0 and non-zero-int Denominator    |  0               |
| Positive int Numerator and Denominator = 0    |  1/0             |
| Negative int Numerator and Denominator = 0    |  -1/0            |


**Test Cases for `__add__`**

| Test case                                         |  Expected Result         |
|---------------------------------------------------|--------------------------|
| Normal Fractions (Positive/Negative) add together | Proper Positive Fraction |
| Fractions and Zero                                | The Sum of those Fractions in Proper Form |
| Positive 0-denominator Fractions and Normal Fractions | 1/0                      |
| Negative 0-denominator Fractions and Normal Fractions | -1/0                     |
| 0-denominator Fractions add together              | ValueError               |


**Test Cases for `__sub__`**

| Test case                                         |  Expected Result         |
|---------------------------------------------------|--------------------------|
| Normal Fractions (Positive/Negative) subtract together | Proper Positive/Negative Fraction |
| Fractions and Zero                                | The Difference of those Fractions in Proper Form |
| Positive 0-denominator Fractions and Normal Fractions | 1/0 or -1/0              |
| Negative 0-denominator Fractions and Normal Fractions | 1/0 or -1/0              |
| 0-denominator Fractions subtract together         | ValueError               |


**Test Cases for `__eq__`**

| Test case                            |  Expected Result |
|--------------------------------------|------------------|
| Fractions with same Proper Form      | True             |
| Fractions with different Proper Form | False            |