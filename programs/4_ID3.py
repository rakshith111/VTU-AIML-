
import math
from collections import Counter
from pprint import pprint
import pandas as pd


def entropy(probs):
    return sum([-prob * math.log(prob, 2) for prob in probs])


def entropylist(inp):  # Entropy calculation of list of discrete val ues(YES / NO)

    cnt = Counter(inp)
    print(inp.name, cnt)
    probs = [x / len(inp) for x in cnt.values()]
    return entropy(probs)  # Call Entropy:


def igain(df, attr, target):
    print("\nInformation Gain Calculation of ", attr)
    df_split = df.groupby(attr)
    nobs = len(df.index) * 1.0
    df_agg_ent = df_split.agg(
        {target: [entropylist, lambda x: len(x) / nobs]})[target]
    df_agg_ent.columns = ['Entropy', 'PropObservations']
    new_entropy = sum(df_agg_ent['Entropy'] * df_agg_ent['PropObservations'])
    old_entropy = entropylist(df[target])
    return old_entropy - new_entropy


def id3(df, target, attribute, default=None):

    cnt = Counter(df[target])
    gainz = []
    if len(cnt) == 1:
        return next(iter(cnt))
    else:
        default = max(cnt.keys())
        for attr in attribute:
            gainz.append(igain(df, attr, target))
        maxi = gainz.index(max(gainz))
        best_a = attribute[maxi]
        tree = {best_a: {}}
        other_a = [
            i for i in attribute if i != best_a]
        for attr_val, data_subset in df.groupby(best_a):
            subtree = id3(data_subset, target,
                          other_a, default)
            tree[best_a][attr_val] = subtree
        return tree

# Classification Accuracy


def classify(instance, tree, default=None):
    attribute = next(iter(tree))  # tree.keys()[0]
    if instance[attribute] in tree[attribute].keys():
        result = tree[attribute][instance[attribute]]
        if isinstance(result, dict):  # this is a tree, delve deeper
            return classify(instance, result)
        else:
            return result  # this is a label
    else:
        return default


df_tennis = pd.read_csv('ID3.csv')

total_entropy = entropylist(df_tennis['PlayTennis'])
print("Entropy of given PlayTennis Data Set:", total_entropy)

# Predicting Attributes
attributes = list(df_tennis.columns)
print("List of Attributes:", attributes)
attributes.remove('PlayTennis')  # Remove the class attribute
print("Predicting Attributes:", attributes)

# Tree Construction

tree = id3(df_tennis, 'PlayTennis', attributes)
print("\n\nThe Resultant Decision Tree is :\n")
pprint(tree)

df_tennis['predicted'] = df_tennis.apply(classify, axis=1, args=(tree, 'No'))
print('Accuracy is:' + str(sum(df_tennis['PlayTennis'] ==
      df_tennis['predicted']) / (1.0 * len(df_tennis.index))))
