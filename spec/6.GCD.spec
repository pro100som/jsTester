SOmTest.spec={
	task:{
		N: 6,																	// номер задания, используется при сохранении последней отправки
		name: 'GCD',														// имя функции
		in: [																	// входные параметры
			'a',
			'b',
		],
		text: 'Написать функцию, вычисляющую наибольший общий делитель чисел <i>a</i> и <i>b</i>.',	// текст задания
		restrict: [																// перечень запрещенных операций
			'alert',
			'prompt',
		],
		input: [																// описание входных данных
			'целое число <i>a</i>.',
			'целое число <i>b</i>.',
			'в задаче гарантируется, что данные соответствуют условию',
		],
		output: [																// описание выходных данных
			'оба числа равны <i>0</i> - вернуть <i>undefined</i> ',
			'числа не равны нулю одновременно - вернуть результат вычисления наибольшего общего делителя',
		],
	},
	TL: 20,																		// default ограничение по времени (мс)
	outType: 'number',															// default тип возвращаемого значения
// поддерживаемые типы: 'boolean', 'number', 'string', 'object', 'array', 'NaN', 'undefined'
// в разработке "сложные" объекты и многомерные массивы
	e: 0,																		// default точность сравнения чисел
	test:[
		{
			in: [											// входные данные
				5,
				7,
			],
			out: 1,											// выходные данные
			outType: 'number',								// тип возвращаемого значения (если не указано, используется default outType)
			e:0,											// точность сравнения чисел (если не указано, используется default e)
			description: "простые числа",					// описание теста
			TL: 20,											// ограничение времени на тест (если не указано, используется default TL)
		},
		{
			in: [
				26,
				9,
			],
			out: 1,
			description: "взаимно простые числа",
		},
		{
			in: [
				24,
				36,
			],
			out: 12,
			description: "положительные числа, несколько итераций",
		},
		{
			in: [
				2,
				8,
			],
			out: 2,
			description: "кратные положительные числа",
		},
		{
			in: [
				7,
				7,
			],
			out: 7,
			description: "равные положительные числа",
		},
		{
			in: [
				1,
				1000000007,
			],
			out: 1,
			description: "большие числа",
		},
		{
			in: [
				1000000001,
				1000000002,
			],
			out: 1,
			description: "большие числа",
		},
		{
			in: [
				987654321,
				876543219,
			],
			out: 9,
			description: "большие числа",
		},
		{
			in: [
				0,
				7,
			],
			out: 7,
			description: "одно из чисел 0, второе положительно",
		},
		{
			in: [
				16,
				0,
			],
			out: 16,
			description: "одно из чисел 0, второе положительно",
		},
		{
			in: [
				0,
				0,
			],
			out: undefined,
			outType: 'undefined',
			description: "оба 0",
		},
		{
			in: [
				-24,
				-36,
			],
			out: 12,
			description: "оба числа отрицательны, несколько итераций",
		},
		{
			in: [
				-26,
				9,
			],
			out: 1,
			description: "одно отрицательно, другое положительно, несколько итераций",
		},
		{
			in: [
				24,
				-81,
			],
			out: 3,
			description: "одно отрицательно, другое положительно, несколько итераций",
		},
		{
			in: [
				-12,
				-12,
			],
			out: 12,
			description: "оба числа отрицательны, равны по модулю",
		},
		{
			in: [
				-12,
				12,
			],
			out: 12,
			description: "одно число отрицательны, равны по модулю",
		},
		{
			in: [
				12,
				-12,
			],
			out: 12,
			description: "одно число отрицательны, равны по модулю",
		},
		{
			in: [
				-55,
				0,
			],
			out: 55,
			description: "одно число отрицательны, другое равно 0",
		},
		{
			in: [
				0,
				-55,
			],
			out: 55,
			description: "одно число отрицательны, другое равно 0",
		},
	],
};