from functools import lru_cache

test_matrix =  [
    [ 1 , 2 , 3 ],
    [ 2 , 4 , 5 ],
    [ 7 , 0 , 1 ]
]

# let max_cheese cheese = 
#   let height = Array.length cheese in
#   let width = Array.length cheese.(0) in
#   let memo = Array.make_matrix height width 0 in
#   let rec poracunaj_celico (vr:int) (st:int) =
#     if st = -1 then () else (
#     let desno = if st = width - 1  then 0 else memo.(vr).(st+1) in
#     let dol = if vr = height - 1  then 0 else memo.(vr+1).(st) in
#     memo.(vr).(st) <- cheese.(vr).(st) + (max desno dol)
#     poracunaj_celico vr (st - 1)
#     )
#   in
#   let rec vrsticno (vr:int) =
#     if vr = -1 then ()
#     else (
#       poracunaj_celico (vr) (width - 1);
#       vrsticno (vr - 1)
#     )
#   in 
#   vrsticno (height - 1);
#   memo.(0).(0)


def max_sir(matrika):
    max_row = len(matrika)
    try: 
        max_col = len(matrika[0])
    except IndexError:
        return 0

    @lru_cache(maxsize=None)
    def max_index(row, col):
        if row == max_row or col == max_col:
            return 0
        return matrika[row][col] + max(
            max_index(row + 1, col),
            max_index(row, col + 1)
        )
    return max_index(0, 0)


print (max_sir(test_matrix))

import sys
sys.setrecursionlimit(10**9)
print(max_sir(
    [[j for j in range(2000)] for _ in range(2000)]
))