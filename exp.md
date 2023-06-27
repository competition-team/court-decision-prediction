# - TODO
## 3_summarized_facts
1. `first_party`, `second_party`: grouping
2. `facts`: `first_party`, `second_party`에 대한 정보를 요약 \
e.g. \
`first_party_summ`: `전과 15범, 반성 기미 없음, 살인미수, 히스패닉계열, 남성, 30세` \
`second_party_summ`: `가정주부, 흑인, 여성, 40세, 세탁소 운영`
3. 최종 features
   1. `first_party_grp`, `second_party_grp`: nominal features
   2. `first_party_summ`, `second_party_summ`: NLP input
4. 2개의 모델을 사용
   1. Nominal features: pycaret ensemble
   2. NLP input: Binary classification NLP model
5. 2개의 모델의 결과를 ensemble


# [0.51129] 2_party_group_only
`first_party`, `second_party`를 분류하여 onehot-encoding 후 pycaret 예측
