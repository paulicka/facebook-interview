"""
This is the EmmanuelSonja module, an homage to what started it all.

>>> tree = sample()
>>> tree.v
4

This module supplies classes:

(object)
- Node
- Visitor
-- DFSVisitor
-- BFSVisitor
- Processor
-- Printer
-- Averager
--- Denser
BFSPrinter(BFSVisitor, Printer)
DFSPrinter(DFSVisitor, Printer)
BFSAverager(BFSVisitor, Averager)
DFSAverager(DFSVisitor, Averager)
BFSDenser(BFSVisitor, Denser)
DFSDenser(DFSVisitor, Denser)


"""

class Node(object):
    def __init__(self, v, l = None, r = None):
        self.v = v
        self.left = l
        self.right = r
    def __str__(self):
        return "%s(%s,%s)" % (self.v, self.left, self.right)

class Visitor(object):
  def __init__(self, node):
    self.node = node

  def traverse(self, node = None, depth = 0, data = None):
    assert(False) # NYI
    return data

class DFSVisitor(Visitor):        
    def traverse(self, node = None, depth = 0, data = None):
        if data is None:
            data = self.data()

        if node == None:
            node = self.node
            
        data = self.process(node, depth, data)
        if node.left:
            data = self.traverse(node.left, depth + 1, data)
        if node.right:
            data = self.traverse(node.right, depth + 1, data)
            
        return data

class BFSVisitor(Visitor):
    def traverse(self, node = None, depth = 0, data = None):
        if data is None:
            data = self.data()

        queue = (
          node if isinstance(node, list) 
          else [self.node if node == None else node]
          )

        children = []
        for n in queue:
          data = self.process(n, depth, data)

          if n.left:
            children.append(n.left)
          if n.right:
            children.append(n.right)

        if len(children):
          data = self.traverse(children, depth + 1, data)
        
        return data

class Processor(object):
    def data(self):
        return None

    def process(self, node, depth, data):
      assert(False) # NYI
      return data

class Printer(Processor):
    def process(self, node, depth, data):
        print("-" * depth + str(node.v))

class Averager(Processor):
    def data(self):
        return {}
        
    def process(self, node, depth, data):
      # Array can grow really big!
        data.setdefault(depth, [])
        data[depth].append(node.v)
        return data
        
class Denser(Averager):
    def process(self, node, depth, data):
      # Fixed tuple instead of array
        data.setdefault(depth, (0,0))
        c, s = data[depth]
        data[depth] = (c + 1, s + node.v)
        return data

class BFSPrinter(BFSVisitor, Printer):
  pass

class DFSPrinter(DFSVisitor, Printer):
  pass

class BFSAverager(BFSVisitor, Averager):
  pass

class DFSAverager(DFSVisitor, Averager):
  pass

class BFSDenser(BFSVisitor, Denser):
  pass

class DFSDenser(DFSVisitor, Denser):
  pass

def sample():
  """Returns sample tree of Nodes from Emmanuel/Sonja interview

  >>> print(sample())
  4(7(10(None,None),2(None,6(2(None,None),None))),9(None,6(None,None)))
  """
  r = Node(4, 
          Node(7,
              Node(10), 
              Node(2, 
                  None, 
                  Node(6, 
                      Node(2)))),
          Node(9, 
              None,
              Node(6))
          )
  return r



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testfile("emmanuel_sonja_doctest.md")
    
