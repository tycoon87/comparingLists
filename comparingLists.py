#l1 = ['celery','carrots','bread','milk']
#l2 = ['celery','carrots','bread','cream']
#
#def compare(arr):
#    for i in l1:
#        for j in l2:
#            if i == j:
#                print "true"
#            
#compare(l1, l2)
#this works in vito once i call it a function it will not take 2 peramaders....

#*****************************************************
#define function
def compare_lists(list_one, list_two):
#    if coditions list one is the same as list two
    if list_one == list_two:
#        print the folowing
        print "The lists are the same"
#        outherwise print this instead
    else:
        print "The lists are not the same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]


compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare_lists(list_one, list_two)