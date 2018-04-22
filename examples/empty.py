import pyblueprint.blueprint

b = pyblueprint.blueprint.BluePrint(filename="/tmp/empty.svg")
b.save()

b = pyblueprint.blueprint.BluePrint(filename="/tmp/hello.svg")
b.text("Hello")
b.save()

b = pyblueprint.blueprint.BluePrint(filename="/tmp/square.svg")
b.square()
b.save()
