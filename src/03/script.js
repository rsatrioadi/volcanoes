const Config = {
  veiMinRadius: 5,
  veiMaxWidth: 50,
}

const main = () => {
  fetchData()
    .then((data) => {
      const points = []
      const names = []
      const veis = []

      // data to chartjs format
      //data.forEach((gunung) => {
	for (var ii = 14; ii >= 0; ii--) {
		var gunung = data[ii]
        const idx = names.push(gunung['name']+' ('+gunung['elevation']+'m)') - 1
        gunung.eruptions.forEach((eruption) => {
          const start = parseInt(eruption['START'], 10)
          const vei = parseInt(eruption['VEI'], 10)
          points.push({
            y: idx,
            x: start,
          })
          veis.push(vei)
        })
      }//)

      // get vei max min
      let veiMin = Number.MAX_SAFE_INTEGER, veiMax = Number.MIN_SAFE_INTEGER
      veis.forEach((vei) => {
        if (vei < veiMin)
          veiMin = vei
        if (vei > veiMax)
          veiMax = vei
      })

      // calculate hue based on vei range
      points.forEach((point, idx) => {
        const hue = 120 - 120 * (veis[idx] - veiMin) / (veiMax - veiMin)
        point.color = `hsl(${hue}, 80%, 50%)`
      })

      visualizeData(points, names, veis)
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

const visualizeData = (points, names, veis) => {
  var scatterChart = new Chart($('#canvas'), {
    type: 'scatter',
    data: {
      datasets: [{
        data: points,
        fill: false,
        borderColor: 'transparent',
        pointBackgroundColor: points.map((point) => point.color),
        pointBorderColor: points.map((point) => point.color),
      }],
    },
    options: {
      responsive: false,
      maintainAspectRatio: false,
      animation: {
        duration: 0,
      },
      hover: {
        animationDuration: 0,
      },
      responsiveAnimationDuration: 0,
      legend: {
        display: false,
      },
      tooltips: {
        callbacks: {
          label: (tooltipItem, data) => {
            return `${names[tooltipItem.yLabel]} | Year ${tooltipItem.xLabel} | Vei ${veis[tooltipItem.index]}`
          },
        },
      },
      scales: {
        yAxes: [{
          ticks: {
            maxTicksLimit: 17,
            callback: (value) => {
              return names[value]
            },
          },
        }],
        xAxes: [{
          ticks: {
            max: 2020,
            maxTicksLimit: 33,
            callback: (value) => {
              return value > 2000 ? '' : value
            },
          },
          scaleLabel: {
            display: true,
            labelString: 'Year',
          },
        }],
      },
    },
  });
}

main()
