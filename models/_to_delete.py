import pandas as pd
import time
 
def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer

orig_list = [1,-4,5,-7,4,3,-5,6,13,-21]
list_as_series = pd.Series(orig_list)

#### OPTION 1 : Using Pandas Series object
# # consecutive two terms
# print(list_as_series.rolling(2).sum())

# # consecutive three terms
# print(list_as_series.rolling(3).sum())

# # consecutive four terms
# print(list_as_series.rolling(4).sum())

#### OPTION 2 : for-loop

orig_list = [1,-4,5,-7,4,3,-5,6,13,-21]
def rolling(ownlist, window):
    for i in range(len(ownlist) - window):
        subset = ownlist[i:i+window]
        print("{} {:>10} {:10}".format(i,",".join(str(j) for j in subset),sum(subset)))

# rolling(orig_list, 2)

orig_list = [1,-4,5,-7,4,3,-5,6,13,-21]

@timerfunc
def which_max_combi(ownlist):
    container = []
    for window in range(1, len(ownlist) + 1):
        max_sum, winning_combi = sum(ownlist), ""
        for i in range(0,len(ownlist) + 1 - window):
            subset = ownlist[i : i + window]
            if sum(subset) >= max_sum:
                max_sum, winning_combi = sum(subset), ", ".join(str(j) for j in subset)
        container.append([window, winning_combi, max_sum])
    return pd.DataFrame(container, columns = ['Number of Terms','Winning Combination','Sum'])

    # return "The combination with the highest sum is [{}] with a sum of {}".format(winning_combi,max_sum)
print(which_max_combi(orig_list))

@timerfunc
def which_max_combi_perm(ownlist):
    container = []
    for window in range(1, len(ownlist) + 1):
        for i in range(0,len(ownlist) + 1 - window):
            subset = ownlist[i : i + window]
            max_sum, winning_combi = sum(subset), ", ".join(str(j) for j in subset)
            container.append([window, subset, max_sum])
    return pd.DataFrame(container, columns = ['Number of Terms','Winning Combination','Sum'])

print(which_max_combi_perm(orig_list))