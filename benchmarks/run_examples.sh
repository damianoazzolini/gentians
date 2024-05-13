# without aggregates
# # 4queens
# gentians -e 4queens -d 5 --verbose=1 --arithm add sub --comparison lt --variables 3

# # adj2red
# gentians -e adjacent_to_red -d 4 --verbose=1

# # clique
# gentians -e clique -d 7 --comparison neq --verbose=1 --variables=2

# # coin
# gentians -e coin --verbose=1

# # coloring
# gentians -e coloring -dh 3 -d 4 --verbose=1

# # evenodd
# gentians -e even_odd --verbose=1

# #grandparent
# gentians -e grandparent --verbose=1

# # sudoku
# gentians -e sudoku -d 3

# hamming0
# gentians -e hamming_0 -d 3 --aggregates "sum(d/2)" --comparison neq --verbose=1 --variables=4

# hamming1
# gentians -e hamming_1 -d 3 --aggregates "sum(d/2)" --comparison neq --verbose=1 --variables=4

# # hamming0n
# gentians -e hamming_0 -d 3 --aggregates "sum(d/2)" "count(d/2)" --comparison neq --verbose=2 --variables=4 -ua

# # hamming1n
# gentians -e hamming_1 -d 3 --aggregates "sum(d/2)" "count(d/2)" --comparison neq --verbose=2 --variables=4 -ua

# # subsum1n
# gentians -e subset_sum -d 3 --aggregates "sum(el/1)" "count(el/1)" --comparison neq --verbose=1 -ua

# # subsum1nop
# gentians -e subset_sum -d 3 --aggregates "sum(el/1)" "count(el/1)" --comparison neq geq leq --verbose=1 -ua

# # subsum2
# gentians -e subset_sum_double -d 4 --aggregates "sum(el/2)" "sum(el/2)" --arithm add --verbose=2 --variables=3

# # subsum2nua
# gentians -e subset_sum_double -d 4 --aggregates "sum(el/2)" "sum(el/2)" --arithm add --verbose=2 --variables=3 -ua

# # subsum2nuac
# gentians -e subset_sum_double -d 4 --aggregates "sum(el/2)" "sum(el/2)" "count(el/2)" "count(el/2)" --arithm add --verbose=2 --variables=3 -ua

# # subsum2prod
# gentians -e subset_sum_double_and_prod -d 4 --aggregates "sum(el/2)" "sum(el/2)" --arithm add mul sub --verbose=1 --variables=5

# # subsum2produa
# gentians -e subset_sum_double_and_prod -d 4 --aggregates "sum(el/2)" "sum(el/2)" --arithm add mul sub --verbose=1 --variables=5 -ua

# # subsum3
# gentians -e subset_sum_triple -d 4 --aggregates "sum(el/3)" "sum(el/3)" "sum(el/3)" --verbose=1 --variables=4

# # ps6
# gentians -e set_partition_sum_new -d 4 --verbose=2 --comparison neq neq --variables 4 --aggregates "sum(p/2)" -ua

# # ps12
# gentians -e set_partition_sum -d 4 --verbose=1 --comparison neq neq --variables 4 --aggregates "sum(p/2)" -ua