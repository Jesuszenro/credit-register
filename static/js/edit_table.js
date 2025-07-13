function enableEdit(id) {
    const clientTd = document.getElementById(`client-${id}`);
    const amountTd = document.getElementById(`amount-${id}`);
    const interestTd = document.getElementById(`interest-${id}`);
    const termTd = document.getElementById(`term-${id}`);
    const dateTd = document.getElementById(`date-${id}`);

    const client = clientTd.innerText.trim();
    const amount = amountTd.innerText.trim().replace('$', '');
    const interest = interestTd.innerText.trim().replace('%', '').trim();
    const term = termTd.innerText.trim();
    const date = dateTd.innerText.trim();

    clientTd.innerHTML = `<input type="text" name="client" value="${client}">`;
    amountTd.innerHTML = `<input type="number" step="0.01" name="amount" value="${amount}">`;
    interestTd.innerHTML = `<input type="number" step="0.01" name="interest_rate" value="${interest}">`;
    termTd.innerHTML = `<input type="number" name="term" value="${term}">`;
    dateTd.innerHTML = `<input type="text" name="grant_day" value="${date}">`;

    const row = document.getElementById(`row-${id}`);
    const actionsTd = row.querySelector('td:last-child');

    actionsTd.innerHTML = `
        <form method="post" action="/update_inline/credits/${id}" style="display:inline;">
            <input type="hidden" name="client" value="${client}">
            <input type="hidden" name="amount" value="${amount}">
            <input type="hidden" name="interest_rate" value="${interest}">
            <input type="hidden" name="term" value="${term}">
            <input type="hidden" name="grant_day" value="${date}">
            <button type="submit" class="btn">Save</button>
        </form>
        <button type="button" onclick="cancelEdit(${id})" class="btn">Cancel</button>
    `;

    const inputs = row.querySelectorAll('input[type="text"], input[type="number"]');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            actionsTd.querySelector('input[name="client"]').value = row.querySelector('input[name="client"]').value;
            actionsTd.querySelector('input[name="amount"]').value = row.querySelector('input[name="amount"]').value;
            actionsTd.querySelector('input[name="interest_rate"]').value = row.querySelector('input[name="interest_rate"]').value;
            actionsTd.querySelector('input[name="term"]').value = row.querySelector('input[name="term"]').value;
            actionsTd.querySelector('input[name="grant_day"]').value = row.querySelector('input[name="grant_day"]').value;
        });
    });
}

function cancelEdit(id) {
    location.reload();
}
