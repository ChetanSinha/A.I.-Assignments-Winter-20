class board():
	def __init__(self, N):
		self.arr = [N*[0] for i in range(N)]
		self.queens=0
		self.g_cost=0
		self.h_cost=(N-self.queens)

QueueOfBoards = []
solutions=False
cost=0

def print_(temp):
	for i in range(len(temp.arr)):
		for j in range(len(temp.arr[0])):
			print(temp.arr[i][j], end=" ")
		print()

	print("heuristics: ", temp.h_cost)
	print("path cost: ", temp.g_cost)
	print("no. of queens: ", temp.queens)
	print()

# def sorted_by(b1, b2):
# 	return (b1.h_cost+h1.g_cost)<(b2.h_cost+b2.g_cost) 

def isvalid(temp):
	q = temp.queens
	
	for i in range(8):
		if temp.arr[q-1][i] == 1:
			break
	
	t = i

	for j in range(q-2, -1, -1):
		if temp.mat[j][t] == 1:
			return False

	for i,j in zip(range(t-1,-1,-1), range(q-2,-1,-1)):
		# if j<0 or i<0:
		# 	break
		if temp.arr[j][i] == 1:
			return False

	for i,j in zip(range(t+1,8), range(q-2,-1,-1)):
		# if j<0 or i>7:
		# 	break
		if temp.arr[j][i] == 1:
			return False

	

	return True


def states(queue):
	temp = board(8)
	size = len(queue)
	
	global cost
	global solutions

	queue.sort(key=lambda x: (x.h_cost + x.g_cost))

	temp = queue[0]
	queue.pop(0)
	q = temp.queens

	if temp.queens == 8:
		print_(temp)
		print("Solution found")
		print("cost: ", cost)
		solutions=True
		return

	for i in range(8):
		temp.arr[q][i] = 1
		pre = temp.g_cost
		temp.queens += 1
		temp.h_cost -= 1
		temp.g_cost = pre + 1

		if(q==0 or isvalid(temp)):
			print_(temp)
			queue.append(temp)
			cost += 1

		temp.queens -= 1
		temp.h_cost += 1
		temp.g_cost = pre
		temp.arr[q][i] = 0	


if __name__ == '__main__':
	b1 = board(8)
	QueueOfBoards.append(b1)
	while(QueueOfBoards and solutions==False):
		states(QueueOfBoards)
