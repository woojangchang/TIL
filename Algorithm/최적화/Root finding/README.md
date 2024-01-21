# 수치최적화


알고리즘 명 | 목적 | 장점| 단점
---------|----------|---------|---------
 Bisection Search | $f(x)=0$이 되게 하는 $x$ 탐색|초기 두 점의 부호가 다르면 반드시 해를 찾을 수 있음 | 비교적 오래 걸림
 Newton's Method | $f(x)=0$이 되게 하는 $x$ 탐색| 비교적 빠름 | 함수가 미분 가능해야 함
 Secant Method |$f(x)=0$이 되게 하는 $x$ 탐색 |미분 불가능한 함수에도 적용할 수 있음 | 두 지점이 함수값이 같아지면 더이상 탐색할 수 없음
 False Position Method | $f(x)=0$이 되게 하는 $x$ 탐색|미분 불가능한 함수에도 적용할 수 있음 | Bisection보다 빠르지만 다른 방법에 비해 느림
 Newton's Method(Quadratic interpolation with 2nd derivative) | $f(x)=0$이 되게 하는 $x$ 탐색|매우 빠름|함수가 미분 가능해야 함
 Golden Section Search | $f(x)$가 최소가 되게 하는 $x$ 탐색 | |최소 구간을 설정할 수 있어야 함
 Fibonacci Search |  $f(x)$가 최소가 되게 하는 $x$ 탐색 ||N을 어떻게 잡느냐에 따라 수렴 속도가 달라짐
 Lagrange Polynomial Interpolation을 이용한 최소값 탐색|$f(x)$가 최소가 되게 하는 $x$ 탐색 | |오래 걸릴 수도 있음