# States: Fit, Unfit
# Actions: Excercise, Relax
#
# | Excercise | Fit    | Unfit  |
# | Fit       | 0.99,8 | 0.01,8 |
# | Unfit     | 0.2,0  | 0.8,0  |
#
# | Relax     | Fit    | Unfit  |
# | Fit       | 0.7,10 | 0.3,10 |
# | Unfit     | 0,5    | 1,5    |
#
# 
#
#
#
#





excercise = [[[0.99,8],[0.01,8]], [[0.2,0],[0.8,0]]]
relax = [[[0.7,10],[0.3,10]], [[0,5],[1,5]]]

iterations = int(raw_input("Please enter number of iterations: "))
disc_val = float(raw_input("Please enter discounted value (0 < y < 1): "))
state = raw_input("Please enter state: ")

if state == "fit" or state == "Fit":
	state = 0
else:
	state = 1
	
def q0(s,a):
	if a == "excercise":
		part1 = excercise[s][0][0] * excercise[s][0][1]
		part2 = excercise[s][1][0] * excercise[s][1][1]
		part3 = part1 + part2
	else:
		part1 = relax[s][0][0] * relax[s][0][1]
		part2 = relax[s][1][0] * relax[s][1][1]
		part3 = part1 + part2
	return part3
		
	
def Vn(s, n):
	temp1 = qn(s, "excercise", n)
	temp2 = qn(s, "relax", n)
	return max(temp1, temp2)
	
	
def qn(s,a,n):

	if n == 0:
		return q0(s,a)
			
	temp = q0(s,a)
	
	if a == "excercise":
		part1 = excercise[s][0][0] * Vn(0, n-1)
		part2 = excercise[s][1][0] * Vn(1, n-1)
		part3 = disc_val * (part1 + part2)
		
	else:
		part1 = relax[s][0][0] * Vn(0, n-1)
		part2 = relax[s][1][0] * Vn(1, n-1)
		part3 = disc_val * (part1 + part2)
	
	part4 = temp + part3
	return part4
	
	
print("Excercise: " + str(qn(state, "excercise", iterations)))
print("Relax: " + str(qn(state, "relax", iterations)))
	


	

