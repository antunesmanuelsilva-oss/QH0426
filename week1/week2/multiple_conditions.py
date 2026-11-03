adventure_type = str (input('What type of adventure should i have?'))
if (adventure_type == 'scary') or (adventure_type == 'short'):
    print('Yes')
elif (adventure_type == 'scary') and (adventure_type == 'short'):
    print('No')
else:
    print('Nothing')