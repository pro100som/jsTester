let SOmTester={
	spec:[
		{
			in: [2,10],												// входные данные
			out: 1024,												// выходные данные
			description: "a^n не превышает 10^7, k не передано",	// описание теста
			TL: 100,												// ограничение времени на тест
		},
		{
			in: [7,7],
			out: 823543,
			description: "a^n не превышает 10^7, k не передано",
			TL: 100,
		},
		{
			in: [3, 27],
			out: 7484987,
			description: "a^n не превышает 10^15, k не передано",
			TL: 100,
		},
		{
			in: [7, 30],
			out: 7863249,
			description: "a^n превышает 10^15, k не передано",
			TL: 100,
		},
		{
			in: [1, 1000000000000],
			out: 1,
			description: "a=1, n > 10^10, k не передано",
			TL: 100,
		},
		{
			in: [7,7, 10000000],
			out: 823543,
			description: "a^n не превышает k",
			TL: 100,
		},
		{
			in: [7,7, 12345],
			out: 8773,
			description: "a^n не превышает 10^15",
			TL: 100,
		},
		{
			in: [7, 30, 12345],
			out: 8359,
			description: "все числа меньше 10^5",
			TL: 100,
		},
		{
			in: [54321, 1000000000000, 12345],
			out: 1131,
			description: "n > 10^10, k*a^2 < 10^15",
			TL: 100,
		},
		{
			in: [7654321, 1000000000000, 9876543],
			out: 9436393,
			description: "n > 10^10, k*a^2 > 10^15",
			TL: 100,
		},
	],
	
	parser: function (str){
		if (~str.indexOf('alert') ||
			~str.indexOf('prompt')) return new Function('','asdf');
		if (!~str.indexOf('return')) return new Function('','return ""');
		
		let res = '';
		while (str != '') {
			let i = str.indexOf('{');
			if (~i) {
				res += str.substring(0, i+1) + 'if (new Date() - startTime > TL) return "";';
				str = str.substring(i+1);
			} else {
				res += str;
				str = '';
			}
		}
		try{
			return new Function ('a, n, k, startTime, TL', res);
		} catch (err) {
			return new Function('','asdf');
		}
	},
	checker: function (unit){
		let s = SOmTester.spec;

		function check (i){
			let res;
			try{
				res = unit(s[i].in[0], s[i].in[1], s[i].in[2], startTime, s[i].TL);
				console.log(i+1,res,s[i].out);
			}  catch (err) {
				return "CE";
			}
			if (typeof res !="number") return "PE";
			if (res == s[i].out) return "OK";
			return "WA";
		}

		for (let i=0; i < s.length; i++){
			startTime = new Date();
			SOmTester.TL = s[i].TL;
			s[i].result = check(i);
			s[i].time = new Date() - startTime;
			if (s[i].time > s[i].TL){
				s[i].time = '>' + s[i].TL;
				s[i].result = "TL";
			}
			s[i].time += ' ms';
		};
	},
};