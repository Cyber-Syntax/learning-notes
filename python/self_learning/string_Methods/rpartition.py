string = "Hello - World - New - sentences/trying - isitjustone"
parts = string.rpartition("-")
before, separator, after = string.rpartition("-")
before = "Hello - World - New - sentences/trying "
separator = "-"
after = " isitjustone"
parts_split = string.split("-")

print(parts)        # prints ('Hello - World - New - sentences/trying ', '-', ' isitjustone')
print(before)       # Hello - World - New - sentences/trying 
print(separator)    # -
print(after)        # isitjustone
print(parts_split)  # ['Hello ', ' World ', ' New ', ' sentences/trying ', ' isitjustone']









