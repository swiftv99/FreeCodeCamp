function convertToRoman(num) {
	let str = "" + num;
	let result = "";
	let birlik = "",
		onlik = "",
		yuzlik = "",
		minglik = "";
	const roman = ["I", "V", "X", "L", "C", "D", "M", "H"];
	if (str.length == 0) {
		return undefined;
	} else if (str.length > 0) {
		switch (str[str.length - 1]) {
			case "1":
				birlik = "I";
				break;
			case "2":
				birlik = "II";
				break;
			case "3":
				birlik = "III";
				break;
			case "4":
				birlik = "IV";
				break;
			case "5":
				birlik = "V";
				break;
			case "6":
				birlik = "VI";
				break;
			case "7":
				birlik = "VII";
				break;
			case "8":
				birlik = "VIII";
				break;
			case "9":
				birlik = "IX";
				break;
		}
		if (str.length > 1) {
			switch (str[str.length - 2]) {
				case "1":
					onlik = "X";
					break;
				case "2":
					onlik = "XX";
					break;
				case "3":
					onlik = "XXX";
					break;
				case "4":
					onlik = "XL";
					break;
				case "5":
					onlik = "L";
					break;
				case "6":
					onlik = "LX";
					break;
				case "7":
					onlik = "LXX";
					break;
				case "8":
					onlik = "LXXX";
					break;
				case "9":
					onlik = "XC";
					break;
			}
		}
		if (str.length > 2) {
			switch (str[str.length - 3]) {
				case "1":
					yuzlik = "C";
					break;
				case "2":
					yuzlik = "CC";
					break;
				case "3":
					yuzlik = "CCC";
					break;
				case "4":
					yuzlik = "CD";
					break;
				case "5":
					yuzlik = "D";
					break;
				case "6":
					yuzlik = "DC";
					break;
				case "7":
					yuzlik = "DCC";
					break;
				case "8":
					yuzlik = "DCCC";
					break;
				case "9":
					yuzlik = "CM";
					break;
			}
		}
		if (str.length > 3) {
			switch (str[str.length - 4]) {
				case "1":
					minglik = "M";
					break;
				case "2":
					minglik = "MM";
					break;
				case "3":
					minglik = "MMM";
					break;
			}
		}
	}

	result = minglik.concat(yuzlik, onlik, birlik);
	console.log(result);
	return result;
}

convertToRoman(36);
