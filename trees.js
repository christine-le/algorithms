// Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = val;
  this.left = left;
  this.right = right;
}

var g = new TreeNode('g', null, null);
var f = new TreeNode('f', null, null);
var d = new TreeNode('d', null, null);
var c = new TreeNode('c', f, g);
var b = new TreeNode('b', d, null);
var a = new TreeNode('a', b, c);


// Print tree level-wise.  For example:
//           a
//         b   c
//       d    f  g

// a
// bc
// dfg
var printTree = function(a) {
  var queue = [a];
  var childList = [];
  
  console.log(a.val);
  
  while(queue.length >= 0){
    node = queue.shift();
    if (!node)
      return;
      
    if (node.left)
      childList.push(node.left);
      
    if (node.right)
      childList.push(node.right);
    
    if (queue.length === 0) {
      printList(childList);
      queue = childList;
      childList = [];
    }
  }
};

var printList = function(list) {
  arr = [];
  for (var i = 0; i < list.length; i++) {
    arr.push(list[i].val);
  }
  console.log(arr.join(''));
}
printTree(a);