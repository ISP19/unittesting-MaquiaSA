## Unit Testing Assignment

by Anant Arayanant.


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

| Test case                          |  Expected Result |
|------------------------------------|------------------|
| int Numerator and int Denominator  |  Fraction(`numerator`, `denominator`) (stored in proper fraction form) |
| Non-int Numerator or Denominator   |  TypeError       |


**Test Cases for `__str__`**

| Test case                                     |  Expected Result |
|-----------------------------------------------|------------------|
| int Numerator and int Denominator(not 0 or 1) |  `numerator`/`denominator` in Proper Fraction Form |
| Numerator Only or Denominator = 1             |  `numerator`     |
| Numerator = 0 and non-zero-int Denominator    |  0               |
| Positive int Numerator and Denominator = 0    |  1/0             |
| Negative int Numerator and Denominator = 0    |  -1/0            |
| Numerator = 0 and Denominator = 0             |  0/0             |


**Test Cases for `__add__`**

(Infinity = 1/0, Negative Infinity = -1/0)

| Test case                                         |  Expected Result         |
|---------------------------------------------------|--------------------------|
| Normal Fractions (Positive/Negative) add together | Proper Positive Fraction |
| Fractions and Zero                                | The Sum of those Fractions in Proper Form |
| Infinity and Normal Fractions                     | 1/0                      |
| Negative Infinity and Normal Fractions            | -1/0                     |
| Infinity and Negative Infinity                    | 0/0                      |


**Test Cases for `__sub__`**

(Infinity = 1/0, Negative Infinity = -1/0)

| Test case                                        |  Expected Result      |
|--------------------------------------------------|-----------------------|
| Normal Fractions (Positive/Negative) subtract together | Proper Positive/Negative Fraction |
| Fractions and Zero (in order)                    | The Difference of those Fractions in Proper Form |
| Zero and Fractions (in order)                    | Negative Form of the Difference of those Fractions in Proper Form |
| Infinity and Normal Fractions                    | 1/0 or -1/0           |
| Negative Infinity Fractions and Normal Fractions | 1/0 or -1/0           |
| Infinity or Negative Infinity subtract together  | 0/0                   |


**Test Cases for `__mul__`**

(Infinity = 1/0, Negative Infinity = -1/0)

| Test case                                    |  Expected Result    |
|----------------------------------------------|---------------------|
| Normal Fractions (Positive/Negative) multiply together | Proper Positive/Negative Fraction |
| Fractions and Zero                           | 0                   |
| Infinity (or Negative Infinity) and Normal Fractions | 1/0 or -1/0         |
| Infinity (or Negative Infinity) multiply together    | 1/0 or -1/0         |
| Infinity (or Negative Infinity) and Zero     | 0/0                 |


**Test Cases for `__gt__`**

(Infinity = 1/0, Negative Infinity = -1/0, NaN = 0/0)

| Test case                                    |  Expected Result |
|----------------------------------------------|------------------|
| Larger Fraction > Smaller Fraction           | True             |
| Smaller Fraction > Larger Fraction           | False            |
| Same Proper Fraction > Same Proper Fraction  | False            |
| Infinity > Normal Fractions                  | True             |
| Normal Fractions > Infinity                  | False            |
| Negaive Infinity > Normal Fractions          | False            |
| Normal Fractions > Negative Infinity         | True             |
| NaN > Any Fraction                           | False            |
| Any Fraction > Nan                           | False            |


**Test Cases for `__neg__`**

(Infinity = 1/0, Negative Infinity = -1/0, NaN = 0/0)

| Test case                                  |  Expected Result  |
|--------------------------------------------|-------------------|
| Any Positive Fraction (including Infinity) | Negative Fraction |
| Any Negative Fraction (including Infinity) | Positive Fraction |
| Zero                                       | Zero              |
| NaN                                        | NaN               |


**Test Cases for `__eq__`**

| Test case                            |  Expected Result |
|--------------------------------------|------------------|
| Fractions with same Proper Form      | True             |
| Fractions with different Proper Form | False            |