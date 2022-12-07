def test_file2_method1():
	x=5
	y=6
	assert x+1 == y
	assert x == y
def test_file2_method2():
	x=5
	y=6
	assert x+1 == y
     

# in this case run time we use the pytest <file name> -v -k "mathch substring"

# -k means match the at least one string in the given function name
# if match the string in the function name that will be tested remaing is deselected
# if not match the string not test will be run. zero test is selected