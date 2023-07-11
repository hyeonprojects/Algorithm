"""
Stack은 LIFO(Last In, First Out) 또는 FILO(First In, Last Out) 데이터 관리 방식을 따름
"""

stack = []

# 원소 추가 push
stack.append(4)

print(stack)

# stack
top = stack.pop()
print(top)

# 그냥 값만 가져올떄
top = stack[-1]

