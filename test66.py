def rev_str(data):
    result=""
    for char in data:
        result=char+result
    return result

str1=rev_str("paras")
print(str1)
