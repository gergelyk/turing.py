import turing

# This program reverses string of input data. Supported data values: 0, 1.

data = '0110101000110101000110101000110101000110101000110101000110101000110101'
program = \
"""
0020>
0131>
02a2<
03a3<

2020>
2121>
2_4_<
2242<
2343<

3030>
3131>
3_5_<
3252<
3353<

4062<
4172<

5063<
5173<

6060<
6161<
6_8_>
6282>
6383>

7070<
7171<
7_9_>
7292>
7393>

8002>
8102>
82a2<
83a3<

9003>
9103>
92a2<
93a3<

a2a2<
a3a3<
a_b_>

b2b0>
b3b1>
b_x_>

"""

# Create a machine
tm = turing.Turing(program, data, printing=False)

# Run the program
output_data = tm.Run()

# Test output data
test_result = list(output_data) == list(data)[::-1]

# Print summary
print 'Output data: ' + output_data + '\n'
print 'Test ' + ['failed', 'passed'][test_result] + '!'
