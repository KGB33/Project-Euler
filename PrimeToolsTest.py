# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:34:27 2018

@author: kelto
"""

import PrimeTools
import time


"""
Testing speed of LittleFermat Vs divisability
"""
testingPrime = 32416190071
start_FLT = time.clock()
result_FLT = PrimeTools.littleFermat(testingPrime, 2)
end_FLT = time.clock()

print('FLT Time: ', end_FLT - start_FLT )

start_Div = time.clock()
#result_Div = PrimeTools.divisionTest(testingPrime)
end_Div = time.clock()



print('DIV Time: ', end_Div - start_Div)
