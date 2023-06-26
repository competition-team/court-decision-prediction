# 월간 데이콘 법원 판결 예측 AI 경진대회
[https://dacon.io/competitions/official/236112](https://dacon.io/competitions/official/236112)


# 1. Install Dependencies
Use [Poetry](https://alchemine.github.io/2023/04/07/poetry.html)
```
poetry install --no-root 
```


# 2. Dataset info
```
train.csv [파일]
ID : 사건 샘플 ID
first_party : 사건의 첫 번째 당사자
second_party : 사건의 두 번째 당사자
facts : 사건 내용
first_party_winner : 첫 번째 당사자의 승소 여부 (0 : 패배, 1 : 승리)


test.csv [파일]
ID : 사건 샘플 ID
first_party : 사건의 첫 번째 당사자
second_party : 사건의 두 번째 당사자
facts : 사건 내용


sample_submission.csv [파일] - 제출 양식
ID : 사건 샘플 ID
first_party_winner : 예측한 첫 번째 당사자의 승소 여부 (0 : 패배, 1 : 승리)
```
