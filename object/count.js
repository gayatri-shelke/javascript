// Q32.Write a Python program to get the key, value and item in a dictionary.
// dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
// Sample Output:

// key  value  count                                                                                             
// 1     10      1                                                                                               
// 2     20      2                                                                                               
// 3     30      3                                                                                               
// 4     40      4                                                                                               
// 5     50      5                                                                                               
// 6     60      6

// dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
// count=0
// for( i in dict_num){
//     count=count+1
//     console.log(i,dict_num[i],count);
// }

// Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
// Original dictionary of lists:
dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
d={}
for(i in dic){
    for(j in dic){
        d[dic[i]]=({i:dic[j]})
        console.log(d);

    }
}
// Split said dictionary of lists into list of dictionaries:
// [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
