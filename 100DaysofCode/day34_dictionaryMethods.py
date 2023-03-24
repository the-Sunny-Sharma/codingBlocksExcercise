#https://www.w3schools.com/python/python_ref_dictionary.asp
#jr
ep = {123:54,234:67,345:56,456:34}
#sr. manager
ep2 = {567:63,678:67,789:44}
# ep apne aap ko update kr rha hai ep2 ke values se
ep.update(ep2)
print(ep,ep2)

ep.clear()
print(ep)


ep2.pop(567)
print(ep2)

#removes last key-value pair
ep2.popitem()
print(ep2)

#deletes the entire dict
# del ep
# print(ep)

del ep2[678]
print(ep2)

