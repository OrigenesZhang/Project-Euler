mat = {}
mat[1] = 'one'
mat[2] = 'two'
mat[3] = 'three'
mat[4] = 'four'
mat[5] = 'five'
mat[6] = 'six'
mat[7] = 'seven'
mat[8] = 'eight'
mat[9] = 'nine'
mat[10] = 'ten'
mat[11] = 'eleven'
mat[12] = 'twelve'
mat[13] = 'thirteen'
mat[14] = 'fourteen'
mat[15] = 'fifteen'
mat[16] = 'sixteen'
mat[17] = 'seventeen'
mat[18] = 'eighteen'
mat[19] = 'nineteen'

mat[20] = 'twenty'
mat[30] = 'thirty'
mat[40] = 'forty'
mat[50] = 'fifty'
mat[60] = 'sixty'
mat[70] = 'seventy'
mat[80] = 'eighty'
mat[90] = 'ninety'

mat[100] = 'hundred'

mat[1000] = 'thousand'

'''--------------------------------------------- '''

ans = 0

for i in range(1, 20):
    ans += len(mat[i])
for i in range(20, 100):
    ans += len(mat[i - (i % 10)])
    if i % 10 != 0:
        ans += len(mat[i % 10])
ans *= 10

ans += 900 * len(mat[100])
ans += (900 - 9) * len('and')
for i in range(1, 10):
    ans += 100 * len(mat[i])
ans += len(mat[1]) + len(mat[1000])
print(ans)

