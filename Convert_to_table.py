import pprint as pp
tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']
              ]


for rows in zip(*tableData):
    print('{:<10}''{:<10}''{:>5}'.format(*rows))
