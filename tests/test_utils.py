import utils

st = "a(_____), #sum{ _____,_____ : a  ( _____,_____ )} = _____, #sum{ _____,_____ : a  ( _____,_____ )} = _____"
expected = [AggregateElement([1,2],[3,4],5), AggregateElement([6,7],[8,9],10)]
res = get_aggregates(st)
print(res == expected)
print(res[0])

st = "a(_____), #sum{ _____,_____ : a  ( _____,_____ )} = _____, a(_____), #sum{ _____,_____ : a  ( _____,_____ )} = _____"
expected = [AggregateElement([1,2],[3,4],5), AggregateElement([7,8],[9,10],11)]
res = get_aggregates(st)
print(res == expected)