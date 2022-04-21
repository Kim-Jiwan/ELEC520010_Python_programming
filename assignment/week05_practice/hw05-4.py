# 2017110292 김지완

n_list = list(map(int, input("5개의 수를 입력하세요 : ").split()))

print(f'합 : {sum(n_list)}')
print(f'평균 : {sum(n_list) / len(n_list)}')
print(f'최댓값 : {max(n_list)}')
print(f'최솟값 : {min(n_list)}')


''' 빈 리스트에 append() method 사용하는 코드입니다.
m_list = []
m0, m1, m2, m3, m4 = map(int, input("5개의 수를 입력하세요:").split())

m_list.append(m0)
m_list.append(m1)
m_list.append(m2)
m_list.append(m3)
m_list.append(m4)

print(f'합 : {sum(m_list)}')
print(f'평균 : {sum(m_list) / len(m_list)}')
print(f'최댓값 : {max(m_list)}')
print(f'최솟값 : {min(m_list)}')
'''

