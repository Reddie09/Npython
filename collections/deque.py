"""
Módulo collections - deque

Podemos dizer que o deque é uma lista de alta performance
"""
from collections import deque

deq = deque('reddie')

print(deq)

deq.append('9')

print(deq)

deq.appendleft('K')

print(deq)

# Remover elementos
print(deq.popleft())
print(deq.pop())
