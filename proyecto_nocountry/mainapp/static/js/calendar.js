const date = new Date();
date.setDate();

const monthDays = document.querySelector('.days');

const months = [
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre'
];

document.querySelector('.date').innerHTML = months[date.getMonth()];
document.querySelector('.today').innerHTML = date.getDay();

let days = '';
for (let i = 1; i <= 31; i++) {
    days += i;
    monthDays.innerHTML = days;
}