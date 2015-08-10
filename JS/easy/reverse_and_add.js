var count = 1;

function reverseAndAdd (num, depth) {
	var reversed = reverseNum(num);
	if ( checkPalindrome(num + reversed) ) {
		return console.log(depth.toString() + " " + (num + reversed).toString());
	} else {
		depth++;
		reverseAndAdd((num + reversed), depth);
	}
}

function reverseNum(num) { 
	return parseInt(reverse(num.toString()));
}

function reverse(s) {
  var o = [];
  for (var i = 0, len = s.length; i <= len; i++)
    o.push(s.charAt(len - i));
  return o.join('');
}

function checkPalindrome(num) {    
		var word = num.toString()
    var l = word.length;
    for (var i = 0; i < l / 2; i++) {
        if (word.charAt(i) !== word.charAt(l - 1 - i)) {
            return false;
        }
    }
    return true;
}

reverseAndAdd(line, count);