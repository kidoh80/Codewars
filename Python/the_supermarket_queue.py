def queue_time(customers, n):
  queue = [customers.pop(0) for i in range(n)]
  count = 0
  while (len(customers)>0 or sum(queue) > 0):
    for i,customer in enumerate(queue):
      if queue[i] > 0:
        queue[i] -= 1
      else:
        queue[i] = customers.pop(0)
    count += 1
    print (queue)
  return (count)

print (queue_time([5,3,4], 1))
print (queue_time([10,2,3,3], 2))
print (queue_time([2,3,10], 2))
