class EmployeeNode:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.left = None
        self.right = None

class EmployeeDirectory:
    def __init__(self):
        self.root = None

    def insert(self, emp_id, name):
        """
        Insert a new employee with the given employee ID and name into the BST.
        """
        if self.root is None:
            self.root = EmployeeNode(emp_id, name)
        else:
            self._insert(emp_id, name, self.root)

    def _insert(self, emp_id, name, node):
        """
        Helper function to recursively find the appropriate location
        to insert a new employee in the BST.
        """
        if emp_id < node.emp_id:
            if node.left is None:
                node.left = EmployeeNode(emp_id, name)
            else:
                self._insert(emp_id, name, node.left)
        elif emp_id > node.emp_id:
            if node.right is None:
                node.right = EmployeeNode(emp_id, name)
            else:
                self._insert(emp_id, name, node.right)

    def search(self, emp_id):
        """
        Search for an employee with the given employee ID in the BST.
        Returns the employee's name if found, or None if not found.
        """
        return self._search(emp_id, self.root)

    def _search(self, emp_id, node):
        """
        Helper function to recursively search for an employee with
        the given employee ID in the BST.
        """
        if node is None or node.emp_id == emp_id:
            return node.name
        if emp_id < node.emp_id:
            return self._search(emp_id, node.left)
        else:
            return self._search(emp_id, node.right)
