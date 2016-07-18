module DataStructures
  
  BSTNode = Struct.new(:value, :left_node, :right_node)
  
  class BinarySearchTree
    attr_accessor :root

    def initialize(root = nil)
      @root = BSTNode.new(root, nil, nil) unless root.nil?
    end

    def insert(value)
      node = BSTNode.new(value, nil, nil)
      @root = node and return if @root.nil?
      insert_at_node(@root, node)
    end

    def insert_at_node(tree, node)
      # if tree node is nil, make it new node
      tree = node and return if tree.nil?

      # if tree node and new node have same value, return tree
      return tree if tree.value == node.value

      # if node val is less than tree val
      if node.value < tree.value
        # if there's a value to left of tree, move down and try to insert again
        return insert_at_node(tree.left_node, node) unless tree.left_node.nil?
        # insert node to left of tree node
        return tree.left_node = node
      end

      # same things as above, but to the right, if the node.val > tree.val
      return insert_at_node(tree.right_node, node) unless tree.right_node.nil?
      return tree.right_node = node
    end

    def path_to_value(value)
      return [value] if @root.value == value
      path = []
      curr = @root
      while true
        if curr.value < value && !curr.right_node.nil?
          path.push(curr.value)
          curr = curr.right_node
          next
        elsif curr.value > value && !curr.left_node.nil?
          path.push(curr.value)
          curr = curr.left_node
          next
        elsif curr.value == value
          return path
        else
          return nil
        end
      end
    end
  end

end

def initializer(list)
  tree = DataStructures::BinarySearchTree.new(list.shift)
  list.map {|el| tree.insert(el)}
  return tree
end

require 'pry'

tree = initializer([30, 52, 8, 3, 20, 10, 29])
line = "3 29"
nums = line.split(" ").map{|el| el.to_i }
path_one = tree.path_to_value(nums[0])
path_two = tree.path_to_value(nums[1])
overlap = path_one || path_two
puts overlap[-1]

