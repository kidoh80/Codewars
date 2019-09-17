/*
https://www.codewars.com/kata/56a5d994ac971f1ac500003e

You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
*/

def longest_consec(strarr, k):
    if (k > len(strarr) or k < 0):
        return('')
    longest_string = ""
    for i in range(len(strarr)):
       current_string = ''.join(strarr[i:(i+k)])
       if (len(current_string) > len(longest_string)):
         longest_string = current_string
    return (longest_string)
