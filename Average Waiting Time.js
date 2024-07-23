var averageWaitingTime = function(customers) {
    let n = customers.length;
    let time_waiting = customers[0][1];
    let finished_prev = customers[0][0] + customers[0][1];

    for (let customer_ind = 1; customer_ind < n; ++customer_ind) {
        let times = customers[customer_ind];
        let arrive = times[0];

        let start_cook = Math.max(arrive, finished_prev);
        let end_time = start_cook + times[1];
        finished_prev = end_time;
        time_waiting += end_time - arrive;
    }

    return time_waiting / n;
};