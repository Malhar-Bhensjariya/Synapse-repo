# Synapse-repo
#Task 1.1 : Superhero Sorting Challenge

jumbled_superheroes = ['DocToR_sTRAngE',
                       'sPidERmaN','MoOn_KnigHT',
                       'caPTAIN_aMERIca','hULK']
indices = []
decoded_names = []

# First Part: indices and decoded_names
for i,hero in enumerate(jumbled_superheroes):
    indices.append(i)
    n = hero.lower().replace('_',' ')
    decoded_names.append(n)
print("indices: ",indices)
print("decoded_names: ",decoded_names,"\n")

#Second Part: lambda and len()
length = lambda name: len(name)
name_lengths = list(map(length,decoded_names))
print("name_lengths: "name_lengths,"\n")

#Third Part: sort() and indices
indices.sort(key=lambda index: name_lengths[index])
print("Sorted indices list: \n"indices,"\n")

#Final Part: printing the superheroes list
for i in range(len(indices)):
    print("Phase 5 kickoff list: ",(i+1),". ",(decoded_names[(indices[i])].title()))

