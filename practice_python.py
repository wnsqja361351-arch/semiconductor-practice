
# 반도체 공정 데이터 분석 기초 연습

# 가상의 식각률 측정값 (nm/min)
etch_rates = [100, 105, 98, 102, 110]

# 측정값 개수
count = len(etch_rates)

# 평균 식각률 계산
average = sum(etch_rates) / count

# 결과 출력
print("측정 데이터:", etch_rates)
print("측정 개수:", count)
print("평균 식각률:", average, "nm/min")

# 최대 식각률
maximum = max(etch_rates)

# 최소 식각률
minimum = min(etch_rates)

# 결과 출력
print("최대 식각률:", maximum, "nm/min")
print("최소 식각률:", minimum, "nm/min")

# 식각률 측정값의 범위 계산
etch_range = maximum - minimum

# 각 측정값과 평균의 차이
deviations = [rate - average for rate in etch_rates]

# 결과 출력
print("식각률 범위:", etch_range, "nm/min")
print("평균과의 차이:", deviations)
