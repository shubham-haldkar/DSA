class TreeNode:
    def __init__(self,data) :
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self,child):
        child.parent = self
        self.children.append(child)
    
    def getLevel(self):
        level = 0 
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level
    
    def showTree(self):
        spaces = " "*self.getLevel()*2
        prefix = spaces + "|--"if self.parent else""
        print(prefix ,self.data)

        if self.children:
            for child in self.children:
                child.showTree()
                

def build_product_tree():
    root = TreeNode("Computer")
    
    hardware = TreeNode("Hardware")
    hardware.addChild(TreeNode("Moniter"))
    hardware.addChild(TreeNode("Keyboard"))
    hardware.addChild(TreeNode("Mouse"))
    hardware.addChild(TreeNode("CPU"))

    software = TreeNode("Software")
    software.addChild(TreeNode("System Software"))
    software.addChild(TreeNode("Application Software"))
    software.addChild(TreeNode("Utility Software"))

    
    root.addChild(hardware)
    root.addChild(software)
     
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.showTree()
    