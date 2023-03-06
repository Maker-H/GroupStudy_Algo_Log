# UnionFind / Disjoint Set (분리집합) 

[메인으로 돌아가기](https://github.com/Maker-H/GroupStudy_Algo_Log)

이 자료구조에서는 분리집합을 익히는 문제들로 뽑았습니다.

<br>

### 📌 읽어주세요
* 4일 기준 🔥와 :heavy_check_mark:로 구성하였습니다. 
**🔥는 꼭 풀어주시고 :heavy_check_mark:는 선택에 맡기겠습니다**
* **그래프쪽의 dfs, bfs**를 공부하신 이후에 풀어주세요
* 일반적으로 분리집합을 표현하는데에는 배열을 활용한 유니언 파인드 자료구조를 사용합니다.
* 다만, 카카오 기출 문제에서 일반적인 유니언 파인드 구조를 사용하지 못하도록 전체 크기를 엄청나게 늘린 문제가 출제 되었던 만큼, 배열이 아닌 해시나 이진트리를 활용해 유니언 파인드 구조를 만들어 보는 연습도 필요합니다. 문제 푸는데 참고해주세요
* 자료구조 문제들을 처음 풀어보는거라면 풀이 방법이 생소할 수 있습니다. **1-2시간 정도 고민하다 안되면 답안을 확인하고 이해한 다음 다시 풀어봅시다!**

<br>

🔥 - 꼭 풀어야 하는 문제

:heavy_check_mark: - 풀어보면 좋을 문제

🚤 - 2순위 문제


<br>

**특이사항**
* 아기상어 : sorted(list, key=lambda x: (x[0], x[1], x[2])) 로 하면 0번째 오름차순 그 이후 1번째 원소 오름차순 그 이후 2번째 원소 오름차순으로 정렬됨

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 01 |  🔥  | <a href="https://www.acmicpc.net/problem/4195" target="_blank">4195</a> | <a href="https://www.acmicpc.net/problem/4195" target="_blank">친구 네트워크</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | <a href="./../solution/disjoint_set/4195">바로가기</a> |
| 02 |      🔥 | <a href="https://www.acmicpc.net/problem/16724" target="_blank">16724</a> | <a href="https://www.acmicpc.net/problem/16724" target="_blank">피리 부는 사나이</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
|03|  🔥  |<a href="https://www.acmicpc.net/problem/4803" target="_blank">4803</a>|<a href="https://www.acmicpc.net/problem/4803" target="_blank">트리</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/11%EC%9B%94%2023%EC%9D%BC%20-%20%EC%9C%A0%EB%8B%88%EC%98%A8%20%ED%8C%8C%EC%9D%B8%EB%93%9C/%EB%9D%BC%EC%9D%B4%EB%B8%8C%20%EC%BD%94%EB%94%A9/4803.cpp)|
| 04 |  🔥  | <a href="https://www.acmicpc.net/problem/1717" target="_blank">1717</a> | <a href="https://www.acmicpc.net/problem/1717" target="_blank">집합의 표현</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/1717">바로가기</a> |
| 05 |  🔥  | <a href="https://www.acmicpc.net/problem/16562" target="_blank">16562</a> | <a href="https://www.acmicpc.net/problem/16562" target="_blank">친구비</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/16562">바로가기</a> |
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1976" target="_blank">1976</a> | <a href="https://www.acmicpc.net/problem/1976" target="_blank">여행 가자</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/1976">바로가기</a> |
|07|  🚤  |<a href="https://www.acmicpc.net/problem/16236" target="_blank">16236</a>|<a href="https://www.acmicpc.net/problem/16236" target="_blank">아기 상어</a>|<img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/>|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/11%EC%9B%94%2023%EC%9D%BC%20-%20%EC%9C%A0%EB%8B%88%EC%98%A8%20%ED%8C%8C%EC%9D%B8%EB%93%9C/%EA%B3%BC%EC%A0%9C/16236.cpp)|
| 08 |  🚤  | <a href="https://www.acmicpc.net/problem/18116" target="_blank">18116</a> | <a href="https://www.acmicpc.net/problem/18116" target="_blank">로봇 조립</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/18116">바로가기</a> |
| 09 |  🚤  | <a href="https://www.acmicpc.net/problem/10775" target="_blank">10775</a> | <a href="https://www.acmicpc.net/problem/10775" target="_blank">공항</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | <a href="./../solution/disjoint_set/10775">바로가기</a> |
| 10 |     🚤     | <a href="https://www.acmicpc.net/problem/1043" target="_blank">1043</a> | <a href="https://www.acmicpc.net/problem/1043" target="_blank">거짓말</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/disjoint_set/1043">바로가기</a> |
| 11 |     🚤      | <a href="https://www.acmicpc.net/problem/20040" target="_blank">20040</a> | <a href="https://www.acmicpc.net/problem/20040" target="_blank">사이클 게임</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |      
| 12 |      🚤     |<a href="https://programmers.co.kr/learn/courses/30/lessons/12905" target="_blank">연습문제 (DP)</a>|<a href="https://programmers.co.kr/learn/courses/30/lessons/12905" target="_blank">가장 큰 정사각형 찾기</a>|Level 2|[바로가기](https://github.com/Altu-Bitu/Notice/blob/main/11%EC%9B%94%2023%EC%9D%BC%20-%20%EC%9C%A0%EB%8B%88%EC%98%A8%20%ED%8C%8C%EC%9D%B8%EB%93%9C/%EA%B3%BC%EC%A0%9C/biggestSquare.cpp)|
| 13 |                      | <a href="https://www.acmicpc.net/problem/17352" target="_blank">17352</a> | <a href="https://www.acmicpc.net/problem/17352" target="_blank">여러분의 다리가 되어 드리겠습니다!</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/disjoint_set/17352">바로가기</a> |
| 14 |                      | <a href="https://www.acmicpc.net/problem/7511" target="_blank">7511</a> | <a href="https://www.acmicpc.net/problem/7511" target="_blank">소셜 네트워킹 어플리케이션</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 15 |                      | <a href="https://www.acmicpc.net/problem/12893" target="_blank">12893</a> | <a href="https://www.acmicpc.net/problem/12893" target="_blank">적의 적</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 16 |                      | <a href="https://www.acmicpc.net/problem/16168" target="_blank">16168</a> | <a href="https://www.acmicpc.net/problem/16168" target="_blank">퍼레이드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 17 |                      | <a href="https://www.acmicpc.net/problem/20955" target="_blank">20955</a> | <a href="https://www.acmicpc.net/problem/20955" target="_blank">민서의 응급 수술</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 18 |                      | <a href="https://www.acmicpc.net/problem/15789" target="_blank">15789</a> | <a href="https://www.acmicpc.net/problem/15789" target="_blank">CTP 왕국은 한솔 왕국을 이길 수 있을까?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 19 |                      | <a href="https://www.acmicpc.net/problem/11085" target="_blank">11085</a> | <a href="https://www.acmicpc.net/problem/11085" target="_blank">군사 이동</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 20 |                      | <a href="https://www.acmicpc.net/problem/17090" target="_blank">17090</a> | <a href="https://www.acmicpc.net/problem/17090" target="_blank">미로 탈출하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 21 |                      | <a href="https://www.acmicpc.net/problem/14595" target="_blank">14595</a> | <a href="https://www.acmicpc.net/problem/14595" target="_blank">동방 프로젝트 (Large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 22 |                      | <a href="https://www.acmicpc.net/problem/3108" target="_blank">3108</a> | <a href="https://www.acmicpc.net/problem/3108" target="_blank">로고</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 23 |                      | <a href="https://www.acmicpc.net/problem/17398" target="_blank">17398</a> | <a href="https://www.acmicpc.net/problem/17398" target="_blank">통신망 분할</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/15.svg"/> |                      |