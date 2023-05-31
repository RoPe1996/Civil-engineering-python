# Civil-engineering-python

This software use for the automatization of the procedure for geodetic 2D network adjustment with the least squares method (classical geodetic datum or min. trace of the cofactor matrix).
The software is used to calculate least squares adjustment of survey observations for quality control of the observations (in this case directions and lengths) and to calculate coordinates of the observed survey stations. This module uses the linear algebra functions of the python numpy module to set up and solve the least squares equations.
Based on the input measurement data (directions and lengths) and the approximate points coordinates, the program determines the most probable values of unknown parameters based on LSM, and after that creates the adjustment report
