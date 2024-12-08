import platform

# help(platform) #tlumaczy wszystko na temat platform

print(platform.machine())
print(platform.processor())

print(platform.system())
print(platform.version())
print()
print(platform.python_implementation()) #na jakiej preferencyjnej implementacji pythonia dzialamy :) :D
print(platform.python_version_tuple()) #poda wersje w krotce/tuple