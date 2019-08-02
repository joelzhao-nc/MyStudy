alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 6}

alien_0 = alien_1
alien_0['color'] = alien_1['color']

alien_0['d_color'] = 'black'

alien_0['c_color'] = 'white'

print(alien_0['color'])
print(alien_0['points'])
print(alien_0['d_color'])
print(alien_0['c_color']) 
