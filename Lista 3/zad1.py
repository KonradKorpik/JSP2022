litera = input()
samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
spolgloski = ['b', 'c', 'ć', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'x', 'z', 'ż', 'ź']

if (litera in samogloski):
    print("samogloska")
elif (litera in spolgloski):
    print("spolgloska")
