
class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """
    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost=1, deletion_cost=1, subst_cost=1):
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost


def distance(string_first, string_second, first, second): 
    l1 = first
    l2 = second
    # if the first string is empty the insert all 
    #characters of the second to first 
    if l1 == 0: 
         return l2 
  
    # remove all characters of the first string if the 
    # second string is empty
    if l2 == 0: 
        return l1 
  
    #Ignore the first characters if they are the same and count for
    #the remain strings.
    if string_first[l1-1]== string_second[l2-1]: 
        return distance(string_first, string_second, l1-1, l2-1) 
  
    # if the last characters differs then we apply all three operations
    # insert, remove and replace and consider the one with the minimun edit 
    # cost.
    return 1 + min(distance(string_first, string_second, l1, l2-1),    # Insert 
                   distance(string_first, string_second, l1-1, l2),    # Remove 
                   distance(string_first, string_second, l1-1, l2-1)    # Replace 
                   ) 
  
# main program to test the function above 

string1 = input("Enter the first string")
string2 = input("Enter the second String")

print( distance(string1, string2, len(string1), len(string2)))
          
            
