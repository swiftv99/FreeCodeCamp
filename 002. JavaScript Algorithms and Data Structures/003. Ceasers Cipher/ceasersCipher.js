function rot13(str) {
	const newStr = [];
	for (let i = 0; i < str.length; i++) {
		let temp = str.charCodeAt(i);
		if ((temp >= 97 && temp <= 109) || (temp >= 65 && temp <= 77)) {
			newStr[i] = String.fromCharCode(str.charCodeAt(i) + 13);
		} else if ((temp >= 110 && temp <= 122) || (temp >= 78 && temp <= 90)) {
			newStr[i] = String.fromCharCode(str.charCodeAt(i) - 13);
		} else {
			newStr[i] = str[i];
		}
	}
	return newStr.join("");
}

rot13("SERR PBQR PNZC");
