start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start % 2 == 1:
    start += 1

for num in range(start, end + 1, 2):
    print(num)
