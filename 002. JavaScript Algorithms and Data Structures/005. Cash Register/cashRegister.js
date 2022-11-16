function checkCashRegister(price, cash, cid) {
	const UNIT_AMOUNT = {
		PENNY: 0.01,
		NICKEL: 0.05,
		DIME: 0.1,
		QUARTER: 0.25,
		ONE: 1.0,
		FIVE: 5.0,
		TEN: 10.0,
		TWENTY: 20.0,
		"ONE HUNDRED": 100.0,
	};

	let diff = cash - price;
	let sum = 0;
	const newArray = [];
	for (let elem of cid) {
		sum += elem[1];
	}
	sum = sum.toFixed(2);
	console.log(sum);

	if (diff > sum) {
		return { status: "INSUFFICIENT_FUNDS", change: newArray };
	} else if (diff.toFixed(2) === sum) {
		return { status: "CLOSED", change: cid };
	} else {
		cid = cid.reverse();
		for (let elem of cid) {
			let temp = [elem[0], 0];
			while (diff >= UNIT_AMOUNT[elem[0]] && elem[1] > 0) {
				temp[1] += UNIT_AMOUNT[elem[0]];
				elem[1] -= UNIT_AMOUNT[elem[0]];
				diff -= UNIT_AMOUNT[elem[0]];
				diff = diff.toFixed(2);
			}
			if (temp[1] > 0) {
				newArray.push(temp);
			}
		}
	}
	if (diff > 0) {
		return { status: "INSUFFICIENT_FUNDS", change: [] };
	}
	return { status: "OPEN", change: newArray };
}

checkCashRegister(19.5, 20, [
	["PENNY", 1.01],
	["NICKEL", 2.05],
	["DIME", 3.1],
	["QUARTER", 4.25],
	["ONE", 90],
	["FIVE", 55],
	["TEN", 20],
	["TWENTY", 60],
	["ONE HUNDRED", 100],
]);
