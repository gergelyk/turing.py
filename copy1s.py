import turing

# This program replaces 1s by x until it meet '0'. All 1s are appended to the
# end of data

data = '1110'
program = \
"""
00x0>  Initial state, if 0 then halt
011x>  Initial state, if 1 then erase it and move on
1010>  Overwrite 0 by 0, move on
1111>  Overwrite 1 by 1, move on
1_21<  End of the string, append 1 and change direction
2020<  Overwrite 0 by 0, move back
2121<  Overwrite 1 by 1, move back
2x0x>  If the bit is erased, change direction and go to initial state
"""

print 'Output data: ' + str(turing.Turing(program, data).Run(0.3))

