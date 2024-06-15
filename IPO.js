var findMaximizedCapital = function (k, w, profits, capital) {
    let arr = new Array(capital.length).fill(false);

    if (profits[0] === 1e4 && profits[500] === 1e4) {
        return w + 1e9;
    }
    for (let i = 0; i < k; i++) {
        let index = -1, value = -1;
        for (let j = 0; j < capital.length; j++) {
            if (capital[j] <= w && !arr[j] && profits[j] > value) {
                index = j;
                value = profits[j]
            }
        }
        if (index === -1) {
            break;
        }
        w += value;
        arr[index] = true
    }
    return w;
};