const buttons = document.querySelectorAll('.page-btn');

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        const current = document.querySelector('.page-btn.active');
        if (current !== btn) {
            current.classList.remove('active');
            btn.classList.add('active');
        }
    });
});

function atualizarContador() {
    const dataInicio = new Date("2025-02-19T00:00:00");
    const agora = new Date();

    // diferença em milissegundos
    let diffMs = agora - dataInicio;

    // converter para meses
    let diffMeses = (agora.getFullYear() - dataInicio.getFullYear()) * 12 +
                    (agora.getMonth() - dataInicio.getMonth());

    // criar uma data de referência para calcular os dias restantes após meses completos
    let dataTemp = new Date(dataInicio);
    dataTemp.setMonth(dataTemp.getMonth() + diffMeses);

    // se ainda não chegou na dataTemp, ajusta meses -1
    if (dataTemp > agora) {
        diffMeses--;
        dataTemp.setMonth(dataTemp.getMonth() - 1);
    }

    // agora calcula o resto em dias, horas, minutos e segundos
    let restoMs = agora - dataTemp;

    let diffDias = Math.floor(restoMs / (1000 * 60 * 60 * 24));
    restoMs -= diffDias * (1000 * 60 * 60 * 24);

    let diffHoras = Math.floor(restoMs / (1000 * 60 * 60));
    restoMs -= diffHoras * (1000 * 60 * 60);

    let diffMinutos = Math.floor(restoMs / (1000 * 60));
    restoMs -= diffMinutos * (1000 * 60);

    let diffSegundos = Math.floor(restoMs / 1000);

    // Atualiza no HTML
    document.getElementById("meses").textContent = diffMeses;
    document.getElementById("dias").textContent = diffDias;
    document.getElementById("horas").textContent = diffHoras;
    document.getElementById("minutos").textContent = diffMinutos;
    document.getElementById("segundos").textContent = diffSegundos;
}

// Atualiza a cada segundo
setInterval(atualizarContador, 1000);
atualizarContador();
