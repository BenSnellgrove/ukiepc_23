class Dependency:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    
    def __hash__(self):
        return hash((self.start, self.end))
    
mesh = []
weights = {}
dependencies = {}

split = input().split();
jobs = int(split[0])
deps = int(split[1])

for i in range(deps):
    split = input.split()
    dependency = Dependency(i + 1, int(split[0]), int(split[1]))

    mesh.append(dependency)

    if dependency in weights:
        weights[dependency] += 1
    else:
        weights[dependency] = 1