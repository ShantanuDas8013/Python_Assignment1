def identical(strings):
    for index,string in enumerate(strings):
        if isinstance(string,str) and len(string)>0 and string[0]==string[-1]:
            print(f"Strings: {string}, Index: {index}")



A=['abc', 'xyz', 'aba', '1221']
identical(A)