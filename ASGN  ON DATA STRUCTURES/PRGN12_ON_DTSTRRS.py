#12)	Get the key corresponding to the minimum value from the following dictionary
sampleDict = { 'Physics': 82,'Math': 65,  'history': 75}
key_list = list(sampleDict.keys())
val_list = list(sampleDict.values())
position = val_list.index(65)
print(key_list[position])
