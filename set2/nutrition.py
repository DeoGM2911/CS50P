while True:
    fruit = input('Item: ')
    if fruit == '1': break
    fda_poster = {'apple':'130',"avocado":'50','banana':'110',
                'cantaloupe':'50', 'grapefruit':'60', 'grapes':'90',
                'honeydew melon':'50', 'kiwifruit':'90','lemon':'15',
                'lime':'20','nectarine':'60','orange':'80','peach':'60',
                'pear':'100','pineapple':'50','plums':'70','strawberries':'50',
                'sweet cherries':'100','tagerine':'50','watermelon':'80'}
    friut_mame = fruit.lower()
    if friut_mame in fda_poster.keys():
        print(f'Calories: {fda_poster[friut_mame]}')
    else:
        print('Not available! Please retry!')