const expressionInput = document.getElementById('expression');
const resultDisplay = document.getElementById('result');
const calculateButton = document.getElementById('calculate');

calculateButton.addEventListener('click', () => {
    const expr = expressionInput.value;
    try {
        const result = eval(expr);
        resultDisplay.textContent = `Result: ${result}`;
    } catch (err) {
        resultDisplay.textContent = 'Error: Invalid expression';
    }
});
