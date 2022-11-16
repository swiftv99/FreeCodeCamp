function telephoneCheck(str) {
	let regex1 = /[1]\s[(]\d{3}[)]\s\d{3}[-]\d{4}/; // 1 (555) 555-5555
	let regex2 = /[1][(]\d{3}[)]\d{3}[-]\d{4}/; // 1(555)555-5555
	let regex3 = /[1]\s\d{3}[-]\d{3}[-]\d{4}/; // 1 555-555-5555
	let regex4 = /[1]\s\d{3}\s\d{3}\s\d{4}/; // 1 555 555 5555
	let regex5 = /[(]\d{3}[)]\s\d{3}[-]\d{4}/; // (555) 555-5555
	let regex6 = /[(]\d{3}[)]\d{3}[-]\d{4}/; // (555)555-5555
	let regex7 = /\d{3}\s\d{3}\s\d{4}/; // 555 555 5555
	let regex8 = /\d{3}[-]\d{3}[-]\d{4}/; // 555-555-5555
	let regex9 = /\d{10}/; // 5555555555

	if (str.length > 16) return false;
	else if (str.length == 11 || str.length == 15 || str.length < 10)
		return false;
	else if (str.length == 16 && str.match(regex1)) return true;
	else if (
		str.length == 14 &&
		(str.match(regex2) ||
			str.match(regex3) ||
			str.match(regex4) ||
			str.match(regex5))
	)
		return true;
	else if (str.length == 13 && str.match(regex6)) return true;
	else if (str.length == 12 && (str.match(regex7) || str.match(regex8)))
		return true;
	else if (str.length == 10 && str.match(regex9)) return true;
	else return false;
}
telephoneCheck("(555)-555-5555");
