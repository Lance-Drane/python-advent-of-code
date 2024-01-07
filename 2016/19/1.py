bin_str = bin(int(input()))
print(int(bin_str[3:] + bin_str[2], 2))
