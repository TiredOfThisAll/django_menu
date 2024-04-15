class Functor:
    def __init__(self, n) -> None:
        self.depth_limit = n.depth
        print(f"INIT: {str(n.value), self.depth_limit}")

    def __call__(self, n) -> None:
        print(f"CALL: {str(n.value), n.depth}")
        print(n.depth <= self.depth_limit)
        return n.depth <= self.depth_limit


class NodeStringBuilder:
    def __init__(self, tabs) -> None:
        self.tabs = tabs
        self.s = ""

    def __call__(self, n) -> None:
        self.s += " " * self.tabs * n.depth + str(n.value) + "\n"

    def result(self):
        return self.s


class NodeChildrenSetBuilder:
    def __init__(self) -> None:
            self.s = set([])

    def __call__(self, n) -> None:
        for child in n.children:
            if not child:
                continue
            self.s.add(child)

    def result(self):
        return self.s

class NodeSetBuilder:
    def __init__(self) -> None:
        self.s = set([])

    def __call__(self, n) -> None:
        self.s.add(n)

    def result(self):
        return self.s

class NodeAboveSetBuilder:
    def __init__(self, node) -> None:
        self.s = set([])
        self.node = node
        self.above = True

    def __call__(self, n) -> None:
        if not self.above:
            return
        if n == self.node:
            self.above = False
            return
        self.s.add(n)

    def result(self):
        return self.s

class HTMLBuilder:
    def __init__(self) -> None:
        self.s = "<ul>"
        self.previous_depth = 0

    def __call__(self, n) -> None:
        diff = n.depth - self.previous_depth
        self.s += "<ul>" if diff == 1 else ""
        self.s += "</ul>" if diff == -1 else ""
        self.s += f"<li><a href = '{n.value.url if n.value else 'http://127.0.0.1:8000/'}'>{(n.value if n.value else 'root')}</a></li>"
        self.previous_depth = n.depth

    def result(self):
        return self.s + "</ul>"
