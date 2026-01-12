function goToMenu() {
    window.location.href = "/";
}

function activateStep(stepNo) {
    document.querySelectorAll(".step").forEach(s => s.classList.remove("active"));
    document.getElementById("step" + stepNo).classList.add("active");
}
const btn = document.getElementById("payBtn");
let isinputempty = false;
btn.addEventListener("click", (e) => {
    e.preventDefault();

    const inputs = document.querySelectorAll(".pay-input");
    let isInputEmpty = false;

    inputs.forEach(input => {
        if (input.value.trim() === "") {
            isInputEmpty = true;
        }
    });

    if (isInputEmpty) {
        alert("Please fill the form");
        return;
    }

    document.getElementById("form_cont").style.display = "none";
    startPayment();
});

function startPayment() {
    activateStep(2);
    document.getElementById("payBtn").style.display = "none";
    document.getElementById("processing").classList.remove("hidden");

    setTimeout(() => {
        activateStep(3);

        fetch("/payment/success/{{ order.id }}/")
            .then(res => res.json())
            .then(() => {
                // ⏳ wait 2 sec, then go to confirmation page
                setTimeout(() => {
                    window.location.href = "/order-confirmed/{{ order.id }}/";
                }, 2000);
            });

    }, 3000);
}