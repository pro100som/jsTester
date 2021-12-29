SOmTest.spec={
	task:{
		N: 1,																	// номер задания, используется при сохранении последней отправки
		name: 'isNumber',														// имя функции
		in: [																	// входные параметры
			'a',
		],
		text: 'Написать функцию, Проверяющую, является ли <i>a</i> числом.',	// текст задания
		restrict: [																// перечень запрещенных операций
			'alert',
			'prompt',
		],
		input: [																// описание входных данных
			'переменная <i>a</i>.',
		],
		output: [																// описание выходных данных
			'передано число - вернуть <i>true</i>',
			'передано не число - вернуть <i>false</i>',
		],
	},
	TL: 20,																		// default ограничение по времени (мс)
	outType: 'boolean',															// default тип возвращаемого значения
// поддерживаемые типы: 'boolean', 'number', 'string', 'object', 'array', 'NaN', 'undefined'
// в разработке "сложные" объекты и многомерные массивы
	test:[
		{
			in: [														// входные данные
				"20",
			],
			out: true,													// выходные данные
			outType: 'boolean',											// тип возвращаемого значения (если не указано, используется default outType)
			description: "целое положительное число в виде строки",		// описание теста
			TL: 20,														// ограничение времени на тест (если не указано, используется default TL)
		},
		{
			in: [
				"-30",
			],
			out: true,
			description: "целое отрицательное число в виде строки",
		},
		{
			in: [
				-30,
			],
			out: true,
			description: "целое отрицательное число",
		},
		{
			in: [
				"0",
			],
			out: true,
			description: "ноль в виде строки",
		},
		{
			in: [
				0,
			],
			out: true,
			description: "ноль",
		},
		{
			in: [
				"123.456",
			],
			out: true,
			description: "действительное положительное число в виде строки",
		},
		{
			in: [
				123.456,
			],
			out: true,
			description: "действительное положительное число",
		},
		{
			in: [
				"-123.456",
			],
			out: true,
			description: "действительное отрицательное число в виде строки",
		},
		{
			in: [
				"",
			],
			out: false,
			description: "пустая строка",
		},
		{
			in: [
				NaN,
			],
			out: false,
			description: "NaN",
		},
		{
			in: [
				undefined,
			],
			out: false,
			description: "undefined",
		},
		{
			in: [
				null,
			],
			out: false,
			description: "null",
		},
		{
			in: [
				"123.456.789",
			],
			out: false,
			description: "Строка",
		},
		{
			in: [
				"qwerty",
			],
			out: false,
			description: "Строка",
		},
		{
			in: [
				[1,2,3],
			],
			out: false,
			description: "Массив",
		},
		{
			in: [
				{a:3, b:4},
			],
			out: false,
			description: "Объект",
		},
	],
};