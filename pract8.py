#Practical 8 : Expression Tree from Prefix Expression
#Non-recursive Post-order Traversal and Deletion of Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#A) Construction of expression tree using a stack
def construct(prefix):
    stack = []
    operators = "+-*/^"
    for ch in reversed(prefix):      #Scan expression from right to left
        node = Node(ch)              #Create a node for each symbol
        if ch in operators:
            node.left = stack.pop()  #First popped node is left child
            node.right = stack.pop() #Second popped node is right child
        stack.append(node)           #Push the node into stack
    return stack.pop()               #Remaining node is the root


#B) Non-recursive post-order traversal using two stacks
def postorder(root):
    if root is None:
        print("Tree is empty")
        return
    stack1 = []
    stack2 = []
    stack1.append(root)              #Push root into stack1
    while len(stack1) > 0:           #Repeat until stack1 becomes empty
        node = stack1.pop()          #Pop node from stack1
        stack2.append(node)          #Push it onto stack2
        if node.left:
            stack1.append(node.left)     #Push left child onto stack1
        if node.right:
            stack1.append(node.right)    #Push right child onto stack1
    while len(stack2) > 0:           #Pop all nodes from stack2 (gives post-order)
        node = stack2.pop()
        print(node.data, end=" ")
    print()


#C) Deletion of entire tree using a stack
def delete(root):
    if root is None:
        return None
    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()           #Visit each node
        if node.left:
            stack.append(node.left)  #Add its children to the stack
        if node.right:
            stack.append(node.right)
        node.left = None             #Clear left and right references
        node.right = None
        node.data = None             #Clear node data
    return None                      #Root pointer set to None


prefix = input("Enter prefix expression (example +a*bc): ")
root = construct(prefix)
print("Expression tree constructed successfully")

print("Post-order traversal:", end=" ")
postorder(root)

root = delete(root)
print("Entire tree deleted successfully")
postorder(root)                      #Shows that tree is now empty
