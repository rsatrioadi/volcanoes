const Config = {
	eleMinHeight: 30,
	eleMaxHeight: 300,
	veiMinWidth: 30,
	veiMaxWidth: 300,
	popMinCount: 1,
	popMaxCount: 20,
}

const main = () => {
	fetchData()
		.then((data) => {
			data = scaleNumbers(data)
			data = sortData(data)
			drawLetusan(data)
		})
		.catch((err) => {
			console.error(err)
			$('#root').html(`
				<p>error, see console log</p>
			`)
		})
}

const fetchData = () => {
	return fetch('data.json')
		.then((response) => {
			return response.json()
		})
		.then((json) => {
			return json
		})
}

const scaleNumbers = (source) => {
	const result = []

	let eleMin = Number.MAX_SAFE_INTEGER, eleMax = Number.MIN_SAFE_INTEGER
	let veiMin = Number.MAX_SAFE_INTEGER, veiMax = Number.MIN_SAFE_INTEGER
	let popMin = Number.MAX_SAFE_INTEGER, popMax = Number.MIN_SAFE_INTEGER

	source.forEach((letusan) => {
		const ele = parseInt(letusan['ELEVATION'], 10)
		const vei = parseInt(letusan['LARGEST VEI'], 10)
		const pop = parseInt(letusan['POPULATION WITHIN 10KM'], 10)
		if (ele < eleMin)
			eleMin = ele
		if (ele > eleMax)
			eleMax = ele
		if (vei < veiMin)
			veiMin = vei
		if (vei > veiMax)
			veiMax = vei
		if (pop < popMin)
			popMin = pop
		if (pop > popMax)
			popMax = pop
	})

	const rangeEleSource = eleMax - eleMin, rangeEleResult = Config.eleMaxHeight - Config.eleMinHeight
	const rangeVeiSource = veiMax - veiMin, rangeVeiResult = Config.veiMaxWidth - Config.veiMinWidth
	const rangePopSource = popMax - popMin, rangePopResult = Config.popMaxCount - Config.popMinCount

	source.forEach((letusan) => {
		const ele = parseInt(letusan['ELEVATION'], 10)
		const vei = parseInt(letusan['LARGEST VEI'], 10)
		const pop = parseInt(letusan['POPULATION WITHIN 10KM'], 10)

		result.push({
			...letusan,
			ele: Config.eleMinHeight + rangeEleResult * (ele - eleMin) / rangeEleSource,
			vei: Config.veiMinWidth + rangeVeiResult * (vei - veiMin) / rangeVeiSource,
			pop: Config.popMinCount + rangePopResult * (pop - popMin) / rangePopSource,
		})
	})

	return result
}

const sortData = (source) => {
	sortby = $("#DdlSort").val()
	result = []

	result = source.sort(function (a, b) {
		aint = parseInt(a[sortby], 10)
		bint = parseInt(b[sortby], 10)
	    return bint - aint
	})

	return result
}

const drawLetusan = (data) => {
	$('#root').empty()
	//data.forEach((letusan) => {
	for (var ii = 0; ii < 20; ii++) {
		var letusan = data[ii]
		const { ele, vei, pop } = letusan
		const nama = letusan['NAME']
		const year = letusan['LARGEST YEAR']

		const $pop = $('<div class="pop"></div>')
		const $letusan = (
			$('<div class="letusan"></div>')
				.append(
					$(`
						<p class="label">
							<b>${nama}</b> ${year}</br>
						</p>
					`)
				)
				.append(
					$(`
						<div class="vei">
							<img src="erup.png">
						</div>
					`).css({ width: vei, height: 624 * vei / 1000 })
				)
				.append(
					$(`
						<div class="ele">
							<img src="volc.png">
						</div>
					`).css({ height: ele, width: 1000 * ele / 721 })
				)
				.append($pop)
		)

		let i
		for (i = 0; i < Math.round(pop); i++) {
			if (i > 0 && i % 5 === 0) {
				$pop.append('<br>')
			}
			$pop.append(
				$(`
					<span class="house">
						<img src="hut.png">
					</span>
				`)
			)
		}

		$('#root').append($letusan)
	}
}

main()
