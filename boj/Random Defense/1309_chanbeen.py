#약 65분 소요

N = int(input())

if N == 1:
    print(3)
    exit()

dp = [0] * (N + 1)

dp[1] = 3
dp[2] = 7

for i in range(3, N + 1):
    dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

print(dp[-1])

#DP
#N 1
#3

#N 2
# 7

#N 3
# 17

#새로 추가된 우리에 사자 배치 X + 왼쪽에 배치 + 오른쪽에 배치
#이전에 왼쪽에 놨으면 추가 우리에는 왼쪽에 배치 불가
#2번째 전에 놨던 경우의 수에서는 왼쪽이든 오른쪽이든 우리 배치 가능
#1번째 전 총 경우의 수에서 2번째 전의 경우의 수를 제외한 친구들은 직전에 왼쪽 또는 오른쪽에 추가 배치를 한 경우

#점화식
#dp[i] = dp[i - 1] + (dp[i - 2] + (dp[i - 1] - dp[i - 2]) / 2) * 2
#추가배치 X + (직전에 추가배치 안 하고 이번에 추가배치 + 직전에 추가배치하고 이번에 안 겹치게 추가배치) * 2 (왼쪽 or 오른쪽)
#식 정리) dp[i] = 2 * (dp[i - 1]) + dp[i - 2]