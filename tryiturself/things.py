käävät = ['Taulakääpä', 'Lampaankääpä', 'Pakurikääpä', 'Rikkikääpä', 'Sitruunakääpä', 'Rusokantokääpä', 'Männynkääpä', 'Aarmikääpä', 'Riehukääpä', 'Ruostekääpä', 'Pinovyökääpä', 'Punakääpä']
sorted(käävät)
käävät.reverse()
käävät.sort(reverse=True)
käävät.remove('Lampaankääpä')
käävät.pop()
del käävät[3]
käävät.insert(0, 'Viuhkokääpä')
käävät.append('Suomukääpä')

print(käävät)


print("Here are the first three items in this list:")
for kääpä in käävät[:3]:
    print(kääpä.title())

print("Here are the last three items in this list:")
for kääpä in käävät[-3:]:
    print(kääpä.title())

print("Here are the middle three items in this list:")
for kääpä in käävät[4:7]:
    print(kääpä.title())
