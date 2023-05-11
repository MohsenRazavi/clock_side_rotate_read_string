def right(ans, letters, index, i):
    while i < len(letters[index]) and letters[index][i][1] != 1 :
        ans += letters[index][i][0]
        letters[index][i][1] = 1
        i += 1

    return ans
 
def down(ans, letters, index, i):
    while i < len(letters[index]) and letters[i][index][1] != 1 :
        ans += letters[i][index][0]
        letters[i][index][1] = 1
        i += 1

    return ans



def left(ans, letters, index, i):
    while i >= 0  and letters[index][i][1] != 1 :
        ans += letters[index][i][0]
        letters[index][i][1] = 1
        i -= 1

    return ans


def up(ans, letters, index, i):
    while i >= 0  and letters[i][index][1] != 1 :
        ans += letters[i][index][0]
        letters[i][index][1] = 1
        i -= 1

    return ans
  

n = int(input())
letters = []

for i in range(n):
    letters.append([[i, 0] for i in input()])

ans = ''

for i in range(n//2):
    ans = right(ans, letters, i, i)
    ans = down(ans, letters, n-i-1, i+1)
    ans = left(ans, letters, n-i-1, n-2-i)
    ans = up(ans, letters, i, n-2-i)

print('-'.join([i for i in ans]))


"""
5

xxxxx
noooy
npqry
nddry
tttty

x-x-x-x-x-y-y-y-y-t-t-t-t-n-n-n-o-o-o-r-r-d-d-p-q
"""
