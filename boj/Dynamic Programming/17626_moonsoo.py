import sys
import math
input= sys.stdin.readline

n = int(input())

dp = [4] * 50001 # 모두 최대 개수인 4로 초기화
dp[0] = 0
dp[1] = 1

"""
라그랑주 정리가 최대 네 개의 제곱수의 합으로 모든 수를 만들 수 있고
앞의 세 개의 제곱수의 합도 하나의 값으로 묶는다면

N =  a^2 + b^2 + c^2  + d^2
  = (a^2 + b^2 + c^2) + d^2
  =  A + B^2 
  의 합으로 생각할 수 있다.

이렇게 하면
dp[N] = min(dp[A] + dp[B^2])
      = min(dp[A] + 1) 
      의 경우의 수를 찾으면 된다. (dp[B^2]은 제곱수이기 때문에 1이므로)

B를 1부터 대입해가며 테스트하면
ex)
170 = 169 + 1^2 = 13^2 + 1^2
    = 166 + 2^2
    = ...

dp[170] = dp[169 (=13^2)] + dp[1 (=1^2)] = 2로 찾을 수 있게 된다.
"""


for N in range(1, n + 1):
    # 1부터 n까지 채워나간다

    if math.sqrt(N) % 1 == 0:
        # if N == a^2 인 경우, 하나의 수의 제곱으로만 표현 가능
        dp[N] = 1
    else:
        for i in range(1, int(math.sqrt(N)) + 1):
            # i의 제곱만 조회함으로써 조회 횟수를 줄였다

            dp[N] = min(dp[N], dp[i*i] + dp[N - i*i])
            # 기존값과 비교하여 최소의 경우 찾기

            if dp[N] == 2:
                # 2를 찾으면 최소이기 때문에 불필요한 실행 없애기
                break
        
        """
        # 처음에 시도했던 방식인데 시간초과가 났다. 그런데 위의 코드도 python3에서는 시간 초과였지만 pypy에서는 잘 되는거로 보아 그 차이일지도..?
        # !! 괜찮은 방식이라고 생각했는데 시간 초과가 난다. 반복문을 너무 길게 돌아서 그런거 같아 반복횟수를 줄이는 방향으로 다시 짜보았다
        for i in range(1, N//2 + 1):
            # 절반까지만 반복해도 모든 케이스 조회 가능 (앞 뒤만 바뀌는 것이기 때문에)
            # 짝수일 경우, ex) N=4이면 i=2까지 조회
            # 홀수일 경우, ex) N=5이면 i=2까지 조회
            dp[N] = min(dp[N], dp[i] + dp[N - i])

            if dp[N] == 2:
                # 2를 찾으면 최소이기 때문에 불필요한 실행 없애기
                break
        """




print(dp[n])