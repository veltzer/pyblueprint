import pyblueprint.blueprint

b = pyblueprint.blueprint.BluePrint(filename="empty.svg")
b.save()

b = pyblueprint.blueprint.BluePrint(filename="hello.svg")
b.text("Hello")
b.save()

b = pyblueprint.blueprint.BluePrint(filename="square.svg")
b.square()
b.save()
