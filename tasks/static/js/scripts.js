$(document).ready(function() {


    var ctxnovo = $(".barras");

    var chartGraphnovo = new Chart(ctxnovo, {
        type: 'bar',
        data: {
            // Legendas das Barras
            labels: lwlabelsnojs,
            datasets: [{
                // Legenda geral - setada pra não aparecer ali no options
                label: 'Tarefas',
                // Dados a serem inseridos nas barras
                data: lwdatanojs,
                // Define as cores de preenchimento das barras
                // de acordo com sua posição no vetor
                backgroundColor: [
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(70, 235, 70, 0.7)',
                ],
                // Define as cores de preenchimento das bordas das barras
                // de acordo com sua posição no vetor
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(70, 235, 70, 1)',
                 ],
                 // Define a espessura da borda dos retângulos
                 borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Últimas 24 horas',
                fontSize: 20,
            },
            legend: {
                display: false,
            },
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMin: 0,
                        suggestedMax: 10,
                        maxTicksLimit: 5,
                    }
                }]
            },
            maintainAspectRatio: false,
        }
    });


    var ctx = $(".pizza");

    var chartGraph = new Chart(ctx, {
        type: 'pie',
        data: {
            datasets: [{
                data: datanojs,
                backgroundColor: [
                    '#34BF49', '#FF4C4C'
                ],
                label: 'Pizza party',
            }],
            labels: labelsnojs
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Status das tarefas',
                fontSize: 20,
            },
            maintainAspectRatio: false,
        }
    });

    var ctx3 = $(".linha");

    var chartGraph3 = new Chart(ctx3, {
        type: 'line',
        data: {
            // Legendas das Linhas
            labels: tpdlabelsnojs,
            datasets: [
                {
                    // Legenda
                    label: 'Criadas',
                    // Define-se a cor da linha.
                    borderColor: 'rgb(54, 162, 235)',
                    backgroundColor: 'rgba(54, 162, 235,0.3)',
                    // Dados a serem inseridos nas barras
                    data: cpddatanojs,
                },
                {
                    // Legenda
                    label: 'Concluídas',
                    // Define-se a cor da linha.
                    borderColor: 'rgb(70, 235, 70)',
                    backgroundColor: 'rgba(70, 235, 70,0.3)',
                    // Dados a serem inseridos nas barras
                    data: tpddatanojs,
                }
            ]
        },
        options: {
            title: {
                display: true,
                text: 'Última semana',
                fontSize: 20,
            },
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMin: 0,
                        suggestedMax: 10,
                        maxTicksLimit: 5,
                    }
                }]
            },
        }
    });

});