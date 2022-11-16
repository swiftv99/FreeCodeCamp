function palindrome(str) {
	let newStr = str
		.toLowerCase()
		.match(/[A-Za-z0-9]/g)
		.reverse()
		.join("");
	console.log(newStr);
	return newStr ===
		str
			.toLowerCase()
			.match(/[A-Za-z0-9]/g)
			.join("")
		? true
		: false;
}

palindrome("eye");
