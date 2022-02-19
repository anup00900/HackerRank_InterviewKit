def lonelyinteger(a):
    # Write your code here
    s=0
    for i in a:
        s=s^i
    return s  