def solve():
    t = int(input("Enter number of test cases: "))
    
    for _ in range(t):
        a, b, c, n = map(int, input().split())
        
        max_val = max(a, b, c)
        
        needed = (3 * max_val) - (a + b + c)
        
        if needed <= n and (n - needed) % 3 == 0:
            print("YES")
        else:
            print("NO")

solve()