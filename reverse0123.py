import turing

# This program reverses string of input data. Supported data values: 0 to 3.

data = '0103120131'
program = \
"""
000x<  This state carries 0 to the left
011x<
022x<
033x<
0_80>  in case of _ it appents 0 to the begining of data and start returning
0x4x<  in case of x it switches to state 6

100x<  Similar to state 0, but applies to bit 1
111x<
122x<
133x<
1_81>
1x5x<

200x<  Similar to state 0, but applies to bit 2
211x<
222x<
233x<
2_82>
2x6x<

300x<  Similar to state 0, but applies to bit 3
311x<
322x<
333x<
3_83>
3x7x<

4040<  This state is similar to state 0, but it carries 0 over x bits
4141<
4242<
4343<
4_80>  
4x4x<

5050<  Similar to state 4, but applies to bit 1
5151<
5252<
5353<
5_81>
5x5x<

6060<  Similar to state 4, but applies to bit 2
6161<
6262<
6363<
6_82>
6x6x<

7070<  Similar to state 4, but applies to bit 3
7171<
7272<
7373<
7_83>
7x7x<

8080>  This state returns to the right
8181>
8282>
8383>
8x9x>  in case of x it switches to state 9

9x9x>  This state returns to the right over all x bits
900x<  in case of a value other than x, it takes it and start moving to the
911x<  left. It also switches to the state 0, 1, 2, or 3, depending of the bit.
922x<
933x<
9_x_<  Halt
"""


print 'Output data: ' + str(turing.Turing(program, data).Run())

