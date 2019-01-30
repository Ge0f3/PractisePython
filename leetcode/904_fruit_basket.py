
import sys

def fruit_basket(tree):
	cnt = {}
	i = res = 0
	for j, v in enumerate(tree):
		cnt[v] = cnt.get(v, 0) + 1  
		while len(cnt) > 2:  
			cnt[tree[i]] -= 1
			if cnt[tree[i]] == 0:
				del cnt[tree[i]]
				i += 1
				res = max(res, j - i + 1)  # 结束一个区间，更新一次最优结果
	return res

def main():
	print("*****************Fruit Basket*****************")
	nums = [int(x) for x in input("Enter the array input: ").split(',')]
	print("The elements {}".format(fruit_basket(nums)))

		
if __name__ == '__main__':
	main()