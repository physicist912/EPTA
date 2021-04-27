# EPTA

I will upload codes here to make our works to be more faster and much efficient
If you have any suggestion to improve the quality of codes, please contact with me: jjang@mpifr-bonn.mpg.de

Pre-requisites: python (above 3.0), pandas, numpy, matplotlib


1. making csv file

TEMPO2 will show up all parameters with the uncertainties. The reference papers may write parameters in this way: eg) 0.00000156(31) which is equivalent to 0.00000031. 

In csv file, you need to write values and uncertainties of each parameter in this way

par       ref    dref 				out 		dout
param 1   value  uncertainty	value		uncertainty.

For the uncertainty of the reference, just put 31, for instance. 


2. Running code

If you see the code, you can find the commands

obj='J1439' is the object name
dat=obj+'/'+obj+'.csv' is calling the directory as well as file. (**** You can either make a directory named as the object name. If you do not want to make a directory, then, please just leave obj+'.csv')

params=list(df['par']) is calling the parameters.
comp='mk_new' is the name of outputs
dcomp='d'+comp is calling the uncertainty column of your output 
comp2='mk+time+epoch' is the reference
dcomp2='d'+comp2 is the uncertainty of the reference.


