import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 50000,          // 5 usuarios virtuales a la vez
    duration: '10s', // durante 10 segundos
};

export default function () {
    const response = http.get('http://127.0.0.1:8000/health');

    check(response, {
        'status code is 200': (r) => r.status === 200,
        'response contains status ok': (r) => r.json('status') === 'ok',
    });

    sleep(1);
}