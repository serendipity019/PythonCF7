string = "Coding Factory"

s1 = string[7] # 'F'
print(s1)

s2 = string[:] # entire string
print(s2)

s3 = string[::] # [start:stop:step]
print(s3)

s4 = string[7:] # from index 7 to end
print(s4)

s5 = string[-1] # last character
print(s5)

# Coding Factor
s6 = string[:-1] # entire string except last character
print(s6)

# Factor
s7 = string[7:-1] # from index 7 to second last character
print(s7)

s8 = string[7:7] # empty string (since start and stop are the same)
print(s8)

r_s = string[13:(-len(string)-1):-1] # reverse string
print(r_s)

r_s2 = string[::-1] # reverse string
print(r_s2)