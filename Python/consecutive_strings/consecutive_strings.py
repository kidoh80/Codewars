def longest_consec(strarr, k):
    if (k > len(strarr) or k < 0):
        return('')
    longest_string = ""
    for i in range(len(strarr)):
       current_string = ''.join(strarr[i:(i+k)])
       if (len(current_string) > len(longest_string)):
         longest_string = current_string
    return (longest_string)
