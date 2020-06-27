import pyblueprint.blueprint

b = pyblueprint.blueprint.BluePrint()
b.save(filename="/tmp/empty.svg")

b = pyblueprint.blueprint.BluePrint()
b.text("Hello")
b.save(filename="/tmp/hello.svg")

b = pyblueprint.blueprint.BluePrint()
b.square()
b.save(filename="/tmp/square.svg")
