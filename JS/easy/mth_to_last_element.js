String.prototype.mthToLastElement = function () {
	var mthArray = this.split(" ").reverse();
	var idx = mthArray.shift();
	if (idx > mthArray.length) {
		return undefined;
	} else {
		return mthArray[idx-1];
	}
}

console.log(line.mthToLastElement());
