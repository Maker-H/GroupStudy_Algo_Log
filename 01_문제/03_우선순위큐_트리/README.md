# 우선순위 큐, 트리

[메인으로 돌아가기](https://github.com/Maker-H/GroupStudy_Algo_Log)

이 자료구조에서는 우선순위 큐와 트리를 익히는 문제들로 뽑았습니다.

이번 🔥 문제는 구현과 응용을 적절히 섞어서 뽑아보았습니다

<br>

### 📌 읽어주세요
* 5일 기준 🔥로만 문제를 구성했습니다
* 해당 문제들은 **그래프 파트에 있는 dfs, bfs를 배우신 다음에** 푸는걸 추천드립니다. **(+ dfs를 활용한 순회)**
* 자료구조 문제들을 처음 풀어보는거라면 풀이 방법이 생소할 수 있습니다. **고민하다 안되면 답안을 확인하고 이해한 다음 다시 풀어봅시다!**

<br>

🔥 - 꼭 풀어야 하는 문제

:heavy_check_mark: - 풀어보면 좋을 문제

🚤 - 2순위 문제


<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***
## 우선순위 큐
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 01 |  🔥|<a href="https://www.acmicpc.net/problem/11279" target="_blank">11279</a>|<a href="https://www.acmicpc.net/problem/11279" target="_blank">최대 힙</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EB%9D%BC%EC%9D%B4%EB%B8%8C%20%EC%BD%94%EB%94%A9/11279.cpp)|우선순위 큐|
| 02 |  🔥|<a href="https://www.acmicpc.net/problem/2075" target="_blank">2075</a>|<a href="https://www.acmicpc.net/problem/2075" target="_blank">N번째 큰 수</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EB%9D%BC%EC%9D%B4%EB%B8%8C%20%EC%BD%94%EB%94%A9/2075.cpp)|우선순위 큐|
| 03 |  :heavy_check_mark: |<a href="https://www.acmicpc.net/problem/11723" target="_blank">11723</a>|<a href="https://www.acmicpc.net/problem/11723" target="_blank">집합</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EA%B3%BC%EC%A0%9C/11723_1.cpp)</br>[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EA%B3%BC%EC%A0%9C/11723_2.cpp)|
| 04 | :heavy_check_mark: |<a href="https://www.acmicpc.net/problem/7662" target="_blank">7662</a>|<a href="https://www.acmicpc.net/problem/7662" target="_blank">이중 우선순위 큐</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EA%B3%BC%EC%A0%9C/7662_1.cpp)</br>[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EA%B3%BC%EC%A0%9C/7662_2.cpp)|
| 05 |   |<a href="https://www.acmicpc.net/problem/3613" target="_blank">3613</a>|<a href="https://www.acmicpc.net/problem/3613" target="_blank">Java vs C++</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EA%B3%BC%EC%A0%9C/3613.cpp)|
| 06 |   |<a href="https://www.acmicpc.net/problem/2493" target="_blank">2493</a>|<a href="https://www.acmicpc.net/problem/2493" target="_blank">탑</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EA%B3%BC%EC%A0%9C/2493.cpp)|
| 07 |   |<a href="https://www.acmicpc.net/problem/11286" target="_blank">11286</a>|<a href="https://www.acmicpc.net/problem/11286" target="_blank">절댓값 힙</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/09%EC%9B%94%2014%EC%9D%BC%20-%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%20%ED%81%90/%EA%B3%BC%EC%A0%9C/11286.cpp)|


<br><br>

## 트리

|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 01 |  🔥  | <a href="https://www.acmicpc.net/problem/9934" target="_blank">9934</a> | <a href="https://www.acmicpc.net/problem/9934" target="_blank">완전 이진 트리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 02 |  🔥  | <a href="https://www.acmicpc.net/problem/14675" target="_blank">14675</a> | <a href="https://www.acmicpc.net/problem/14675" target="_blank">단절점과 단절선</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | 
| 03 |  🔥  | <a href="https://www.acmicpc.net/problem/17073" target="_blank">17073</a> | <a href="https://www.acmicpc.net/problem/17073" target="_blank">나무 위의 빗물</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 04 |  🔥  | <a href="https://www.acmicpc.net/problem/1967" target="_blank">1967</a> | <a href="https://www.acmicpc.net/problem/1967" target="_blank">트리의 지름</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/tree/1967">바로가기</a> |
| 05 |  🔥  | <a href="https://www.acmicpc.net/problem/20924" target="_blank">20924</a> | <a href="https://www.acmicpc.net/problem/20924" target="_blank">트리의 기둥과 가지</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | 
| 06 |  🔥  | <a href="https://www.acmicpc.net/problem/2250" target="_blank">2250</a> | <a href="https://www.acmicpc.net/problem/2250" target="_blank">트리의 높이와 너비</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |     
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/6416" target="_blank">6416</a> | <a href="https://www.acmicpc.net/problem/6416" target="_blank">트리인가?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/0.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11725" target="_blank">11725</a> | <a href="https://www.acmicpc.net/problem/11725" target="_blank">트리의 부모 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1991" target="_blank">1991</a> | <a href="https://www.acmicpc.net/problem/1991" target="_blank">트리 순회</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | <a href="./../solution/tree/1991">바로가기</a> |
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1068" target="_blank">1068</a> | <a href="https://www.acmicpc.net/problem/1068" target="_blank">트리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/tree/1068">바로가기</a> |
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/5639" target="_blank">5639</a> | <a href="https://www.acmicpc.net/problem/5639" target="_blank">이진 검색 트리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/3584" target="_blank">3584</a> | <a href="https://www.acmicpc.net/problem/3584" target="_blank">가장 가까운 공통 조상</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/tree/3584">바로가기</a> |
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9489" target="_blank">9489</a> | <a href="https://www.acmicpc.net/problem/9489" target="_blank">사촌</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |                   |
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/4256" target="_blank">4256</a> | <a href="https://www.acmicpc.net/problem/4256" target="_blank">트리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2263" target="_blank">2263</a> | <a href="https://www.acmicpc.net/problem/2263" target="_blank">트리의 순회</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |                   |
| 16 |                      | <a href="https://www.acmicpc.net/problem/9372" target="_blank">9372</a> | <a href="https://www.acmicpc.net/problem/9372" target="_blank">상근이의 여행</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 17 |                      | <a href="https://www.acmicpc.net/problem/20364" target="_blank">20364</a> | <a href="https://www.acmicpc.net/problem/20364" target="_blank">부동산 다툼</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                     |
| 18 |                      | <a href="https://www.acmicpc.net/problem/15900" target="_blank">15900</a> | <a href="https://www.acmicpc.net/problem/15900" target="_blank">나무 탈출</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 19 |                      | <a href="https://www.acmicpc.net/problem/15681" target="_blank">15681</a> | <a href="https://www.acmicpc.net/problem/15681" target="_blank">트리와 쿼리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/tree/15681">바로가기</a> |
| 20 |                      | <a href="https://www.acmicpc.net/problem/19641" target="_blank">19641</a> | <a href="https://www.acmicpc.net/problem/19641" target="_blank">중첩 집합 모델</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 21 |                      | <a href="https://www.acmicpc.net/problem/1240" target="_blank">1240</a> | <a href="https://www.acmicpc.net/problem/1240" target="_blank">노드사이의 거리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 22 |                      | <a href="https://www.acmicpc.net/problem/4803" target="_blank">4803</a> | <a href="https://www.acmicpc.net/problem/4803" target="_blank">트리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 23 |                      | <a href="https://www.acmicpc.net/problem/14267" target="_blank">14267</a> | <a href="https://www.acmicpc.net/problem/14267" target="_blank">회사 문화 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 24 |                      | <a href="https://www.acmicpc.net/problem/20955" target="_blank">20955</a> | <a href="https://www.acmicpc.net/problem/20955" target="_blank">민서의 응급 수술</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 25 |                      | <a href="https://www.acmicpc.net/problem/1595" target="_blank">1595</a> | <a href="https://www.acmicpc.net/problem/1595" target="_blank">북쪽나라의 도로</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 26 |                      | <a href="https://www.acmicpc.net/problem/19542" target="_blank">19542</a> | <a href="https://www.acmicpc.net/problem/19542" target="_blank">전단지 돌리기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 27 |                      | <a href="https://www.acmicpc.net/problem/21276" target="_blank">21276</a> | <a href="https://www.acmicpc.net/problem/21276" target="_blank">계보 복원가 호석</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 28 |                      | <a href="https://www.acmicpc.net/problem/2058" target="_blank">2058</a> | <a href="https://www.acmicpc.net/problem/2058" target="_blank">원자의 에너지</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 29 |                      | <a href="https://www.acmicpc.net/problem/2533" target="_blank">2533</a> | <a href="https://www.acmicpc.net/problem/2533" target="_blank">사회망 서비스(SNS)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 30 |                      | <a href="https://www.acmicpc.net/problem/11437" target="_blank">11437</a> | <a href="https://www.acmicpc.net/problem/11437" target="_blank">LCA</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> | <a href="./../solution/tree/11437">바로가기</a> |
| 31 |                      | <a href="https://www.acmicpc.net/problem/19535" target="_blank">19535</a> | <a href="https://www.acmicpc.net/problem/19535" target="_blank">ㄷㄷㄷㅈ</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 32 |                      | <a href="https://www.acmicpc.net/problem/16437" target="_blank">16437</a> | <a href="https://www.acmicpc.net/problem/16437" target="_blank">양 구출 작전</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 33 |                      | <a href="https://www.acmicpc.net/problem/12978" target="_blank">12978</a> | <a href="https://www.acmicpc.net/problem/12978" target="_blank">스크루지 민호 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 34 |                      | <a href="https://www.acmicpc.net/problem/4933" target="_blank">4933</a> | <a href="https://www.acmicpc.net/problem/4933" target="_blank">뉴턴의 사과</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 35 |                      | <a href="https://www.acmicpc.net/problem/1167" target="_blank">1167</a> | <a href="https://www.acmicpc.net/problem/1167" target="_blank">트리의 지름</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 36 |                      | <a href="https://www.acmicpc.net/problem/12896" target="_blank">12896</a> | <a href="https://www.acmicpc.net/problem/12896" target="_blank">스크루지 민호</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 37 |                      | <a href="https://www.acmicpc.net/problem/14657" target="_blank">14657</a> | <a href="https://www.acmicpc.net/problem/14657" target="_blank">준오는 최종인재야!!</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 38 |                      | <a href="https://www.acmicpc.net/problem/1949" target="_blank">1949</a> | <a href="https://www.acmicpc.net/problem/1949" target="_blank">우수 마을</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 39 |                      | <a href="https://www.acmicpc.net/problem/2233" target="_blank">2233</a> | <a href="https://www.acmicpc.net/problem/2233" target="_blank">사과나무</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 40 |                      | <a href="https://www.acmicpc.net/problem/14570" target="_blank">14570</a> | <a href="https://www.acmicpc.net/problem/14570" target="_blank">나무 위의 구슬</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 41 |                      | <a href="https://www.acmicpc.net/problem/2213" target="_blank">2213</a> | <a href="https://www.acmicpc.net/problem/2213" target="_blank">트리의 독립집합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
| 42 |                      | <a href="https://www.acmicpc.net/problem/12912" target="_blank">12912</a> | <a href="https://www.acmicpc.net/problem/12912" target="_blank">트리 수정</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
| 43 |                      | <a href="https://www.acmicpc.net/problem/19581" target="_blank">19581</a> | <a href="https://www.acmicpc.net/problem/19581" target="_blank">두 번째 트리의 지름</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |                      |
| 44 |                      | <a href="https://www.acmicpc.net/problem/4315" target="_blank">4315</a> | <a href="https://www.acmicpc.net/problem/4315" target="_blank">나무 위의 구슬</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/16.svg"/> |                      |