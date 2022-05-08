import numpy as np
from collections import OrderedDict


class Cube:
    def __init__(self, name):
        self.name = name
        self.dimensions = Dimensions()
        self.root = {}
        self.columns = {}
        self.rows = {}

    def compile(self):
        for e in self.dimensions[2].elements:
            self.columns[e.name] = e.key
            print("Col {0},{1}".format(e.key, e.name))

        for e in self.dimensions[3].elements:
            self.rows[e.name] = e.key
            print("Row {0},{1}".format(e.key, e.name))

    def write_value(self, value: float, dims: list):
        if len(dims) != self.dimensions.count():
            raise ValueError('Invalid number of dimensions (should be {0})!'.format(self.dimensions.count()))

        page = self.root

        # year
        if dims[0] not in page:
            page[dims[0]] = {}
            print("add page for {0}:{1}".format(self.dimensions[0].name, dims[0]))
        page = page[dims[0]]

        # period

        if dims[1] not in page:
            print("add final page for {0}:{1}".format(self.dimensions[1].name, dims[1]))

            page[dims[1]] = np.zeros((self.dimensions[2].elements.count(), self.dimensions[3].elements.count()))

        page = page[dims[1]]

        page[
            self.columns[dims[2]],
            self.rows[dims[3]]
        ] = value

        print(self.root)


class Dimension:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description if description != "" else name
        self.elements = Elements()


class Dimensions:
    def __init__(self):
        self.list = []

    def add(self, dim: Dimension):
        self.list[dim.name] = dim

    def add(self, dims: list[Dimension]):
        for d in dims:
            self.list.append(d)

    def count(self) -> int:
        return len(self.list)

    def __iter__(self):
        return self.list.__iter__()

    def __getitem__(self, item):
        return self.list[item]


class Elements:
    def __init__(self):
        self.list = {}

    def add(self, name):
        self.list[name] = Element(len(self.list), name)

    def add(self, names=[]):
        for e in names:
            self.list[e] = Element(len(self.list), e)

    def count(self) -> int:
        return len(self.list)

    def __iter__(self):
        return self.list.values().__iter__()


class Element:
    def __init__(self, key, name):
        self.key = key
        self.name = name
