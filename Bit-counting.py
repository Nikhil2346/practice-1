def count_bits(n):
    l = [int(i) for i in (bin(int(n))) if i != 'b']
    return (sum(l))
print(count_bits(n=input("Enter: ")))
