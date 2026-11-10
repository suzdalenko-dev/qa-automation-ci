import http from 'k6/http';
import { check } from 'k6';

export const options = {
  vus: 100, // 100 usuarios virtuales a la vez
  duration: '30s', // durante 30 segundos
};

export default function () {
  let res = http.get('https://jsonplaceholder.typicode.com/users/1');
  check(res, {
    'va bien, es 200': (r) => r.status === 200,
    'tarda menos de 500ms': (r) => r.timings.duration < 500,
  });
}