import array as arr

a = arr.array('i',[1,2,3])
for i in a:
    print(i)

# Type code	| Python Data Type	| Byte size
# i	int	2
# I	int	2
# u	unicode character	2
# h	int	2
# H	int	2
# l	int	4
# L	int	4
# f	float	4
# d	float	8

#Error
#a = arr.array('i',[1.1,2,3])

#emmpty array
a = arr.array('i',[])
print(len(a))

# Array operations: (all same as python list)
# - Add
# - Update/Read
# - Remove
# - Looping
# - Concatenation
# - Slicing