
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
