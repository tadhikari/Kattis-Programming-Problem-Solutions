def go_or_no(capacity,requirement):
    if len(capacity) >= len(requirement):
        return 'go'
    else:
        return 'no'
cap = input()
req = input()
print(go_or_no(cap,req))
