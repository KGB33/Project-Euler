# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:34:27 2018

@author: kelto
"""

from PrimeTools import timer, littleFermat, divisionTest


"""
Testing speed of LittleFermat Vs divisability
"""
testingPrime = 32416190071
result_FLT = @timer littleFermat(testingPrime, 2)


print('FLT Time: ', end_FLT - start_FLT )

start_Div = time.clock()
#result_Div = PrimeTools.divisionTest(testingPrime)
end_Div = time.clock()



print('DIV Time: ', end_Div - start_Div)
