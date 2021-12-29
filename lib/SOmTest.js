"use strict"
let SOmTest = {
	createElement: function (eTag, eParent, eClass, eHtml){
		eTag = eTag || 'div';
		eParent = eParent || document.body;
		let element = document.createElement(eTag);
		eParent.appendChild(element);
		if (eClass)
			if (typeof eClass == 'string') element.classList.add(eClass);
			else
				for (let i=0; i<eClass.length; i++) element.classList.add(eClass[i]);
		if (eHtml) element.innerHTML = eHtml;
		return element;
	},
	
	deleteElement: function (eClass, eParent){
		eParent = eParent || document.body;
		let element = eParent.getElementsByClassName(eClass);
		for (let i=0; i<element.length; i++)
			element[i].remove();
	},
	
	createTask: function (spec, tParent){
		spec = spec || SOmTest.spec;
		let task = spec.task;
		tParent = tParent || document.body;
		this.deleteElement('input', tParent);
		let main = this.createElement('div', tParent, 'input');
			this.createElement('h2', main, 'input__header', 'Задание ' + task.N + '. Функция ' + task.name + '(' + task.in + ')');
			this.createElement('p', main, 'input__task', task.text);
			let restrict = this.createElement('ul', main, 'input__restrict', 'При выполнении задания запрещены операции:');
				for (let i = 0; i<task.restrict.length; i++)
					this.createElement('li', restrict, 'input__restrOp', task.restrict[i]);
			let input = this.createElement('ul', main, 'input__data', 'Передаваемые параметры:');
				for (let i = 0; i<task.input.length; i++)
					this.createElement('li', input, 'input__data', task.input[i]);
			let output = this.createElement('ul', main, 'input__data', 'Возвращаемое значение:');
				for (let i = 0; i<task.output.length; i++)
					this.createElement('li', output, 'input__data', task.output[i]);
			this.createElement('p', main, 'input__funcH', 'function ' + task.name + '(' + task.in + '){');
			let textArea = this.createElement('textarea', main, 'input__inp');
				 textArea.placeholder = 'insert your code here';
				 textArea.value = localStorage.getItem('SOmTestLastCheck_' + spec.task.N);
			this.createElement('p', main, 'input__funcB', '}');
			let chButton = this.createElement('input', main, 'input__check');
				chButton.type = 'button';
				chButton.value = 'Проверить результат';
				let self = this;
				chButton.addEventListener('click', function(){
					self.startCheck (spec, textArea.value);
				});
	},
	createResult: function (test, rParent){
		rParent = rParent || document.body;
		this.deleteElement('result', rParent);
		let main = this.createElement('div', rParent, 'result');
			let table = this.createElement('table', main, 'result__table');
				let header = this.createElement('tr', table, 'result__header');
					this.createElement('th', header, 'result__headN', 'Номер');
					this.createElement('th', header, 'result__headDescr', 'Описание');
					this.createElement('th', header, 'result__headT', 'Время');
					this.createElement('th', header, 'result__headRes', 'Результат');
				for (let i=0; i<test.length; i++){
					let row = this.createElement('tr', table, 'result__item');
						this.createElement('td', row, 'result__testN', i+1);
						this.createElement('td', row, 'result__testDescr', test[i].description);
						this.createElement('td', row, 'result__testT', test[i].time);
						let resClass = ['result__testRes'];
						if (test[i].result == 'OK') resClass.push('result__testRes--OK');
						this.createElement('td', row, resClass, test[i].result);
				}
	},
	functionCreator: function (str, input, restrict){
		function restrCheck (str, restrict){
			if (typeof restrict == 'string'){
				if (~str.indexOf(restrict)) return true;
			} else if (typeof restrict == 'object') {
				for (let i=0; i<restrict.length; i++)
					if (~str.indexOf(restrict[i])) return true;
			};
			return false;
		};
		if (restrCheck (str, restrict)) return 'RT';
		if (!~str.indexOf('return')) return 'PE';

		let res = '';
		for (let i=0; i<input.length; i++){
			res += 'let ' + input[i] + '=SOmTestInput[' + i + '];';
		}
		while (str != '') {
			let i = str.indexOf('for');
			let wh = str.indexOf('while');
			if (~wh && wh < i || !~i) i = wh;
			if (~i) {
				for (; str[i]!='('; i++); i++;
				let count = 1;
				for (; count>0; i++)
					if (str[i]=='(') count++;
					else if (str[i]==')') count--;
				for (; str[i] == ' ' || str[i] == `
`; i++);												//отступов не добавлять!!! хак с введением ENTER, пока не разберусь, как по нормальному сделать
				res += str.substring(0, i+1)
				if (str[i]=='{') res += 'if (new Date() - startTime > TL) return "";';
				str = str.substring(i+1);
			} else {
				res += str;
				str = '';
			}
		}
		try{
			return new Function ('SOmTestInput, startTime, TL', res);
		} catch (err) {
			console.log('function constructor error', err);
			return 'CE';
		}
	},
	checker: function (unit, spec){
		console.clear();
		let check = {
			'boolean': function (res, out){
				if (typeof res != 'boolean') return "PE";
				if (res === out) return "OK";
				return "WA";
			},
			'number': function (res, out, e){
				if (typeof res != 'number') return "PE";
				if (Math.abs(res-out) <= e) return "OK";
				return "WA";
			},
			'string': function (res, out){
				if (typeof res != 'string') return "PE";
				if (res === out) return "OK";
				return "WA";
			},
			'object': function (res, out){
				if (typeof res != 'object') return "PE";
				for (let key in out){
					if (out[key] !== res[key]) return "WA";
				}
				return "OK";
			},
			'array': function (res, out){
				if (typeof res != 'object') return "PE";
				if (!res.length) return "PE";
				if (res.length != out.length) return "WA";
				for (let i=0; i<out.length; i++)
					if (out[i] != res[i]) return "WA";
				return "OK";
			},
			'NaN': function (res, out){
				if (res != res) return "OK";
				return "PE";
			},
			'undefined': function (res, out){
				if (res === undefined) return "OK";
				return "PE";
			},
		};
		for (let i=0; i<spec.test.length; i++){
			if (typeof unit == 'string'){
				spec.test[i].result = unit;
				spec.test[i].time = '';
			} else {
				let TL = spec.test[i].TL || spec.TL || 100;
				let outType = spec.test[i].outType || spec.outType || 'string';
				let e = spec.test[i].e || spec.e || 0;
				try{
					let startTime = new Date();
					let res = unit (spec.test[i].in, startTime, TL);
					let time = new Date() - startTime;
					if (time<TL){
						spec.test[i].time = time + ' ms';
						spec.test[i].result = check[outType](res, spec.test[i].out, e);
					} else {
						spec.test[i].result = 'TL';
						spec.test[i].time = '>' + TL + ' ms';
					};
console.log(i+1,res,spec.test[i].out,spec.test[i].result);
				} catch (err) {
					console.log('error in test ' + (i+1) + ': ', err);
					spec.test[i].result = 'RE';
				};
			};
		};
	},
	initTask: function (spec, tParent){
		spec = spec || this.spec;
		tParent = tParent || document.body;
		this.deleteElement('SOmTest', document.body);
		this.wrapper = this.createElement('div', tParent, 'SOmTest');
			this.createTask (spec, this.wrapper);
	},
	startCheck: function(spec, str){
		localStorage.setItem('SOmTestLastCheck_' + spec.task.N, str);
		if (str) {
			spec = spec || this.spec;
			let unit = this.functionCreator(str, spec.task.in, spec.task.restrict);
			this.checker (unit, spec);
			this.createResult(spec.test, this.wrapper);
		};
	},
};